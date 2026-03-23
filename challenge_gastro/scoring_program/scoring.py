# GastroCorp NER 2026 - Scoring Program
# Computes Span-level Micro-F1 and secondary metrics for NER

import json
import os
import pandas as pd

# Paths (Codabench standard paths for result submission)
input_dir = '/app/input'
output_dir = '/app/output/'
reference_dir = os.path.join(input_dir, 'ref')   # Ground truth
submission_dir = os.path.join(input_dir, 'res')  # Participant submission

score_file = os.path.join(output_dir, 'scores.json')
html_file = os.path.join(output_dir, 'detailed_results.html')

CLASSES = ["DISH", "BEVERAGE", "INGREDIENT", "BRAND"]
VALID_TAGS = {"O"} | {f"B-{c}" for c in CLASSES} | {f"I-{c}" for c in CLASSES}

def write_file(file, content):
    """Write content to file."""
    with open(file, 'a', encoding="utf-8") as f:
        f.write(content)

def print_bar():
    """Display a separator bar."""
    print('-' * 50)

def find_csv_file(directory, required_name=None):
    """Find a CSV file in the directory."""
    for f in os.listdir(directory):
        if f.endswith('.csv'):
            if required_name and f != required_name:
                raise ValueError(f"CSV file must be named '{required_name}', but found '{f}'")
            return os.path.join(directory, f)
    raise FileNotFoundError(f"No CSV file found in {directory}")

def extract_spans(labels):
    """Extract entities (type, start, end) from IOB2 labels."""
    spans = set()
    current_type = None
    start = None
    for i, label in enumerate(labels):
        if label.startswith("B-"):
            if current_type is not None:
                spans.add((current_type, start, i - 1))
            current_type = label[2:]
            start = i
        elif label.startswith("I-"):
            if current_type != label[2:]:
                if current_type is not None:
                    spans.add((current_type, start, i - 1))
                current_type = label[2:]
                start = i
        else:
            if current_type is not None:
                spans.add((current_type, start, i - 1))
            current_type = None
            start = None
    if current_type is not None:
        spans.add((current_type, start, len(labels) - 1))
    return spans

def evaluate(ground_truth_path: str, submission_path: str):
    gt = pd.read_csv(ground_truth_path)
    sub = pd.read_csv(submission_path)

    # Validate columns
    if not {"sequence_id", "token_index", "tag"}.issubset(gt.columns):
        raise ValueError("Ground truth must contain columns: sequence_id, token_index, tag")
    if not {"sequence_id", "token_index", "predicted_tag"}.issubset(sub.columns):
        raise ValueError("Submission must contain columns: sequence_id, token_index, predicted_tag")

    df = gt.merge(sub, on=["sequence_id", "token_index"], how="left")

    # Check for missing predictions
    missing = df["predicted_tag"].isna().sum()
    if missing > 0:
        raise ValueError(f"Missing predictions for {missing} tokens.")

    # Check for invalid tags
    invalid = ~df["predicted_tag"].isin(VALID_TAGS)
    if invalid.any():
        bad_vals = df.loc[invalid, "predicted_tag"].unique().tolist()
        raise ValueError(f"Invalid tags found: {bad_vals}. Allowed: {VALID_TAGS}")

    tp, fp, fn = 0, 0, 0
    tp_c = {c: 0 for c in CLASSES}
    fp_c = {c: 0 for c in CLASSES}
    fn_c = {c: 0 for c in CLASSES}

    for seq_id, group in df.groupby("sequence_id"):
        group = group.sort_values("token_index")
        gold_tags = group["tag"].tolist()
        pred_tags = group["predicted_tag"].tolist()

        gold_spans = extract_spans(gold_tags)
        pred_spans = extract_spans(pred_tags)

        # Calculate True Positives and False Positives
        for span in pred_spans:
            c = span[0]
            if c not in CLASSES: continue
            if span in gold_spans:
                tp += 1
                tp_c[c] += 1
            else:
                fp += 1
                fp_c[c] += 1
        
        # Calculate False Negatives
        for span in gold_spans:
            c = span[0]
            if c not in CLASSES: continue
            if span not in pred_spans:
                fn += 1
                fn_c[c] += 1

    denominator = 2 * tp + fp + fn
    micro_f1 = (2 * tp) / denominator if denominator > 0 else 0.0

    f1_c = {}
    for c in CLASSES:
        den = 2 * tp_c[c] + fp_c[c] + fn_c[c]
        f1_c[c] = (2 * tp_c[c]) / den if den > 0 else 0.0

    macro_f1 = sum(f1_c.values()) / len(CLASSES)

    scores = {
        "micro_f1": float(micro_f1),
        "macro_f1": float(macro_f1)
    }

    return scores, tp_c, fp_c, fn_c, f1_c

def generate_detailed_results(scores, tp_c, fp_c, fn_c, f1_c):
    """Generate HTML with detailed results."""
    html = "<div style='font-family: sans-serif;'>"
    html += "<h2>GastroCorp NER 2026 - Detailed Results</h2>"
    html += f"<h3>Overall Scores</h3>"
    html += f"<p><strong>Micro F1 (Primary Metric):</strong> {scores['micro_f1']:.4f}</p>"
    html += f"<p><strong>Macro F1:</strong> {scores['macro_f1']:.4f}</p>"

    html += "<h3>Span-level Performance per Entity Type</h3>"
    html += "<table border='1' style='border-collapse: collapse; text-align: center;' cellpadding='5'>"
    html += "<tr style='background-color: #f2f2f2;'><th>Entity Type</th><th>True Positives</th><th>False Positives</th><th>False Negatives</th><th>F1-Score</th></tr>"
    for c in CLASSES:
        html += f"<tr><td>{c}</td><td>{tp_c[c]}</td><td>{fp_c[c]}</td><td>{fn_c[c]}</td><td>{f1_c[c]:.4f}</td></tr>"
    html += "</table>"
    html += "</div>"
    return html

def main():
    print_bar()
    print('GastroCorp NER 2026 - Scoring Program')
    print_bar()

    print('Looking for submission and ground truth files...')
    try:
        ground_truth_path = find_csv_file(reference_dir)
        submission_path = find_csv_file(submission_dir, required_name="submission.csv")

        print(f'Ground truth: {ground_truth_path}')
        print(f'Submission: {submission_path}')

        print_bar()
        print('Evaluating submission...')
        scores, tp_c, fp_c, fn_c, f1_c = evaluate(ground_truth_path, submission_path)
        print(f"Micro-F1: {scores['micro_f1']:.4f}")

        print_bar()
        print('Writing scores...')
        with open(score_file, 'w') as f:
            json.dump(scores, f)

        html = generate_detailed_results(scores, tp_c, fp_c, fn_c, f1_c)
        with open(html_file, 'w', encoding="utf-8") as f:
            f.write(html)

        print('Scoring completed successfully!')

    except Exception as e:
        print(f'ERROR: {str(e)}')
        with open(html_file, 'w', encoding="utf-8") as f:
            f.write(f"<h2>Error</h2><p style='color:red;'>{str(e)}</p>")
        with open(score_file, 'w') as f:
            json.dump({"micro_f1": 0.0, "macro_f1": 0.0}, f)
        raise

    print_bar()

if __name__ == '__main__':
    main()
