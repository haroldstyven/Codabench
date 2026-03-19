# Dataset Description

The dataset contains approximately 1000 images taken under real conditions. It is organized into 10 folders combining the crop's stage and the device used:

* `plantula_camera`, `plantula_smartphone`
* `early_vegetative_camera`, `early_vegetative_smartphone`
* `vegetative_growth_camera`, `vegetative_growth_smartphone`
* `flowering_camera`, `flowering_smartphone`
* `fruit_setting_camera`, `fruit_setting_smartphone`

## Characteristics

* **Capture domains:** Camera and Smartphone.
* **Class imbalance:** The number of images per folder is not uniform.
* **Variability:** Different framing, lighting, occlusions, and presence of soil/weeds.

## Structure & Access

`train/` and `val/` folders include labels, while `test/` does not. We provide CSV files (`train.csv`, `val.csv`, `test.csv`) to facilitate data loading.

> **Important:** Challenge images are not embedded here. Please download the dataset directly from Zenodo.

[Download Dataset from Zenodo (19073937)](https://zenodo.org/records/19073937)
