# NALEF Food Safety

Food safety and agricultural sustainability benefit from timely management practices that reduce losses and optimize inputs (water, fertilization, and labor). In cucumber crops, the phenological stage is a key indicator for planning tasks and monitoring crop development under real conditions.

**NALEF Food Safety** proposes a computer vision task: given an image of a cucumber crop taken with a camera or smartphone, you must predict the growth stage among five distinct classes. The challenge includes real field variability (lighting, framing, occlusions, and background) and a natural class imbalance.

---

## Task

Classify each cucumber crop image into one of the following **five phenological stages**:

<table style="border-collapse: collapse; width: 100%;">
  <tr style="background-color: #f2f2f2;">
    <th style="border: 1px solid #ddd; padding: 12px; text-align: left;">Class</th>
    <th style="border: 1px solid #ddd; padding: 12px; text-align: left;">Description</th>
  </tr>
  <tr>
    <td style="border: 1px solid #ddd; padding: 12px;"><code>plantula</code></td>
    <td style="border: 1px solid #ddd; padding: 12px;">Seedling stage</td>
  </tr>
  <tr style="background-color: #f9f9f9;">
    <td style="border: 1px solid #ddd; padding: 12px;"><code>early_vegetative</code></td>
    <td style="border: 1px solid #ddd; padding: 12px;">Early vegetative growth</td>
  </tr>
  <tr>
    <td style="border: 1px solid #ddd; padding: 12px;"><code>vegetative_growth</code></td>
    <td style="border: 1px solid #ddd; padding: 12px;">Vegetative growth</td>
  </tr>
  <tr style="background-color: #f9f9f9;">
    <td style="border: 1px solid #ddd; padding: 12px;"><code>flowering</code></td>
    <td style="border: 1px solid #ddd; padding: 12px;">Flowering stage</td>
  </tr>
  <tr>
    <td style="border: 1px solid #ddd; padding: 12px;"><code>fruit_setting</code></td>
    <td style="border: 1px solid #ddd; padding: 12px;">Fruit setting stage</td>
  </tr>
</table>

---

## Timeline

<table style="border-collapse: collapse; width: 100%;">
  <tr style="background-color: #f2f2f2;">
    <th style="border: 1px solid #ddd; padding: 12px; text-align: left;">Event</th>
    <th style="border: 1px solid #ddd; padding: 12px; text-align: left;">Date</th>
  </tr>
  <tr>
    <td style="border: 1px solid #ddd; padding: 12px;">Challenge opens</td>
    <td style="border: 1px solid #ddd; padding: 12px;">March 18, 2026</td>
  </tr>
  <tr style="background-color: #f9f9f9;">
    <td style="border: 1px solid #ddd; padding: 12px;">Submissions open</td>
    <td style="border: 1px solid #ddd; padding: 12px;">March 18, 2026</td>
  </tr>
  <tr>
    <td style="border: 1px solid #ddd; padding: 12px;">Submissions close</td>
    <td style="border: 1px solid #ddd; padding: 12px;">April 30, 2026</td>
  </tr>
  <tr style="background-color: #f9f9f9;">
    <td style="border: 1px solid #ddd; padding: 12px;">Paper deadline</td>
    <td style="border: 1px solid #ddd; padding: 12px;">April 30, 2026</td>
  </tr>
</table>

---

## Quick Start

1. **Download** the dataset from [Zenodo](https://doi.org/10.5281/zenodo.19073937)
2. **Train** your model using `train_images/`
3. **Predict** labels for all images in `val_images/`
4. **Submit** your predictions following the format below

---

## Submission Format

Your submission must follow this **exact structure**:

```
submission.zip
└── submission.csv
```

The CSV file must be named **`submission.csv`** and contain two columns:

```csv
image_id,stage_pred
img_000001.jpg,plantula
img_000002.jpg,flowering
img_000003.jpg,vegetative_growth
...
```

<table style="border-collapse: collapse; width: 100%;">
  <tr style="background-color: #f2f2f2;">
    <th style="border: 1px solid #ddd; padding: 12px; text-align: left;">Column</th>
    <th style="border: 1px solid #ddd; padding: 12px; text-align: left;">Description</th>
  </tr>
  <tr>
    <td style="border: 1px solid #ddd; padding: 12px;"><code>image_id</code></td>
    <td style="border: 1px solid #ddd; padding: 12px;">Image filename as it appears in <code>val_images/</code></td>
  </tr>
  <tr style="background-color: #f9f9f9;">
    <td style="border: 1px solid #ddd; padding: 12px;"><code>stage_pred</code></td>
    <td style="border: 1px solid #ddd; padding: 12px;">Predicted class (one of the 5 valid labels)</td>
  </tr>
</table>

**Valid labels:** `plantula` · `early_vegetative` · `vegetative_growth` · `flowering` · `fruit_setting`

---

## References

Menco-Tovar, A., Martinez-Santos, J. C., & Puertas, E. (2026). Detection of diseases in cucumber using deep neural networks. *Neural Computing And Applications*, 38(5). [https://doi.org/10.1007/s00521-026-11945-z](https://doi.org/10.1007/s00521-026-11945-z)
