# Data

### Corpus overview

GastroCorp is a bilingual (Spanish–English) gastronomic corpus for Named Entity Recognition, constructed through collaborative human annotation at Universidad Tecnológica de Bolívar. The annotation was carried out by 71 trained university students over a 40-day period (October–December 2025) using Label Studio deployed on an institutional server.

<table style="border-collapse: collapse; width: 100%;">
  <tr style="background-color: #f2f2f2;">
    <th style="border: 1px solid #ddd; padding: 12px; text-align: left;">Statistic</th>
    <th style="border: 1px solid #ddd; padding: 12px; text-align: left;">Value</th>
  </tr>
  <tr>
    <td style="border: 1px solid #ddd; padding: 12px;">Total annotated sequences</td>
    <td style="border: 1px solid #ddd; padding: 12px;">21,385</td>
  </tr>
  <tr style="background-color: #f9f9f9;">
    <td style="border: 1px solid #ddd; padding: 12px;">Total clean entities</td>
    <td style="border: 1px solid #ddd; padding: 12px;">86,320</td>
  </tr>
  <tr>
    <td style="border: 1px solid #ddd; padding: 12px;">Entity types</td>
    <td style="border: 1px solid #ddd; padding: 12px;">4: DISH, BEVERAGE, INGREDIENT, BRAND</td>
  </tr>
  <tr style="background-color: #f9f9f9;">
    <td style="border: 1px solid #ddd; padding: 12px;">Text domains</td>
    <td style="border: 1px solid #ddd; padding: 12px;">Restaurant menus · Culinary recipes</td>
  </tr>
  <tr>
    <td style="border: 1px solid #ddd; padding: 12px;">Languages</td>
    <td style="border: 1px solid #ddd; padding: 12px;">Spanish · English (bilingual, mixed)</td>
  </tr>
  <tr style="background-color: #f9f9f9;">
    <td style="border: 1px solid #ddd; padding: 12px;">Annotation period</td>
    <td style="border: 1px solid #ddd; padding: 12px;">October–December 2025</td>
  </tr>
  <tr>
    <td style="border: 1px solid #ddd; padding: 12px;">Inter-annotator agreement (Cohen's κ)</td>
    <td style="border: 1px solid #ddd; padding: 12px;">0.9031 — <em>Almost perfect</em> (Landis & Koch, 1977)</td>
  </tr>
  <tr style="background-color: #f9f9f9;">
    <td style="border: 1px solid #ddd; padding: 12px;">Pairwise F1 (Brandsen et al., 2020)</td>
    <td style="border: 1px solid #ddd; padding: 12px;">0.9727</td>
  </tr>
  <tr>
    <td style="border: 1px solid #ddd; padding: 12px;">Annotators</td>
    <td style="border: 1px solid #ddd; padding: 12px;">71 university students</td>
  </tr>
</table>

### Download

The dataset is publicly available on Zenodo:

**https://doi.org/10.5281/zenodo.19183413**

Released under **Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)**.  
Academic and research use is permitted with proper attribution. Commercial use is not permitted.

### Dataset files

<table style="border-collapse: collapse; width: 100%;">
  <tr style="background-color: #f2f2f2;">
    <th style="border: 1px solid #ddd; padding: 12px; text-align: left;">File</th>
    <th style="border: 1px solid #ddd; padding: 12px; text-align: left;">Sequences</th>
    <th style="border: 1px solid #ddd; padding: 12px; text-align: left;">Description</th>
  </tr>
  <tr>
    <td style="border: 1px solid #ddd; padding: 12px;"><code>menu_train.jsonl</code></td>
    <td style="border: 1px solid #ddd; padding: 12px;">11,604</td>
    <td style="border: 1px solid #ddd; padding: 12px;">Menu training set — tokens + full IOB2 labels + entity attributes</td>
  </tr>
  <tr style="background-color: #f9f9f9;">
    <td style="border: 1px solid #ddd; padding: 12px;"><code>menu_dev.jsonl</code></td>
    <td style="border: 1px solid #ddd; padding: 12px;">2,480</td>
    <td style="border: 1px solid #ddd; padding: 12px;">Menu development set — tokens only (labels withheld)</td>
  </tr>
  <tr>
    <td style="border: 1px solid #ddd; padding: 12px;"><code>menu_test.jsonl</code></td>
    <td style="border: 1px solid #ddd; padding: 12px;">2,503</td>
    <td style="border: 1px solid #ddd; padding: 12px;">Menu test set — tokens only (labels withheld)</td>
  </tr>
  <tr style="background-color: #f9f9f9;">
    <td style="border: 1px solid #ddd; padding: 12px;"><code>recipe_train.jsonl</code></td>
    <td style="border: 1px solid #ddd; padding: 12px;">3,358</td>
    <td style="border: 1px solid #ddd; padding: 12px;">Recipe training set — tokens + full IOB2 labels + entity attributes</td>
  </tr>
  <tr>
    <td style="border: 1px solid #ddd; padding: 12px;"><code>recipe_dev.jsonl</code></td>
    <td style="border: 1px solid #ddd; padding: 12px;">719</td>
    <td style="border: 1px solid #ddd; padding: 12px;">Recipe development set — tokens only (labels withheld)</td>
  </tr>
  <tr style="background-color: #f9f9f9;">
    <td style="border: 1px solid #ddd; padding: 12px;"><code>recipe_test.jsonl</code></td>
    <td style="border: 1px solid #ddd; padding: 12px;">721</td>
    <td style="border: 1px solid #ddd; padding: 12px;">Recipe test set — tokens only (labels withheld)</td>
  </tr>
</table>

### Dataset format

Each `.jsonl` file follows the HuggingFace NER format. Every line is a self-contained JSON object:

**Training and development gold files** (available to organizers and released post-challenge):

```json
{
  "id": "menu_000001",
  "tokens": ["Pizza", "Margarita", "con", "mozzarella", "fresca"],
  "ner_tags": ["B-DISH", "I-DISH", "O", "B-INGREDIENT", "I-INGREDIENT"],
  "entities": [
    {
      "text": "Pizza Margarita",
      "label": "DISH",
      "token_start": 0,
      "token_end": 1,
      "course_type": "main_course"
    },
    {
      "text": "mozzarella fresca",
      "label": "INGREDIENT",
      "token_start": 3,
      "token_end": 4,
      "preparation_state": "fresh",
      "origin_cuisine": "Italian",
      "ingredient_language": "Spanish"
    }
  ],
  "meta_language": "Spanish"
}
```

**Participant files** (dev and test — labels withheld):

```json
{
  "id": "menu_000001",
  "tokens": ["Pizza", "Margarita", "con", "mozzarella", "fresca"]
}
```

### Loading the data

```python
import json

def load_sequences(path):
    with open(path, encoding="utf-8") as f:
        return [json.loads(line) for line in f]

train = load_sequences("menu_train.jsonl")
dev   = load_sequences("menu_dev.jsonl")

# Example: access tokens and labels
seq = train[0]
print(seq["tokens"])    # ["Pizza", "Margarita", ...]
print(seq["ner_tags"])  # ["B-DISH", "I-DISH", ...]
```

Or using the HuggingFace `datasets` library:

```python
from datasets import load_dataset

ds = load_dataset("json", data_files={
    "train": "menu_train.jsonl",
    "dev":   "menu_dev.jsonl",
})
```

### Entity types and annotation notes

<table style="border-collapse: collapse; width: 100%;">
  <tr style="background-color: #f2f2f2;">
    <th style="border: 1px solid #ddd; padding: 12px; text-align: left;">Label</th>
    <th style="border: 1px solid #ddd; padding: 12px; text-align: left;">Description</th>
    <th style="border: 1px solid #ddd; padding: 12px; text-align: left;">Examples</th>
  </tr>
  <tr>
    <td style="border: 1px solid #ddd; padding: 12px;"><code>DISH</code></td>
    <td style="border: 1px solid #ddd; padding: 12px;">Complete dish or prepared food item</td>
    <td style="border: 1px solid #ddd; padding: 12px;"><em>Lomo saltado</em>, <em>Grilled salmon with lemon butter</em></td>
  </tr>
  <tr style="background-color: #f9f9f9;">
    <td style="border: 1px solid #ddd; padding: 12px;"><code>BEVERAGE</code></td>
    <td style="border: 1px solid #ddd; padding: 12px;">Drink listed as a consumable product</td>
    <td style="border: 1px solid #ddd; padding: 12px;"><em>Mojito</em>, <em>Café americano</em>, <em>Vino tinto Malbec</em></td>
  </tr>
  <tr>
    <td style="border: 1px solid #ddd; padding: 12px;"><code>INGREDIENT</code></td>
    <td style="border: 1px solid #ddd; padding: 12px;">Individual component in descriptions or recipes</td>
    <td style="border: 1px solid #ddd; padding: 12px;"><em>mozzarella fresca</em>, <em>ají amarillo</em>, <em>olive oil</em></td>
  </tr>
  <tr style="background-color: #f9f9f9;">
    <td style="border: 1px solid #ddd; padding: 12px;"><code>BRAND</code></td>
    <td style="border: 1px solid #ddd; padding: 12px;">Commercial or registered brand name</td>
    <td style="border: 1px solid #ddd; padding: 12px;"><em>Coca-Cola</em>, <em>Heineken</em>, <em>Starbucks</em></td>
  </tr>
</table>


**Important annotation properties participants should be aware of:**

- **Context-dependent labels.** The same term may bear different labels in different contexts. *Pollo al curry* is `DISH` as a menu item but `INGREDIENT` when mentioned in a recipe instruction or dish description. **Context is decisive.**

- **Multi-label entities.** The same text span can carry two simultaneous labels. *Coca-Cola* may appear as both `BRAND` and `BEVERAGE` in the same sequence, represented as two independent entity spans with different boundaries or offsets. Models should not assume one entity per span.

- **Bilingual mixing.** Menu texts frequently alternate between Spanish and English within the same sequence. Tokens are annotated in their original language without normalization.

- **Attribute propagation.** Within each training sequence, semantic attributes (cooking method, culinary origin, etc.) are propagated from the first occurrence of an entity surface form to subsequent occurrences. Downstream models may exploit these attributes as auxiliary features.

### Data sources and licensing

<table style="border-collapse: collapse; width: 100%;">
  <tr style="background-color: #f2f2f2;">
    <th style="border: 1px solid #ddd; padding: 12px; text-align: left;">Component</th>
    <th style="border: 1px solid #ddd; padding: 12px; text-align: left;">Source</th>
    <th style="border: 1px solid #ddd; padding: 12px; text-align: left;">License</th>
  </tr>
  <tr>
    <td style="border: 1px solid #ddd; padding: 12px;">Menu texts</td>
    <td style="border: 1px solid #ddd; padding: 12px;">CLUVI (Colombia) — under academic use agreement</td>
    <td style="border: 1px solid #ddd; padding: 12px;">Academic only, non-commercial</td>
  </tr>
  <tr style="background-color: #f9f9f9;">
    <td style="border: 1px solid #ddd; padding: 12px;">Recipe texts</td>
    <td style="border: 1px solid #ddd; padding: 12px;">RecipeNLG (Bień et al., 2020)</td>
    <td style="border: 1px solid #ddd; padding: 12px;">CC BY 4.0</td>
  </tr>
  <tr>
    <td style="border: 1px solid #ddd; padding: 12px;">Recipe texts</td>
    <td style="border: 1px solid #ddd; padding: 12px;">HumbleIntelligence Food NER 1M (HuggingFace)</td>
    <td style="border: 1px solid #ddd; padding: 12px;">See source</td>
  </tr>
  <tr style="background-color: #f9f9f9;">
    <td style="border: 1px solid #ddd; padding: 12px;">Recipe texts</td>
    <td style="border: 1px solid #ddd; padding: 12px;">TASTEset (Wróblewska et al., 2021)</td>
    <td style="border: 1px solid #ddd; padding: 12px;">CC BY 4.0</td>
  </tr>
  <tr>
    <td style="border: 1px solid #ddd; padding: 12px;">Annotations</td>
    <td style="border: 1px solid #ddd; padding: 12px;">Universidad Tecnológica de Bolívar, 2025</td>
    <td style="border: 1px solid #ddd; padding: 12px;">CC BY-NC 4.0</td>
  </tr>
</table>


The full dataset is distributed under **CC BY-NC 4.0**. The non-commercial restriction derives from the menu data component and applies to the entire released dataset.

---

## Starter Kit and Baselines

A starter kit repository is available at:

**https://github.com/nalef-initiative/GastroCorpNER**

### Repository contents

```
gastrocorp-ner-2026/
├── baselines/
│   ├── baseline_majority.py      # Majority-class baseline
│   └── baseline_transformer.py  # Fine-tuning starter (mBERT / BETO)
├── evaluate.py                   # Local evaluation script
├── requirements.txt
└── README.md
```

### Majority-class baseline

Assigns to each token the most frequent IOB2 tag observed for that token surface form in the training set. Unknown tokens receive `O`.

```bash
python baselines/baseline_majority.py \
    --train menu_train.jsonl \
    --dev   menu_dev.jsonl \
    --out   predictions/baseline_dev.csv
```

### Transformer baseline

Fine-tunes a multilingual pre-trained model on the training split. Recommended models:

<table style="border-collapse: collapse; width: 100%;">
  <tr style="background-color: #f2f2f2;">
    <th style="border: 1px solid #ddd; padding: 12px; text-align: left;">Model</th>
    <th style="border: 1px solid #ddd; padding: 12px; text-align: left;">HuggingFace identifier</th>
    <th style="border: 1px solid #ddd; padding: 12px; text-align: left;">Suitable for</th>
  </tr>
  <tr>
    <td style="border: 1px solid #ddd; padding: 12px;">mBERT</td>
    <td style="border: 1px solid #ddd; padding: 12px;"><code>bert-base-multilingual-cased</code></td>
    <td style="border: 1px solid #ddd; padding: 12px;">Both sub-domains (bilingual)</td>
  </tr>
  <tr style="background-color: #f9f9f9;">
    <td style="border: 1px solid #ddd; padding: 12px;">BETO</td>
    <td style="border: 1px solid #ddd; padding: 12px;"><code>dccuchile/bert-base-spanish-wwm-cased</code></td>
    <td style="border: 1px solid #ddd; padding: 12px;">Menus (predominantly Spanish)</td>
  </tr>
  <tr>
    <td style="border: 1px solid #ddd; padding: 12px;">XLM-RoBERTa</td>
    <td style="border: 1px solid #ddd; padding: 12px;"><code>xlm-roberta-base</code></td>
    <td style="border: 1px solid #ddd; padding: 12px;">Both sub-domains (state of the art)</td>
  </tr>
</table>

```bash
python baselines/baseline_transformer.py \
    --model  bert-base-multilingual-cased \
    --train  menu_train.jsonl \
    --dev    menu_dev.jsonl \
    --output predictions/
```

### Local evaluation

Participants are strongly encouraged to evaluate predictions locally before uploading:

```bash
python evaluate.py \
    --gold menu_train.jsonl \
    --pred predictions/my_predictions.csv
```

Output:

```
Label                P        R       F1    Support
DISH            0.8912   0.8734   0.8822       2562
BEVERAGE        0.9134   0.9056   0.9094       2666
INGREDIENT      0.8678   0.8521   0.8599       7733
BRAND           0.7823   0.7641   0.7731        487
----------------------------------------------------------
MICRO-AVG       0.8756   0.8612   0.8683      13448
```
