# TakeMeter

A fine-tuned text classifier for evaluating discourse quality in r/leagueoflegends.
Built for AI201 Project 3.

---

## Community Choice

**Community:** r/leagueoflegends

r/leagueoflegends is one of the most active gaming subreddits with over 6 million
members. The community produces highly varied discourse — from detailed patch
analysis citing specific game mechanics, to short emotional reactions, to joke
comments with zero informational content. This variance makes it a strong fit for
a classification task: the distinctions between labels are meaningful to community
members and observable in the text itself.

---

## Label Taxonomy

| Label      | Definition                                                                                                                    |
| ---------- | ----------------------------------------------------------------------------------------------------------------------------- |
| `analysis` | Makes a structured argument using specific, verifiable evidence — game mechanics, stats, patch history, or logical reasoning. |
| `opinion`  | States a position or preference with light reasoning but no verifiable evidence to support it.                                |
| `noise`    | Jokes, memes, one-word reactions, or off-topic comments that contribute no substantive argument.                              |

### Examples per label

**analysis**

1. "Gold card cycled at a ratio of 6 blue, 3 red, 1 gold so gold was rare, a jackpot reward. That is why it is the stun."
2. "Second wind lost 3 HP per 10 and Dshield lost 5 HP per 8 seconds last patch. Small numbers but they compound in long matchups."

**opinion**

1. "Red and blue equal buffs, gold fits the gambler vibe way better than soccer ref logic."
2. "I dont think chests should have champion shards. Been playing 13 years I dont need more blue essence."

**noise**

1. "lmfao"
2. "Nice try APA but no"

---

## Data Collection

**Source:** r/leagueoflegends posts and comment threads, collected manually via Reddit.

**Labeling process:** All 200 examples were labeled manually using the decision
rules defined in planning.md. Claude was used as a collaborative labeling partner
during collection sessions — posts were discussed and labeled together, with final
label decisions made by the annotator.

**Label distribution:**

| Label    | Count | % of dataset |
| -------- | ----- | ------------ |
| analysis | 72    | 36%          |
| opinion  | 71    | 35.5%        |
| noise    | 57    | 28.5%        |

### Difficult-to-label examples

**1. Opinion with one piece of evidence**

> "47% wr — they are lost and have 0 idea how to play."

Could be analysis (cites a stat) or opinion (stat used as a punchline).
Decision: `opinion` — the stat is decorative, not the backbone of an argument.

**2. Joke with a real point inside**

> "Well in rugby a yellow card puts you in a temporary time out which is more close to a stun."

Could be noise (casual tone) or analysis (makes a valid cross-game comparison).
Decision: `analysis` — the core claim stands on its own as a reasonable argument
even without the humorous framing.

**3. News post with added commentary**

> "Zeyzal returns to Shopify Rebellion. Good move, he was wasted on that roster last split."

Could be noise (just a link) or opinion (added evaluative commentary).
Decision: `opinion` — any evaluative claim beyond the factual news = opinion.

---

## Fine-Tuning Approach

**Base model:** `distilbert-base-uncased` (HuggingFace)

**Training setup:**

- Framework: HuggingFace `transformers` + `Trainer` API
- Platform: Google Colab (T4 GPU)
- Train/val/test split: 70% / 15% / 15% (stratified)
- Training examples: 140

**Hyperparameter decisions:**

| Parameter                   | Value | Reasoning                                                           |
| --------------------------- | ----- | ------------------------------------------------------------------- |
| num_train_epochs            | 3     | Standard for small datasets; more risks overfitting on 200 examples |
| learning_rate               | 2e-5  | Standard starting point for fine-tuning BERT-family models          |
| per_device_train_batch_size | 16    | Fits T4 GPU comfortably                                             |
| weight_decay                | 0.01  | Light regularization to reduce overfitting                          |

---

## Baseline Description

**Model:** Groq `llama-3.3-70b-versatile` (zero-shot)

**Prompt used:**

```
You are classifying comments and posts from r/leagueoflegends.

Assign each post to exactly one of the following categories.

analysis: Makes a structured argument using specific, verifiable evidence.
Example: "Gold card cycled at a ratio of 6 blue, 3 red, 1 gold so gold was rare."

opinion: States a position or preference with light reasoning but no verifiable evidence.
Example: "Red and blue equal buffs, gold fits the gambler vibe way better."

noise: Jokes, memes, one-word reactions, or off-topic comments.
Example: "lmfao"

Respond with ONLY the label name. Do not explain your reasoning.

Valid labels:
analysis
opinion
noise
```

All 30 test examples were parseable (0 unparseable responses).
