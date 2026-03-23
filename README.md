# Codabench Challenges

This repository contains the source code and configurations for two shared tasks on Codabench.

## Task 1: NALEF Food Safety

**Objective:** Predict crop growth stages using computer vision to enhance food safety and agricultural sustainability.
**Bundle:** `bundle_reto.zip`

### Structure (Root Directory)
- `html/`: Markdown pages for the Codabench challenge description.
- `img/`: Images used in the challenge description.
- `ingestion_program/`: Script that feeds data to the models.
- `scoring_program/`: Script that evaluates the predictions (Macro F1).
- `public_data/` & `reference_data/`: Sample datasets for testing.
- `competition.yaml`: Codabench configuration file for Task 1.

---

## Task 2: GastroCorp NER 2026

**Objective:** Named Entity Recognition over a bilingual (Spanish–English) gastronomic corpus. Participants must assign an IOB2 entity label to sequences of tokens, recognizing entities like DISH, BRAND, BEVERAGE, and INGREDIENT.
**Bundle:** `challenge-plant.zip`

### Structure (`challenge-plant/` Directory)
- `pages/`: Markdown pages for the Codabench challenge description.
- `img/`: Images used in the challenge description.
- `scoring_program/`: Evaluates predictions using exact-boundary Span-Level Micro F1 score.
- `reference_data/`: Ground truth sample dataset with dummy IOB2 tags.
- `competition.yaml`: Codabench configuration file for Task 2.

---

## How to generate the bundles

You no longer need to manually compress the folders. Simply run the unified Python script provided in the root directory:

```bash
python create_bundle.py
```

This script will automatically iterate through both tasks, package their necessary `.zip` folders internally, and then create the final ready-to-upload bundles:
1. `bundle_reto.zip` (Task 1)
2. `challenge-plant.zip` (Task 2)

## Uploading to Codabench
Once generated, upload `bundle_reto.zip` and `challenge-plant.zip` directly to the Codabench platform in their respective challenge creations.