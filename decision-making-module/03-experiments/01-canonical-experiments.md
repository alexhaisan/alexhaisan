# 01 — Canonical Experiments (quick-reference)

> The brief permits *"a theory **or experiment** which we have studied on this module."*
> An experiment can be the stronger choice: it is concrete, memorable, and easier to
> describe crisply in a 300-word limit than an abstract model.
>
> ⚠️ Confirm which of these were actually covered before using one.

---

## 1. Allais Paradox (1953) — violates Independence

**Setup.** Choose between:
- **A:** £1m with certainty
- **B:** 89% £1m, 10% £5m, 1% £0

Then choose between:
- **C:** 11% £1m, 89% £0
- **D:** 10% £5m, 90% £0

**Result.** Most choose **A** then **D**. These are jointly inconsistent with EUT: the
second pair is the first pair with a common 89% chance of £1m removed from both. Independence
says removing a common component cannot flip the ranking.

**Why it matters.** The **certainty effect** — a 100% chance is valued disproportionately
over a 99% chance. Direct ancestor of prospect theory's probability weighting function.

**Use if:** your decision involved paying a premium for certainty / eliminating a small risk
entirely rather than reducing a large one.

---

## 2. Ellsberg Paradox (1961) — violates Subjective EU

**Setup.** An urn holds 30 red balls and 60 balls that are black or yellow in unknown
proportion.
- Bet A: £100 if red | Bet B: £100 if black
- Bet C: £100 if red or yellow | Bet D: £100 if black or yellow

**Result.** Most prefer **A over B** *and* **D over C**. These cannot both hold under any
coherent probability assignment — preferring A implies you think red > black; preferring D
implies the reverse.

**Why it matters.** **Ambiguity aversion** — people dislike *unknown* odds over and above
disliking risk. Known unknowns are preferred to unknown unknowns.

**Use if:** you chose a worse-but-well-understood option over a better-but-uncertain one.

---

## 3. Asian Disease Problem (Tversky & Kahneman, 1981) — violates Invariance

**Setup.** 600 people are expected to die from a disease outbreak.

*Gain frame:*
- A: 200 people will be saved → **72% choose**
- B: ⅓ chance 600 saved, ⅔ chance none saved → 28%

*Loss frame:*
- C: 400 people will die → 22%
- D: ⅓ chance nobody dies, ⅔ chance 600 die → **78% choose**

**Result.** A ≡ C and B ≡ D in every respect that matters. **Pure wording reverses the
majority preference.** Risk averse over gains, risk seeking over losses — the reflection
effect, in a single study.

**Why it matters.** The cleanest framing violation in the literature. Highly citable.

**Use if:** the presentation or wording of your options influenced you.

---

## 4. Wheel of Fortune / Anchoring (Tversky & Kahneman, 1974)

**Setup.** Spin a rigged wheel landing on 10 or 65. Ask: is the percentage of African nations
in the UN higher or lower than that number? Then: what is it?

**Result.** Median estimates **25%** (anchor 10) vs **45%** (anchor 65).

**Why it matters.** A **transparently random** number moved judgements substantially.
Extended by Ariely, Loewenstein & Prelec (2003) — social security digits anchored
willingness-to-pay for wine and chocolates ("coherent arbitrariness").

**Use if:** a list price, first offer, or arbitrary figure shaped your valuation.

---

## 5. Linda / Conjunction Fallacy (Tversky & Kahneman, 1983)

**Setup.** Linda is 31, single, outspoken, a philosophy graduate concerned with
discrimination and social justice. Which is more probable?
- (a) Linda is a bank teller
- (b) Linda is a bank teller and active in the feminist movement

**Result.** ~85% choose (b) — which is **logically impossible**, since (b) is a subset of (a).

**Why it matters.** Judgement runs on **similarity to a stereotype**, not probability theory.
Survives when participants are statistically trained.

**Use if:** you judged likelihood by "fit" rather than frequency.

---

## 6. Mugs / Endowment Effect (Kahneman, Knetsch & Thaler, 1990)

**Setup.** Randomly give half the participants a mug. Open a market between owners and
non-owners.

**Result.** Median **WTA ≈ $7.12**, median **WTP ≈ $2.87** — roughly a **2:1 gap**. Trading
volume was about half the level the Coase theorem predicts.

**Why it matters.** Ownership, assigned *at random seconds earlier*, changed valuation.
Preferences are reference-dependent, not fixed over final states. Also an empirical limit
on the Coase theorem.

**Use if:** you overvalued something you owned, or wouldn't give up something you'd never
have bought at that price.

---

## 7. Ultimatum Game (Güth, Schmittberger & Schwarze, 1982)

**Setup.** Proposer splits a sum; responder accepts or rejects. Rejection ⇒ both get nothing.

**Result.** Modal offers 40–50%; offers below ~20% rejected about half the time.
Robust cross-culturally, though magnitudes vary (Henrich et al., 2001).

**Why it matters.** Rejection is **costly punishment** — paying real money to deny an unfair
gain. Pure payoff maximisation predicts accepting anything positive.

**Use if:** you turned down a materially favourable option on fairness grounds.

---

## 8. Sunk Cost / Theatre Season Tickets (Arkes & Blumer, 1985)

**Setup.** Season ticket buyers randomly assigned full price, $2 discount, or $7 discount.

**Result.** Full-price buyers attended **significantly more** performances in the first half
of the season. Future benefit was identical; only the sunk amount differed.

**Why it matters.** Unrecoverable past expenditure drove forward-looking behaviour — a
direct violation of consequentialism.

**Use if:** you continued something because of what you'd already spent.

---

## 9. Jam Study / Choice Overload (Iyengar & Lepper, 2000)

**Setup.** A supermarket tasting booth displayed either 6 or 24 varieties of jam.

**Result.** 24 varieties drew more **attention** (60% vs 40% stopped) but far fewer
**purchases** — about **3%** of those who stopped bought, versus **30%** in the 6-jam
condition, a ~10× difference in conversion.

**Why it matters.** A larger feasible set produced *worse* outcomes. Under IRC, more options
are weakly better by construction — you can always ignore the extras.

**Use if:** you were paralysed by options, deferred, or defaulted.

> ⚠️ Note for critical engagement: this result has a **contested replication record**
> (Scheibehenne, Greifeneder & Todd, 2010, find a near-zero mean effect in meta-analysis).
> Acknowledging that in one clause demonstrates evaluative skill — but it costs words, so
> only include it if you have room.

---

## 10. Preference Reversals (Lichtenstein & Slovic, 1971; Grether & Plott, 1979)

**Setup.** Two bets of similar expected value:
- **P-bet**: high probability, small prize
- **$-bet**: low probability, large prize

Participants **choose** between them, and separately **price** each.

**Result.** People typically **choose the P-bet** but **price the $-bet higher** — a direct
violation of procedure invariance. Grether & Plott set out to debunk it as an artefact of
psychologists' methods, controlled for every economic objection, and **reproduced it**.

**Why it matters.** Arguably the most damaging single finding for the idea of a stable
underlying preference ordering. Also a lovely piece of intellectual history.

**Use if:** your stated valuation and your actual choice diverged.

---

## 11. "A Fine Is a Price" (Gneezy & Rustichini, 2000)

**Setup.** Israeli day-care centres introduced a small fine for collecting children late.

**Result.** Late collections **roughly doubled** — and remained high after the fine was
withdrawn.

**Why it matters.** The price **crowded out** a social norm, converting a moral obligation
into a purchasable commodity. The effect was *not* reversible. Directly relevant to the
module's organisational/managerial economics strand.

**Use if:** an explicit incentive changed your motivation perversely.

---

## 12. Default Effects / Organ Donation (Johnson & Goldstein, 2003)

**Setup.** Compare consent rates in countries with opt-in vs opt-out organ donation defaults.

**Result.** Opt-in countries clustered around **4–28%**; opt-out countries around
**86–100%**. Neighbouring, culturally similar country pairs (Austria vs Germany, Sweden vs
Denmark) show the gap starkly.

**Why it matters.** A decision of the highest personal significance is dominated by an
administrative default. Foundational for **nudge** / choice architecture
(Thaler & Sunstein, 2008).

**Use if:** you went with a default, or failed to switch.

> ⚠️ Verify every experiment, figure and citation against the module materials before use.
> Reported magnitudes above are from general knowledge and should be checked against the
> primary sources.
