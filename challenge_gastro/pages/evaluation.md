# Evaluation

### Primary metric: Span-level Micro-F1 (exact match)

The official ranking metric is **span-level micro-average F1 with exact boundary match**. A predicted entity span is counted as a True Positive if and only if both its boundaries and its entity type match the gold annotation exactly. Partial boundary overlaps are not credited.

For each entity type $c$:

$$F_1(c) = \frac{2 \cdot \text{TP}_c}{2 \cdot \text{TP}_c + \text{FP}_c + \text{FN}_c}$$

The final score micro-averages across all entity types:

$$\text{Micro-F1} = \frac{2 \cdot \sum_c \text{TP}_c}{2 \cdot \sum_c \text{TP}_c + \sum_c \text{FP}_c + \sum_c \text{FN}_c}$$

**Rationale for exact match.** In downstream applications such as machine translation augmentation, a partially recognized entity (e.g., identifying only *Pizza* from *Pizza Margarita*) is effectively unusable. Exact boundary recovery is therefore the operationally meaningful criterion.

---

## Secondary metrics (reported, not used for ranking)

<table style="border-collapse: collapse; width: 100%;">
  <tr style="background-color: #f2f2f2;">
    <th style="border: 1px solid #ddd; padding: 12px; text-align: left;">Metric</th>
    <th style="border: 1px solid #ddd; padding: 12px; text-align: left;">Description</th>
  </tr>
  <tr>
    <td style="border: 1px solid #ddd; padding: 12px;">Macro-F1</td>
    <td style="border: 1px solid #ddd; padding: 12px;">F1 averaged equally across all 4 entity types; highlights performance on low-frequency entities (BRAND, BEVERAGE)</td>
  </tr>
  <tr style="background-color: #f9f9f9;">
    <td style="border: 1px solid #ddd; padding: 12px;">Per-entity F1</td>
    <td style="border: 1px solid #ddd; padding: 12px;">Individual F1 for each of DISH, BEVERAGE, INGREDIENT, BRAND</td>
  </tr>
  <tr>
    <td style="border: 1px solid #ddd; padding: 12px;">Micro-F1 per sub-domain</td>
    <td style="border: 1px solid #ddd; padding: 12px;">Separate scores for the menus and recipes sub-domains</td>
  </tr>
</table>

---

## Baseline results (majority-class)

The following scores provide a lower-bound reference obtained with the majority-class baseline included in the starter kit:

<table style="border-collapse: collapse; width: 100%;">
  <tr style="background-color: #f2f2f2;">
    <th style="border: 1px solid #ddd; padding: 12px; text-align: left;">Sub-domain</th>
    <th style="border: 1px solid #ddd; padding: 12px; text-align: left;">Micro-F1</th>
  </tr>
  <tr>
    <td style="border: 1px solid #ddd; padding: 12px;">Menus</td>
    <td style="border: 1px solid #ddd; padding: 12px;"><em>to be reported</em></td>
  </tr>
  <tr style="background-color: #f9f9f9;">
    <td style="border: 1px solid #ddd; padding: 12px;">Recipes</td>
    <td style="border: 1px solid #ddd; padding: 12px;"><em>to be reported</em></td>
  </tr>
</table>

> Baseline results will be published on the leaderboard at challenge opening.

---

## Ranking

The public leaderboard ranks all valid submissions by **Micro-F1 (span-level, exact match)** in descending order. In the event of a tie, the earlier submission takes precedence. The leaderboard is updated after each valid submission.

**Submission limits:** 5 submissions per day · 100 submissions total.

---

## Submission Format

### File structure

```
submission.zip
└── submission.csv
```

### CSV format

The file must be named exactly `submission.csv` and contain three columns with no header variations:

```csv
sequence_id,token_index,predicted_tag
menu_000001,0,B-DISH
menu_000001,1,I-DISH
menu_000001,2,O
menu_000001,3,B-INGREDIENT
menu_000001,4,I-INGREDIENT
menu_000001,5,O
menu_000001,6,B-BRAND
```

<table style="border-collapse: collapse; width: 100%;">
  <tr style="background-color: #f2f2f2;">
    <th style="border: 1px solid #ddd; padding: 12px; text-align: left;">Column</th>
    <th style="border: 1px solid #ddd; padding: 12px; text-align: left;">Type</th>
    <th style="border: 1px solid #ddd; padding: 12px; text-align: left;">Description</th>
  </tr>
  <tr>
    <td style="border: 1px solid #ddd; padding: 12px;"><code>sequence_id</code></td>
    <td style="border: 1px solid #ddd; padding: 12px;">string</td>
    <td style="border: 1px solid #ddd; padding: 12px;">Sequence identifier matching the <code>id</code> field in the dataset</td>
  </tr>
  <tr style="background-color: #f9f9f9;">
    <td style="border: 1px solid #ddd; padding: 12px;"><code>token_index</code></td>
    <td style="border: 1px solid #ddd; padding: 12px;">integer</td>
    <td style="border: 1px solid #ddd; padding: 12px;">Zero-based position of the token within the sequence</td>
  </tr>
  <tr>
    <td style="border: 1px solid #ddd; padding: 12px;"><code>predicted_tag</code></td>
    <td style="border: 1px solid #ddd; padding: 12px;">string</td>
    <td style="border: 1px solid #ddd; padding: 12px;">Predicted IOB2 tag</td>
  </tr>
</table>

### Requirements

- The submission must include predictions for **every token** in **every sequence** of the evaluation set
- All nine valid tags must be spelled exactly as shown (case-sensitive)
- Sequences must be submitted in any order; token indices within each sequence must be complete and contiguous starting from 0
- The archive must contain exactly one file named `submission.csv`

---

## Common errors

<table style="border-collapse: collapse; width: 100%;">
  <tr style="background-color: #f2f2f2;">
    <th style="border: 1px solid #ddd; padding: 12px; text-align: left;">Error</th>
    <th style="border: 1px solid #ddd; padding: 12px; text-align: left;">Cause</th>
    <th style="border: 1px solid #ddd; padding: 12px; text-align: left;">Fix</th>
  </tr>
  <tr>
    <td style="border: 1px solid #ddd; padding: 12px;"><code>Wrong file name</code></td>
    <td style="border: 1px solid #ddd; padding: 12px;">File not named <code>submission.csv</code></td>
    <td style="border: 1px solid #ddd; padding: 12px;">Rename the file exactly</td>
  </tr>
  <tr style="background-color: #f9f9f9;">
    <td style="border: 1px solid #ddd; padding: 12px;"><code>Missing sequences</code></td>
    <td style="border: 1px solid #ddd; padding: 12px;">Not all sequences included</td>
    <td style="border: 1px solid #ddd; padding: 12px;">Check that sequence count matches the evaluation file</td>
  </tr>
  <tr>
    <td style="border: 1px solid #ddd; padding: 12px;"><code>Missing tokens</code></td>
    <td style="border: 1px solid #ddd; padding: 12px;">Gaps in <code>token_index</code> within a sequence</td>
    <td style="border: 1px solid #ddd; padding: 12px;">Include all positions from 0 to len(sequence)−1</td>
  </tr>
  <tr style="background-color: #f9f9f9;">
    <td style="border: 1px solid #ddd; padding: 12px;"><code>Invalid tag</code></td>
    <td style="border: 1px solid #ddd; padding: 12px;">Misspelled or unknown tag</td>
    <td style="border: 1px solid #ddd; padding: 12px;">Use only the 9 defined IOB2 tags</td>
  </tr>
  <tr>
    <td style="border: 1px solid #ddd; padding: 12px;"><code>Not zipped</code></td>
    <td style="border: 1px solid #ddd; padding: 12px;">Raw CSV uploaded</td>
    <td style="border: 1px solid #ddd; padding: 12px;">Wrap in a ZIP archive</td>
  </tr>
</table>

---

## Ranking

The public leaderboard displays all valid submissions ranked by **Macro F1-Score** in descending order. Higher scores indicate better performance. In case of tied scores, the earlier submission takes precedence.