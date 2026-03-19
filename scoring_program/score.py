import os
import sys
import json
import pandas as pd
from sklearn.metrics import accuracy_score, f1_score

def score():
    input_dir = sys.argv[1]  # Contiene subcarpetas 'res' y 'ref'
    output_dir = sys.argv[2] # Donde guardamos scores.json

    res_dir = os.path.join(input_dir, 'res')
    ref_dir = os.path.join(input_dir, 'ref')

    # Leer soluciones reales y predicciones
    y_true = pd.read_csv(os.path.join(ref_dir, 'solution.csv'))['target'].values
    with open(os.path.join(res_dir, 'results.txt'), 'r') as f:
        y_pred = [int(line.strip()) for line in f.readlines()]

    # Calcular métricas
    acc = accuracy_score(y_true, y_pred)
    f1 = f1_score(y_true, y_pred, average='macro')

    scores = {
        "accuracy": float(acc),
        "f1_score": float(f1)
    }

    with open(os.path.join(output_dir, 'scores.json'), 'w') as f:
        json.dump(scores, f)

if __name__ == "__main__":
    score()