# TakeMeter — Planning

## Community
- Chosen community: r/leagueoflegends
- Why this community: Active, text-heavy community with highly varied discourse quality. Members range from casual players making jokes to veterans citing patch history and game mechanics. The analysis vs. opinion distinction is meaningful and recognizable to regulars in this community.

## Label taxonomy (3 labels)

| Label    | Definition                                                                                      |
|----------|-------------------------------------------------------------------------------------------------|
| analysis | Makes a structured argument using specific, verifiable evidence — game mechanics, stats, patch history, or logical reasoning. |
| opinion  | States a position or preference with light reasoning but no verifiable evidence to support it.  |
| noise    | Jokes, memes, one-word reactions, or off-topic comments that contribute no substantive argument. |

## Concrete examples per label

### analysis
1. "Gold card cycled at a ratio of 6 blue, 3 red, 1 gold — so gold was rare, a jackpot reward. That's why it's the stun, not the red card."
2. "Second wind lost 3 HP per 10 and Dshield lost 5 HP per 8 seconds last patch. Small numbers but they compound in long lane matchups — top lane sustain is genuinely weaker now."

### opinion
1. "Red/blue = buffs, gold fits the gambler vibe way better than soccer ref logic."
2. "I don't think chests or orbs should have champion shards — I've been playing 13 years, I don't need more blue essence."

### noise
1. "lmfao"
2. "Nice try APA, but no"

## Edge cases & decision rules

### Edge case 1: Opinion with one piece of evidence
Post: "LeBron is overrated — his playoff win rate against top-seeded opponents is below .500."
Could be: analysis (cites a stat) or opinion (stat is cherry-picked for effect)
Decision rule: If the evidence is specific and verifiable AND forms the backbone of the argument → analysis. If the evidence is decorative — selected to sound credible but not genuinely reasoning — → opinion. One cherry-picked stat with accusatory framing = opinion.

### Edge case 2: Joke with a real point inside
Post: "Well in rugby a yellow card puts you in a temporary time out which is more close to a stun."
Could be: noise (casual tone) or analysis (makes a valid cross-game comparison)
Decision rule: If the core claim could stand alone as a reasonable argument even without the humor → label by the argument, not the tone. This one = analysis.

### Edge case 3: News post with added commentary
Post: "Zeyzal returns to Shopify Rebellion. Good move, he was wasted on that roster last split."
Could be: noise (just a link) or opinion (added commentary)
Decision rule: If the poster adds any evaluative claim beyond the factual news → opinion. Pure link drops with no commentary → noise.

## Data collection plan
- Source: r/leagueoflegends posts and comment threads
- How collected: Manual copy from Reddit — post titles, bodies, and individual comments
- Target: 200+ examples (aim for ~70 per label for balanced distribution)

## Label distribution target
| Label    | Target count | % of dataset |
|----------|-------------|--------------|
| analysis | ~70         | 35%          |
| opinion  | ~70         | 35%          |
| noise    | ~70         | 30%          |

## Label distribution (fill after annotation)
| Label    | Actual count | % of dataset |
|----------|-------------|--------------|
| analysis |             |              |
| opinion  |             |              |
| noise    |             |              |
