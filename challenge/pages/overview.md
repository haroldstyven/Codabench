# GastroCorp NER 2026: Gastronomic Named Entity Recognition in Spanish–English Texts

**Organized by:** Daniel Arturo Peña Gnecco · Universidad Tecnológica de Bolívar  
**Docker image:** `codalab/codalab-legacy:py312`

---

## Overview

The gastronomic domain presents distinctive challenges for Natural Language Processing that general-purpose systems fail to address adequately. Terms such as *arepa de choclo*, *ají amarillo*, or *tacos al pastor* carry cultural identity and semantic specificity that demand precise entity recognition before any downstream task — including machine translation, recipe recommendation, or intelligent menu systems — can be performed reliably.

**GastroCorp NER 2026** is a shared task on Named Entity Recognition over a bilingual (Spanish–English) gastronomic corpus. Given a sequence of tokens from a restaurant menu item or a culinary recipe, participants must assign an IOB2 entity label to each token. The challenge covers real-world linguistic phenomena including code-switching between Spanish and English, brand names embedded in dish descriptions, culturally specific ingredient terminology, and the context-dependent nature of gastronomic entities (e.g., the same term may denote a *dish* in a menu context and an *ingredient* in a recipe context).

The task is organized as part of ongoing research on integrating Named Entity Recognition with Neural Machine Translation for gastronomic texts at Universidad Tecnológica de Bolívar (Cartagena, Colombia).

---

## Task Description

### Input

A sequence of whitespace-tokenized tokens from a gastronomic text (restaurant menu or culinary recipe), provided in HuggingFace NER JSONL format.

### Output

An IOB2 label for each token in the sequence, selecting from the following tag set:

| Tag | Entity type | Description |
|---|---|---|
| `O` | — | Token does not belong to any named entity |
| `B-DISH` | Dish | First token of a dish or prepared food item |
| `I-DISH` | Dish | Continuation token of a dish entity |
| `B-BEVERAGE` | Beverage | First token of a beverage listed as a final product |
| `I-BEVERAGE` | Beverage | Continuation token of a beverage entity |
| `B-INGREDIENT` | Ingredient | First token of an individual ingredient or component |
| `I-INGREDIENT` | Ingredient | Continuation token of an ingredient entity |
| `B-BRAND` | Brand | First token of a commercial or registered brand name |
| `I-BRAND` | Brand | Continuation token of a brand entity |

### Sub-domains

The corpus covers two complementary text domains with distinct characteristics:

- **Menus** — restaurant menu items in Spanish and English, including dish names, beverages, and ingredient descriptions within dish entries. Entity boundaries follow item-level granularity.
- **Recipes** — ingredient lists and preparation steps, predominantly in English. Entities correspond to individual culinary components and commercial product names that appear in ingredient lines.

Participants may train a single model covering both sub-domains or develop specialized models per sub-domain.

### Illustrative Example

**Input tokens:** `Pizza` `Margarita` `con` `mozzarella` `fresca` `y` `Heineken`

**Expected output:**

| Token | Tag |
|---|---|
| Pizza | `B-DISH` |
| Margarita | `I-DISH` |
| con | `O` |
| mozzarella | `B-INGREDIENT` |
| fresca | `I-INGREDIENT` |
| y | `O` |
| Heineken | `B-BRAND` |

---

## Timeline

| Event | Date |
|---|---|
| Task published | March 23, 2026 |
| Challenge opens — submissions begin | April 5, 2026 |
| Development phase closes | April 25, 2026 |
| Evaluation phase opens (Test set) | April 26, 2026 |
| Evaluation phase closes | April 30, 2026 |
| Results announced | May 5, 2026 |
| Paper/article submission deadline | Second week of May 2026 |

> **Development phase:** Participants submit predictions on the development set. The leaderboard is public and updated in real time. Labels are withheld from participants.  
> **Evaluation phase:** Participants submit predictions on the held-out test set. This phase determines the final ranking. Participants may use any insights gained during the development phase.

---

## Quick Start

```bash
# 1. Download the dataset
#    https://doi.org/10.5281/zenodo.19183413

# 2. Clone the starter kit repository
git clone https://github.com/nalef-initiative/GastroCorpNER
cd gastrocorp-ner-2026

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the majority-class baseline to verify your setup
python baselines/baseline_majority.py \
    --train data/menu_train.jsonl \
    --dev   data/menu_dev.jsonl \
    --out   predictions/menu_dev_baseline.csv

# 5. Evaluate locally before submitting
python evaluate.py \
    --gold data/menu_dev.jsonl \
    --pred predictions/menu_dev_baseline.csv

# 6. Package and submit
zip submission.zip submission.csv
```
