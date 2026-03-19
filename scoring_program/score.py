import os
import sys
import json
import pandas as pd
from sklearn.metrics import f1_score, balanced_accuracy_score

CLASSES = [
    "plantula",
    "early_vegetative",
    "vegetative_growth",
    "flowering",
    "fruit_setting",
]

def score():
    # Codabench passes input and output directories as arguments
    input_dir = sys.argv[1]
    output_dir = sys.argv[2]

    res_dir = os.path.join(input_dir, 'res')
    ref_dir = os.path.join(input_dir, 'ref')

    submission_files = [f for f in os.listdir(res_dir) if f.endswith('.csv')]
    truth_files = [f for f in os.listdir(ref_dir) if f.endswith('.csv')]
    
    if not submission_files:
        raise ValueError("No submission CSV found in the uploaded file.")
    if not truth_files:
        raise ValueError("No ground truth file found in reference_data.")

    submission_path = os.path.join(res_dir, submission_files[0])
    truth_path = os.path.join(ref_dir, truth_files[0])

    gt = pd.read_csv(truth_path)
    sub = pd.read_csv(submission_path)

    # Validate columns
    if not {"image_id", "stage"}.issubset(gt.columns):
        raise ValueError("Ground truth must contain columns: image_id, stage")
    if not {"image_id", "stage_pred"}.issubset(sub.columns):
        raise ValueError("Submission must contain columns: image_id, stage_pred")

    # Merge ensures we score exactly the test set and detect missing preds
    df = gt.merge(sub, on="image_id", how="left")

    # Missing predictions
    missing = df["stage_pred"].isna().sum()
    if missing > 0:
        examples = df.loc[df["stage_pred"].isna(), "image_id"].head(10).tolist()
        raise ValueError(f"Missing predictions for {missing} images. Examples: {examples}")

    # Invalid labels
    invalid = ~df["stage_pred"].isin(CLASSES)
    if invalid.any():
        bad_vals = df.loc[invalid, "stage_pred"].value_counts().to_dict()
        raise ValueError(f"Invalid stage_pred labels found: {bad_vals}. Allowed: {CLASSES}")

    y_true = df["stage"].astype(str).tolist()
    y_pred = df["stage_pred"].astype(str).tolist()

    macro_f1 = f1_score(y_true, y_pred, average="macro", labels=CLASSES)
    bal_acc = balanced_accuracy_score(y_true, y_pred)

    scores = {
        "macro_f1": float(macro_f1),
        "balanced_accuracy": float(bal_acc)
    }

    with open(os.path.join(output_dir, 'scores.json'), 'w') as f:
        json.dump(scores, f)

if __name__ == "__main__":
    score()