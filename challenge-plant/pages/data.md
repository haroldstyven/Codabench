# Data

This challenge uses a real-world dataset of cucumber crop images captured under field conditions. The images exhibit natural variations in lighting, framing, background, and plant appearance that reflect the complexity of agricultural computer vision tasks.

---

## Download

The complete dataset is publicly available on **Zenodo**, a trusted open-access repository for research data. You can download the images using the following link:

**[https://zenodo.org/records/19192941](https://zenodo.org/records/19192941)**

The dataset is released under a **Creative Commons Attribution 4.0 International (CC BY 4.0)** license, allowing you to use, share, and adapt the data with proper attribution.

<table style="border-collapse: collapse; width: 100%;">
  <tr style="background-color: #f2f2f2;">
    <th style="border: 1px solid #ddd; padding: 12px; text-align: left;">File</th>
    <th style="border: 1px solid #ddd; padding: 12px; text-align: left;">Size</th>
    <th style="border: 1px solid #ddd; padding: 12px; text-align: left;">Description</th>
  </tr>
  <tr>
    <td style="border: 1px solid #ddd; padding: 12px;"><code>train_images.zip</code></td>
    <td style="border: 1px solid #ddd; padding: 12px;">5.2 GB</td>
    <td style="border: 1px solid #ddd; padding: 12px;">Training images organized by class</td>
  </tr>
  <tr style="background-color: #f9f9f9;">
    <td style="border: 1px solid #ddd; padding: 12px;"><code>val_images.zip</code></td>
    <td style="border: 1px solid #ddd; padding: 12px;">594 MB</td>
    <td style="border: 1px solid #ddd; padding: 12px;">Validation images for submission</td>
  </tr>
</table>

---

## Dataset Structure

The dataset is divided into two sets: a labeled training set for model development and an unlabeled validation set for competition submissions.

### Training Set

The training images are organized in a folder hierarchy where each subfolder name indicates the phenological stage and capture device:

```
train_images/
├── plantula_camera/
├── plantula_smartphone/
├── early_vegetative_camera/
├── early_vegetative_smartphone/
├── vegetative_growth_camera/
├── vegetative_growth_smartphone/
├── flowering_camera/
├── flowering_smartphone/
├── fruit_setting_camera/
└── fruit_setting_smartphone/
```

**Extracting labels:** The class label is the folder name without the device suffix. For example, all images in `flowering_camera/` and `flowering_smartphone/` belong to the `flowering` class.

### Validation Set

The validation images are provided in a flat directory with anonymized filenames. Your task is to predict the phenological stage for each image and submit your predictions to Codabench.

```
val_images/
├── img_000001.jpg
├── img_000002.jpg
├── img_000003.jpg
└── ... (239 images total)
```

---

## Classes

The classification task involves five phenological stages that represent key milestones in cucumber crop development:

<table style="border-collapse: collapse; width: 100%;">
  <tr style="background-color: #f2f2f2;">
    <th style="border: 1px solid #ddd; padding: 12px; text-align: left;">Label</th>
    <th style="border: 1px solid #ddd; padding: 12px; text-align: left;">Stage</th>
    <th style="border: 1px solid #ddd; padding: 12px; text-align: left;">Description</th>
  </tr>
  <tr>
    <td style="border: 1px solid #ddd; padding: 12px;"><code>plantula</code></td>
    <td style="border: 1px solid #ddd; padding: 12px;">Seedling</td>
    <td style="border: 1px solid #ddd; padding: 12px;">Initial growth after germination</td>
  </tr>
  <tr style="background-color: #f9f9f9;">
    <td style="border: 1px solid #ddd; padding: 12px;"><code>early_vegetative</code></td>
    <td style="border: 1px solid #ddd; padding: 12px;">Early vegetative</td>
    <td style="border: 1px solid #ddd; padding: 12px;">Development of first true leaves</td>
  </tr>
  <tr>
    <td style="border: 1px solid #ddd; padding: 12px;"><code>vegetative_growth</code></td>
    <td style="border: 1px solid #ddd; padding: 12px;">Vegetative</td>
    <td style="border: 1px solid #ddd; padding: 12px;">Rapid leaf and stem expansion</td>
  </tr>
  <tr style="background-color: #f9f9f9;">
    <td style="border: 1px solid #ddd; padding: 12px;"><code>flowering</code></td>
    <td style="border: 1px solid #ddd; padding: 12px;">Flowering</td>
    <td style="border: 1px solid #ddd; padding: 12px;">Appearance of male and female flowers</td>
  </tr>
  <tr>
    <td style="border: 1px solid #ddd; padding: 12px;"><code>fruit_setting</code></td>
    <td style="border: 1px solid #ddd; padding: 12px;">Fruit setting</td>
    <td style="border: 1px solid #ddd; padding: 12px;">Formation and early growth of fruits</td>
  </tr>
</table>

---

## Dataset Characteristics

Understanding the dataset properties will help you design appropriate preprocessing and modeling strategies:

- **Capture devices:** Images were taken with both professional cameras and smartphones, introducing variation in resolution and quality
- **Class imbalance:** The distribution of images across classes is not uniform, reflecting natural field collection patterns
- **Visual variability:** Expect differences in lighting (sunny, cloudy, shadows), framing (close-up, wide shots), and backgrounds (soil, weeds, greenhouse structures)
- **Real-world conditions:** All images were captured in actual agricultural settings, not controlled laboratory environments
