# NALEF Food Safety - Scoring Program
# Computes Macro-F1 and Balanced Accuracy for phenological stage classification

import json
import os
import pandas as pd
from sklearn.metrics import f1_score

# Paths (Codabench standard paths for result submission)
input_dir = '/app/input'
output_dir = '/app/output/'
reference_dir = os.path.join(input_dir, 'ref')   # Ground truth
submission_dir = os.path.join(input_dir, 'res')  # Participant submission

score_file = os.path.join(output_dir, 'scores.json')
html_file = os.path.join(output_dir, 'detailed_results.html')

# Valid classes
CLASSES = [
    "plantula",
    "early_vegetative",
    "vegetative_growth",
    "flowering",
    "fruit_setting",
]

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

def evaluate(ground_truth_path: str, submission_path: str) -> dict:
    """
    Evaluate submission against ground truth.

    Args:
        ground_truth_path: CSV with columns [image_id, stage]
        submission_path: CSV with columns [image_id, stage_pred]

    Returns:
        dict with macro_f1 and balanced_accuracy scores
    """
    gt = pd.read_csv(ground_truth_path)
    sub = pd.read_csv(submission_path)

    # Validate ground truth columns
    if not {"image_id", "stage"}.issubset(gt.columns):
        raise ValueError("Ground truth must contain columns: image_id, stage")

    # Validate submission columns
    if not {"image_id", "stage_pred"}.issubset(sub.columns):
        raise ValueError("Submission must contain columns: image_id, stage_pred")

    # Merge to align predictions with ground truth
    df = gt.merge(sub, on="image_id", how="left")

    # Check for missing predictions
    missing = df["stage_pred"].isna().sum()
    if missing > 0:
        examples = df.loc[df["stage_pred"].isna(), "image_id"].head(10).tolist()
        raise ValueError(f"Missing predictions for {missing} images. Examples: {examples}")

    # Check for invalid labels
    invalid = ~df["stage_pred"].isin(CLASSES)
    if invalid.any():
        bad_vals = df.loc[invalid, "stage_pred"].value_counts().to_dict()
        raise ValueError(f"Invalid stage_pred labels found: {bad_vals}. Allowed: {CLASSES}")

    y_true = df["stage"].astype(str).tolist()
    y_pred = df["stage_pred"].astype(str).tolist()

    # Compute metric
    macro_f1 = f1_score(y_true, y_pred, average="macro", labels=CLASSES)

    return {
        "macro_f1": float(macro_f1),
    }

def generate_detailed_results(scores, y_true, y_pred):
    """Generate HTML with detailed results."""
    from sklearn.metrics import classification_report, confusion_matrix
    import numpy as np

    html = "<h1>NALEF Food Safety - Detailed Results</h1>"
    html += f"<h2>Score</h2>"
    html += f"<p><strong>Macro F1:</strong> {scores['macro_f1']:.4f}</p>"

    # Classification report
    html += "<h2>Classification Report</h2>"
    report = classification_report(y_true, y_pred, labels=CLASSES, output_dict=True)
    html += "<table border='1' style='border-collapse: collapse;'>"
    html += "<tr><th>Class</th><th>Precision</th><th>Recall</th><th>F1-Score</th><th>Support</th></tr>"
    for cls in CLASSES:
        if cls in report:
            r = report[cls]
            html += f"<tr><td>{cls}</td><td>{r['precision']:.3f}</td><td>{r['recall']:.3f}</td><td>{r['f1-score']:.3f}</td><td>{int(r['support'])}</td></tr>"
    html += "</table>"

    # Confusion matrix
    html += "<h2>Confusion Matrix</h2>"
    cm = confusion_matrix(y_true, y_pred, labels=CLASSES)
    html += "<table border='1' style='border-collapse: collapse;'>"
    html += "<tr><th></th>" + "".join([f"<th>{c}</th>" for c in CLASSES]) + "</tr>"
    for i, cls in enumerate(CLASSES):
        html += f"<tr><th>{cls}</th>" + "".join([f"<td>{cm[i,j]}</td>" for j in range(len(CLASSES))]) + "</tr>"
    html += "</table>"

    return html

def main():
    """Main scoring function."""
    print_bar()
    print('NALEF Food Safety - Scoring Program')
    print_bar()

    # Find files
    print('Looking for submission and ground truth files...')
    ground_truth_path = find_csv_file(reference_dir)
    submission_path = find_csv_file(submission_dir, required_name="submission.csv")

    print(f'Ground truth: {ground_truth_path}')
    print(f'Submission: {submission_path}')

    # Evaluate
    print_bar()
    print('Evaluating submission...')

    try:
        scores = evaluate(ground_truth_path, submission_path)
        print(f"Macro F1: {scores['macro_f1']:.4f}")

        # Write scores
        print_bar()
        print('Writing scores...')
        with open(score_file, 'w') as f:
            json.dump(scores, f)

        # Generate detailed results
        gt = pd.read_csv(ground_truth_path)
        sub = pd.read_csv(submission_path)
        df = gt.merge(sub, on="image_id", how="left")
        y_true = df["stage"].astype(str).tolist()
        y_pred = df["stage_pred"].astype(str).tolist()

        html = generate_detailed_results(scores, y_true, y_pred)
        write_file(html_file, html)

        print('Scoring completed successfully!')

    except Exception as e:
        print(f'ERROR: {str(e)}')
        # Write error to detailed results
        write_file(html_file, f"<h1>Error</h1><p style='color:red;'>{str(e)}</p>")
        # Write zero scores
        with open(score_file, 'w') as f:
            json.dump({"macro_f1": 0.0}, f)
        raise

    print_bar()

if __name__ == '__main__':
    main()
