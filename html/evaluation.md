# Evaluation Metrics

The performance of the models will be evaluated using two metrics, taking the natural class imbalance into account.

## Primary Metric: Macro-F1
The official ranking score is the **Macro-F1**. This metric averages the F1-Score for each class equally, without favoring the majority classes.

## Secondary Metric: Balanced Accuracy
We also compute the **Balanced Accuracy** to report balanced performance across classes (average recall obtained on each class).

## Practical Example
Suppose you have the following predictions in your `submission.csv`:

```csv
image_id,stage_pred
vegetative_growth_smartphone_000901.jpg,vegetative_growth
plantula_camera_000012.jpg,plantula
flowering_smartphone_000455.jpg,flowering
fruit_setting_camera_000777.jpg,fruit_setting
early_vegetative_camera_000120.jpg,early_vegetative
```

The scoring program will merge this file with the private ground truth on `image_id`. It will then calculate the Macro-F1 across the 5 valid labels: `plantula`, `early_vegetative`, `vegetative_growth`, `flowering`, and `fruit_setting`.
