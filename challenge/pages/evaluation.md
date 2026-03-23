## Evaluation

### Primary metric: Span-level Micro-F1 (exact match)

The official ranking metric is **span-level micro-average F1 with exact boundary match**. A predicted entity span is counted as a True Positive if and only if both its boundaries and its entity type match the gold annotation exactly. Partial boundary overlaps are not credited.

For each entity type $c$:

$$F_1(c) = \frac{2 \cdot \text{TP}_c}{2 \cdot \text{TP}_c + \text{FP}_c + \text{FN}_c}$$

The final score micro-averages across all entity types:

$$\text{Micro-F1} = \frac{2 \cdot \sum_c \text{TP}_c}{2 \cdot \sum_c \text{TP}_c + \sum_c \text{FP}_c + \sum_c \text{FN}_c}$$

**Rationale for exact match.** In downstream applications such as machine translation augmentation, a partially recognized entity (e.g., identifying only *Pizza* from *Pizza Margarita*) is effectively unusable. Exact boundary recovery is therefore the operationally meaningful criterion.

### Secondary metrics (reported, not used for ranking)

| Metric | Description |
|---|---|
| Macro-F1 | F1 averaged equally across all 4 entity types; highlights performance on low-frequency entities (BRAND, BEVERAGE) |
| Per-entity F1 | Individual F1 for each of DISH, BEVERAGE, INGREDIENT, BRAND |
| Micro-F1 per sub-domain | Separate scores for the menus and recipes sub-domains |

### Baseline results (majority-class)

The following scores provide a lower-bound reference obtained with the majority-class baseline included in the starter kit:

| Sub-domain | Micro-F1 |
|---|---|
| Menus | *to be reported* |
| Recipes | *to be reported* |

> Baseline results will be published on the leaderboard at challenge opening.

### Ranking

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

| Column | Type | Description |
|---|---|---|
| `sequence_id` | string | Sequence identifier matching the `id` field in the dataset |
| `token_index` | integer | Zero-based position of the token within the sequence |
| `predicted_tag` | string | Predicted IOB2 tag |

### Requirements

- The submission must include predictions for **every token** in **every sequence** of the evaluation set
- All nine valid tags must be spelled exactly as shown (case-sensitive)
- Sequences must be submitted in any order; token indices within each sequence must be complete and contiguous starting from 0
- The archive must contain exactly one file named `submission.csv`

### Common errors

| Error | Cause | Fix |
|---|---|---|
| `Wrong file name` | File not named `submission.csv` | Rename the file exactly |
| `Missing sequences` | Not all sequences included | Check that sequence count matches the evaluation file |
| `Missing tokens` | Gaps in `token_index` within a sequence | Include all positions from 0 to len(sequence)−1 |
| `Invalid tag` | Misspelled or unknown tag | Use only the 9 defined IOB2 tags |
| `Not zipped` | Raw CSV uploaded | Wrap in a ZIP archive |
