# GastroCorp NER 2026: Gastronomic Named Entity Recognition in Spanish–English Texts

The gastronomic domain presents distinctive challenges for Natural Language Processing that general-purpose systems fail to address adequately. Terms such as *arepa de choclo*, *ají amarillo*, or *tacos al pastor* carry cultural identity and semantic specificity that demand precise entity recognition before any downstream task — including machine translation, recipe recommendation, or intelligent menu systems — can be performed reliably.

**GastroCorp NER 2026** is a shared task on Named Entity Recognition over a bilingual (Spanish–English) gastronomic corpus. Given a sequence of tokens from a restaurant menu item or a culinary recipe, participants must assign an IOB2 entity label to each token. The challenge covers real-world linguistic phenomena including code-switching between Spanish and English, brand names embedded in dish descriptions, culturally specific ingredient terminology, and the context-dependent nature of gastronomic entities (e.g., the same term may denote a *dish* in a menu context and an *ingredient* in a recipe context).

The task is organized as part of ongoing research on integrating Named Entity Recognition with Neural Machine Translation for gastronomic texts at Universidad Tecnológica de Bolívar (Cartagena, Colombia).

---

## Task Description

### Input

A sequence of whitespace-tokenized tokens from a gastronomic text (restaurant menu or culinary recipe), provided in HuggingFace NER JSONL format.

### Output

An IOB2 label for each token in the sequence, selecting from the following tag set:

<table style="border-collapse: collapse; width: 100%;">
  <tr style="background-color: #f2f2f2;">
    <th style="border: 1px solid #ddd; padding: 12px; text-align: left;">Tag</th>
    <th style="border: 1px solid #ddd; padding: 12px; text-align: left;">Entity type</th>
    <th style="border: 1px solid #ddd; padding: 12px; text-align: left;">Description</th>
  </tr>
  <tr>
    <td style="border: 1px solid #ddd; padding: 12px;"><code>O</code></td>
    <td style="border: 1px solid #ddd; padding: 12px;">—</td>
    <td style="border: 1px solid #ddd; padding: 12px;">Token does not belong to any named entity</td>
  </tr>
  <tr style="background-color: #f9f9f9;">
    <td style="border: 1px solid #ddd; padding: 12px;"><code>B-DISH</code></td>
    <td style="border: 1px solid #ddd; padding: 12px;">Dish</td>
    <td style="border: 1px solid #ddd; padding: 12px;">First token of a dish or prepared food item</td>
  </tr>
  <tr>
    <td style="border: 1px solid #ddd; padding: 12px;"><code>I-DISH</code></td>
    <td style="border: 1px solid #ddd; padding: 12px;">Dish</td>
    <td style="border: 1px solid #ddd; padding: 12px;">Continuation token of a dish entity</td>
  </tr>
  <tr style="background-color: #f9f9f9;">
    <td style="border: 1px solid #ddd; padding: 12px;"><code>B-BEVERAGE</code></td>
    <td style="border: 1px solid #ddd; padding: 12px;">Beverage</td>
    <td style="border: 1px solid #ddd; padding: 12px;">First token of a beverage listed as a final product</td>
  </tr>
  <tr>
    <td style="border: 1px solid #ddd; padding: 12px;"><code>I-BEVERAGE</code></td>
    <td style="border: 1px solid #ddd; padding: 12px;">Beverage</td>
    <td style="border: 1px solid #ddd; padding: 12px;">Continuation token of a beverage entity</td>
  </tr>
  <tr style="background-color: #f9f9f9;">
    <td style="border: 1px solid #ddd; padding: 12px;"><code>B-INGREDIENT</code></td>
    <td style="border: 1px solid #ddd; padding: 12px;">Ingredient</td>
    <td style="border: 1px solid #ddd; padding: 12px;">First token of an individual ingredient or component</td>
  </tr>
  <tr>
    <td style="border: 1px solid #ddd; padding: 12px;"><code>I-INGREDIENT</code></td>
    <td style="border: 1px solid #ddd; padding: 12px;">Ingredient</td>
    <td style="border: 1px solid #ddd; padding: 12px;">Continuation token of an ingredient entity</td>
  </tr>
  <tr style="background-color: #f9f9f9;">
    <td style="border: 1px solid #ddd; padding: 12px;"><code>B-BRAND</code></td>
    <td style="border: 1px solid #ddd; padding: 12px;">Brand</td>
    <td style="border: 1px solid #ddd; padding: 12px;">First token of a commercial or registered brand name</td>
  </tr>
  <tr>
    <td style="border: 1px solid #ddd; padding: 12px;"><code>I-BRAND</code></td>
    <td style="border: 1px solid #ddd; padding: 12px;">Brand</td>
    <td style="border: 1px solid #ddd; padding: 12px;">Continuation token of a brand entity</td>
  </tr>
</table>

### Sub-domains

The corpus covers two complementary text domains with distinct characteristics:

- **Menus** — restaurant menu items in Spanish and English, including dish names, beverages, and ingredient descriptions within dish entries. Entity boundaries follow item-level granularity.
- **Recipes** — ingredient lists and preparation steps, predominantly in English. Entities correspond to individual culinary components and commercial product names that appear in ingredient lines.

Participants may train a single model covering both sub-domains or develop specialized models per sub-domain.

### Illustrative Example

**Input tokens:** `Pizza` `Margarita` `con` `mozzarella` `fresca` `y` `Heineken`

**Expected output:**

<table style="border-collapse: collapse; width: 100%;">
  <tr style="background-color: #f2f2f2;">
    <th style="border: 1px solid #ddd; padding: 12px; text-align: left;">Token</th>
    <th style="border: 1px solid #ddd; padding: 12px; text-align: left;">Tag</th>
  </tr>
  <tr>
    <td style="border: 1px solid #ddd; padding: 12px;">Pizza</td>
    <td style="border: 1px solid #ddd; padding: 12px;"><code>B-DISH</code></td>
  </tr>
  <tr style="background-color: #f9f9f9;">
    <td style="border: 1px solid #ddd; padding: 12px;">Margarita</td>
    <td style="border: 1px solid #ddd; padding: 12px;"><code>I-DISH</code></td>
  </tr>
  <tr>
    <td style="border: 1px solid #ddd; padding: 12px;">con</td>
    <td style="border: 1px solid #ddd; padding: 12px;"><code>O</code></td>
  </tr>
  <tr style="background-color: #f9f9f9;">
    <td style="border: 1px solid #ddd; padding: 12px;">mozzarella</td>
    <td style="border: 1px solid #ddd; padding: 12px;"><code>B-INGREDIENT</code></td>
  </tr>
  <tr>
    <td style="border: 1px solid #ddd; padding: 12px;">fresca</td>
    <td style="border: 1px solid #ddd; padding: 12px;"><code>I-INGREDIENT</code></td>
  </tr>
  <tr style="background-color: #f9f9f9;">
    <td style="border: 1px solid #ddd; padding: 12px;">y</td>
    <td style="border: 1px solid #ddd; padding: 12px;"><code>O</code></td>
  </tr>
  <tr>
    <td style="border: 1px solid #ddd; padding: 12px;">Heineken</td>
    <td style="border: 1px solid #ddd; padding: 12px;"><code>B-BRAND</code></td>
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
    <td style="border: 1px solid #ddd; padding: 12px;">Task published</td>
    <td style="border: 1px solid #ddd; padding: 12px;">March 23, 2026</td>
  </tr>
  <tr style="background-color: #f9f9f9;">
    <td style="border: 1px solid #ddd; padding: 12px;">Challenge opens — submissions begin</td>
    <td style="border: 1px solid #ddd; padding: 12px;">April 5, 2026</td>
  </tr>
  <tr>
    <td style="border: 1px solid #ddd; padding: 12px;">Development phase closes</td>
    <td style="border: 1px solid #ddd; padding: 12px;">April 25, 2026</td>
  </tr>
  <tr style="background-color: #f9f9f9;">
    <td style="border: 1px solid #ddd; padding: 12px;">Evaluation phase opens (Test set)</td>
    <td style="border: 1px solid #ddd; padding: 12px;">April 26, 2026</td>
  </tr>
  <tr>
    <td style="border: 1px solid #ddd; padding: 12px;">Evaluation phase closes</td>
    <td style="border: 1px solid #ddd; padding: 12px;">April 30, 2026</td>
  </tr>
  <tr style="background-color: #f9f9f9;">
    <td style="border: 1px solid #ddd; padding: 12px;">Results announced</td>
    <td style="border: 1px solid #ddd; padding: 12px;">May 5, 2026</td>
  </tr>
  <tr>
    <td style="border: 1px solid #ddd; padding: 12px;">Paper/article submission deadline</td>
    <td style="border: 1px solid #ddd; padding: 12px;">Second week of May 2026</td>
  </tr>
</table>

> **Development phase:** Participants submit predictions on the development set. The leaderboard is public and updated in real time. Labels are withheld from participants.  
> **Evaluation phase:** Participants submit predictions on the held-out test set. This phase determines the final ranking. Participants may use any insights gained during the development phase.

---

## Quick Start

1. **Download** the dataset from [Zenodo](https://doi.org/10.5281/zenodo.19183413)

2. **Clone** the starter kit repository
```bash
# 2. Clone the starter kit repository
git clone https://github.com/nalef-initiative/GastroCorpNER
cd gastrocorp-ner-2026
```

3. **Install** dependencies
```bash
pip install -r requirements.txt
```
4. **Run** the majority-class baseline to verify your setup
```bash
python baselines/baseline_majority.py \
    --train data/menu_train.jsonl \
    --dev   data/menu_dev.jsonl \
    --out   predictions/menu_dev_baseline.csv
```

5. **Evaluate** locally before submitting
```bash
python evaluate.py \
    --gold data/menu_dev.jsonl \
    --pred predictions/menu_dev_baseline.csv
```

6. **Package and submit**
```bash
zip submission.zip submission.csv
```

---

## Paper Submission

Participants can submit a paper describing their system, resources, results, and analysis. Accepted papers will be included in the official NALEF proceedings.

- Use CEURART format: [Overleaf Template](https://www.overleaf.com/latex/templates/template-for-submissions-to-ceur-workshop-proceedings-ceur-ws-dot-org/wqyfdgftmcfw)
- Length: 5–8 pages
- Language: English

- Include copyright footnote:

```
Copyright © 2026 for this paper by its authors.
Use permitted under CC BY 4.0.
NALEF 2026, Cartagena, Colombia.
```

- No page numbers or headers allowed
- Full author names and affiliations required

- CEUR agreement: [Download PDF](https://ceur-ws.org/ceur-author-agreement-ccby-ntp.pdf?ver=2025-06-10)

---

## References

Peña Gnecco, D., Puertas, E., & Martinez-Santos, J. C. (2026). GastroCorp: A Bilingual Gastronomic NER Corpus (Spanish–English) [https://doi.org/10.5281/zenodo.19183413](https://doi.org/10.5281/zenodo.19183413)