## Data

### Corpus overview

GastroCorp is a bilingual (Spanish–English) gastronomic corpus for Named Entity Recognition, constructed through collaborative human annotation at Universidad Tecnológica de Bolívar. The annotation was carried out by 71 trained university students over a 40-day period (October–December 2025) using Label Studio deployed on an institutional server.

| Statistic | Value |
|---|---|
| Total annotated sequences | 21,385 |
| Total clean entities | 86,320 |
| Entity types | 4: DISH, BEVERAGE, INGREDIENT, BRAND |
| Text domains | Restaurant menus · Culinary recipes |
| Languages | Spanish · English (bilingual, mixed) |
| Annotation period | October–December 2025 |
| Inter-annotator agreement (Cohen's κ) | 0.9031 — *Almost perfect* (Landis & Koch, 1977) |
| Pairwise F1 (Brandsen et al., 2020) | 0.9727 |
| Annotators | 71 university students |

### Download

The dataset is publicly available on Zenodo:

**https://doi.org/10.5281/zenodo.19183413**

Released under **Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)**.  
Academic and research use is permitted with proper attribution. Commercial use is not permitted.

### Dataset files

| File | Sequences | Description |
|---|---|---|
| `menu_train.jsonl` | 11,604 | Menu training set — tokens + full IOB2 labels + entity attributes |
| `menu_dev.jsonl` | 2,480 | Menu development set — tokens only (labels withheld) |
| `menu_test.jsonl` | 2,503 | Menu test set — tokens only (labels withheld) |
| `recipe_train.jsonl` | 3,358 | Recipe training set — tokens + full IOB2 labels + entity attributes |
| `recipe_dev.jsonl` | 719 | Recipe development set — tokens only (labels withheld) |
| `recipe_test.jsonl` | 721 | Recipe test set — tokens only (labels withheld) |

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

| Label | Description | Examples |
|---|---|---|
| `DISH` | Complete dish or prepared food item | *Lomo saltado*, *Grilled salmon with lemon butter* |
| `BEVERAGE` | Drink listed as a consumable product | *Mojito*, *Café americano*, *Vino tinto Malbec* |
| `INGREDIENT` | Individual component in descriptions or recipes | *mozzarella fresca*, *ají amarillo*, *olive oil* |
| `BRAND` | Commercial or registered brand name | *Coca-Cola*, *Heineken*, *Starbucks* |

**Important annotation properties participants should be aware of:**

- **Context-dependent labels.** The same term may bear different labels in different contexts. *Pollo al curry* is `DISH` as a menu item but `INGREDIENT` when mentioned in a recipe instruction or dish description. **Context is decisive.**

- **Multi-label entities.** The same text span can carry two simultaneous labels. *Coca-Cola* may appear as both `BRAND` and `BEVERAGE` in the same sequence, represented as two independent entity spans with different boundaries or offsets. Models should not assume one entity per span.

- **Bilingual mixing.** Menu texts frequently alternate between Spanish and English within the same sequence. Tokens are annotated in their original language without normalization.

- **Attribute propagation.** Within each training sequence, semantic attributes (cooking method, culinary origin, etc.) are propagated from the first occurrence of an entity surface form to subsequent occurrences. Downstream models may exploit these attributes as auxiliary features.

### Data sources and licensing

| Component | Source | License |
|---|---|---|
| Menu texts | CLUVI (Colombia) — under academic use agreement | Academic only, non-commercial |
| Recipe texts | RecipeNLG (Bień et al., 2020) | CC BY 4.0 |
| Recipe texts | HumbleIntelligence Food NER 1M (HuggingFace) | See source |
| Recipe texts | TASTEset (Wróblewska et al., 2021) | CC BY 4.0 |
| Annotations | Universidad Tecnológica de Bolívar, 2025 | CC BY-NC 4.0 |

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

| Model | HuggingFace identifier | Suitable for |
|---|---|---|
| mBERT | `bert-base-multilingual-cased` | Both sub-domains (bilingual) |
| BETO | `dccuchile/bert-base-spanish-wwm-cased` | Menus (predominantly Spanish) |
| XLM-RoBERTa | `xlm-roberta-base` | Both sub-domains (state of the art) |

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
