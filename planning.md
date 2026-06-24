## Evaluation Metrics

Accuracy alone is insufficient for this task for two reasons. First, with
three labels, a model that predicts the majority class every time would still
achieve ~36% accuracy — accuracy doesn't reveal whether the model learned all
three distinctions. Second, the labels are not equally important: a classifier
that learns analysis and opinion but completely ignores noise is useless for
the intended purpose of sorting community discourse.

The right metrics are:

- **Per-class F1** for each label — catches cases where one class is never
  predicted (F1 = 0) even when overall accuracy looks acceptable
- **Confusion matrix** — reveals which specific label pairs are being confused
  and in which direction, which is more actionable than a single accuracy number
- **Overall accuracy** — useful for comparison against baseline but never
  interpreted in isolation

## Definition of Success

A classifier that would be genuinely useful in a real r/leagueoflegends
community tool needs:

- Overall accuracy ≥ 0.70
- Per-class F1 ≥ 0.60 for all three labels (no label left at zero)

The zero-shot Groq baseline achieved 0.733 overall but noise F1 of 0.62 —
barely clearing the bar. The fine-tuned DistilBERT at 0.400 overall and
noise F1 of 0.00 does not meet the threshold and would not be deployed.

A key insight from the results: 200 examples was insufficient for fine-tuning
to beat a strong zero-shot baseline on this task. The noise class in particular
(40 training examples, highly varied short-form text) was never learned by the
fine-tuned model.

## AI Tool Plan

### Label stress-testing

Claude was used to generate boundary examples between analysis and opinion
during taxonomy design. Posts that cited one specific stat with accusatory
framing (e.g. cherry-picked winrate data) were used to sharpen the decision
rule: if evidence forms the backbone of the argument it is analysis; if it
is decorative it is opinion.

### Annotation assistance

No LLM pre-labeling was used. All 200 examples were labeled manually using
the decision rules in the taxonomy section above. Claude was used as a
collaborative labeling partner during collection sessions — posts were
discussed and labeled together, with final label decisions made by the
annotator. This is disclosed here per the AI usage policy.

### Failure analysis

After fine-tuning, wrong predictions were reviewed with Claude to identify
systematic patterns. Key finding: the model confused analysis and opinion in
both directions for posts with specific but opinonated framing, and failed
to learn noise entirely — predicting it zero times on the test set. This
pattern was verified by manually re-reading all 18 wrong predictions.
