# Welcome!

Food safety and agricultural sustainability benefit from timely management practices that reduce losses and optimize inputs (water, fertilization, and labor). In cucumber crops, the phenological stage is a key indicator for planning tasks and monitoring crop development under real conditions.

**NALEF Food Safety** proposes a computer vision task: given an image of a cucumber crop taken with a camera or smartphone, you must predict the growth stage among five distinct classes. The challenge includes real field variability (lighting, framing, occlusions, and background) and a natural class imbalance.

## Baseline
To help you get started, we have provided a simple baseline solution in Google Colab. You can use this notebook to understand the data loading process and create your first submission:

[Open Baseline in Colab (Example)](https://colab.research.google.com/)

## Submission Format
Your submission must be a CSV file named `submission.csv` with two columns: `image_id` and `stage_pred`. Ensure your predictions match the allowed classes.

## References
* Menco-Tovar, A., Martinez-Santos, J. C., & Puertas, E. (2026). Detection of diseases in cucumber using deep neural networks. Neural Computing And Applications, 38(5). https://doi.org/10.1007/s00521-026-11945-z
