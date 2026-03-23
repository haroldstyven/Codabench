# Evaluation

This section describes how submissions are scored and ranked. Understanding the evaluation criteria will help you optimize your model for the competition objectives.

---

## Metric: Macro F1-Score

Given the natural class imbalance present in agricultural datasets, we selected **Macro F1-Score** as the official ranking metric. Unlike accuracy, Macro F1 treats all classes equally by computing the F1-score for each class independently and then averaging them. This ensures that models must perform well across all phenological stages, not just the most frequent ones.

For each class *c*, the F1-score is the harmonic mean of precision and recall:

$$F_1(c) = \frac{2 \cdot \text{Precision}(c) \cdot \text{Recall}(c)}{\text{Precision}(c) + \text{Recall}(c)}$$

The Macro F1 averages over all *C* = 5 classes:

$$\text{Macro-}F_1 = \frac{1}{C} \sum_{c=1}^{C} F_1(c)$$

A score of **1.0** indicates perfect classification across all classes, while **0.0** indicates complete failure. Scores typically range between **0.2** and **0.9** depending on model quality and the inherent difficulty of distinguishing phenological stages.

---

## Submission Format

To evaluate your model, you must submit your predictions in a specific format. The system expects a ZIP archive containing a single CSV file with your predictions for all validation images.

**Required structure:**

```
submission.zip
└── submission.csv
```

The CSV file must contain exactly two columns:

<table style="border-collapse: collapse; width: 100%;">
  <tr style="background-color: #f2f2f2;">
    <th style="border: 1px solid #ddd; padding: 12px; text-align: left;">Column</th>
    <th style="border: 1px solid #ddd; padding: 12px; text-align: left;">Type</th>
    <th style="border: 1px solid #ddd; padding: 12px; text-align: left;">Description</th>
  </tr>
  <tr>
    <td style="border: 1px solid #ddd; padding: 12px;"><code>image_id</code></td>
    <td style="border: 1px solid #ddd; padding: 12px;">string</td>
    <td style="border: 1px solid #ddd; padding: 12px;">Image filename (e.g., <code>img_000001.jpg</code>)</td>
  </tr>
  <tr style="background-color: #f9f9f9;">
    <td style="border: 1px solid #ddd; padding: 12px;"><code>stage_pred</code></td>
    <td style="border: 1px solid #ddd; padding: 12px;">string</td>
    <td style="border: 1px solid #ddd; padding: 12px;">Predicted class label</td>
  </tr>
</table>

### Example: submission.csv

```csv
image_id,stage_pred
img_000001.jpg,vegetative_growth
img_000002.jpg,plantula
img_000003.jpg,flowering
img_000004.jpg,fruit_setting
img_000005.jpg,early_vegetative
```

---

## Valid Labels

Your predictions must use exactly these five class labels. Any variation in spelling, capitalization, or formatting will result in an error.

- `plantula`
- `early_vegetative`
- `vegetative_growth`
- `flowering`
- `fruit_setting`

---

## Common Errors

Before submitting, verify that your file meets all requirements. The following table lists frequent issues that cause submissions to fail:

<table style="border-collapse: collapse; width: 100%;">
  <tr style="background-color: #f2f2f2;">
    <th style="border: 1px solid #ddd; padding: 12px; text-align: left;">Error</th>
    <th style="border: 1px solid #ddd; padding: 12px; text-align: left;">Cause</th>
  </tr>
  <tr>
    <td style="border: 1px solid #ddd; padding: 12px;">Wrong CSV name</td>
    <td style="border: 1px solid #ddd; padding: 12px;">File must be named exactly <code>submission.csv</code></td>
  </tr>
  <tr style="background-color: #f9f9f9;">
    <td style="border: 1px solid #ddd; padding: 12px;">Missing predictions</td>
    <td style="border: 1px solid #ddd; padding: 12px;">CSV must include all 97 images from <code>val_images/</code></td>
  </tr>
  <tr>
    <td style="border: 1px solid #ddd; padding: 12px;">Invalid label</td>
    <td style="border: 1px solid #ddd; padding: 12px;">Only the 5 defined classes are accepted</td>
  </tr>
  <tr style="background-color: #f9f9f9;">
    <td style="border: 1px solid #ddd; padding: 12px;">Wrong columns</td>
    <td style="border: 1px solid #ddd; padding: 12px;">CSV must have exactly <code>image_id</code> and <code>stage_pred</code> columns</td>
  </tr>
  <tr>
    <td style="border: 1px solid #ddd; padding: 12px;">Incorrect filename</td>
    <td style="border: 1px solid #ddd; padding: 12px;">Image filenames must match exactly (case-sensitive)</td>
  </tr>
  <tr style="background-color: #f9f9f9;">
    <td style="border: 1px solid #ddd; padding: 12px;">Not zipped</td>
    <td style="border: 1px solid #ddd; padding: 12px;">Upload <code>submission.zip</code>, not a raw CSV file</td>
  </tr>
</table>

---

## Ranking

The public leaderboard displays all valid submissions ranked by **Macro F1-Score** in descending order. Higher scores indicate better performance. In case of tied scores, the earlier submission takes precedence.
