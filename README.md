# NALEF Food Safety - Codabench Challenge

This repository contains the source code and configuration for the NALEF Food Safety challenge on Codabench.

## Objective
Predict crop growth stages using computer vision to enhance food safety and agricultural sustainability.

## Project Structure
- `html/`: Markdown pages for the Codabench challenge description.
- `img/`: Images used in the challenge description.
- `ingestion_program/`: Contains the script that feeds data to the models.
- `scoring_program/`: Contains the script that evaluates the predictions.
- `public_data/` & `reference_data/`: Sample datasets for testing.
- `competition.yaml`: Codabench configuration file.
- `create_bundle.py`: Automation script to generate the final challenge bundle.

## How to generate the bundle

You no longer need to manually compress the folders. Simply run the Python script provided:

```bash
python create_bundle.py
```

This script will automatically create the necessary `.zip` files (`ingestion_program.zip`, `scoring_program.zip`, `public_data.zip`, `reference_data.zip`) and package everything into a final `bundle_reto.zip` ready to be uploaded to Codabench.

## Uploading to Codabench
Once generated, upload `bundle_reto.zip` directly to the Codabench platform.