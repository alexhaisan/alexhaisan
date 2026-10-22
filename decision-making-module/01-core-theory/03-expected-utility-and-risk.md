# 03 — Expected Utility, Risk and Uncertainty

> Needed if your decision involved **risk** (known probabilities) or **uncertainty**
> (unknown probabilities). Skip to `04-irc-worked-template.md` if your decision was
> essentially riskless (e.g. a sunk-cost or self-control decision).

---

## 1. The three decision environments

| Environment | Probabilities | Model | Source |
|---|---|---|---|
| **Certainty** | Outcomes known | Ordinal utility maximisation | Standard micro |
| **Risk** | Known, objective | Expected Utility Theory (EUT) | von Neumann & Morgenstern (1944) |
| **Uncertainty / ambiguity** | Unknown or unknowable | Subjective Expected Utility (SEU) | Savage (1954) |

Knight (1921) draws the risk/uncertainty distinction: **risk is measurable, uncertainty is
not.** Savage's achievement was to show that a consistent agent behaves *as if* they had
subjective probabilities even under uncertainty — which is exactly what the Ellsberg Paradox
then undermined.

---

## 2. Expected Value vs Expected Utility

**Expected value** is linear in money: $EV = \sum p_i x_i$.

Expected value alone cannot explain why anyone buys insurance *and* why anyone gambles, nor
why nobody will pay an unbounded sum for the **St. Petersburg gamble** (infinite EV, yet
people offer only a few pounds). Bernoulli's (1738) resolution — **diminishing marginal
utility of wealth** — is the origin of expected *utility*:

$$EU = \sum_i p_i \, u(x_i), \qquad u'(x) > 0, \quad u''(x) < 0$$

## 3. Risk attitudes from curvature

| Curvature of $u$ | Attitude | Behaviour | Certainty equivalent |
|---|---|---|---|
| $u'' < 0$ (concave) | Risk **averse** | Prefers the sure thing to a fair gamble | $CE < EV$ |
| $u'' = 0$ (linear) | Risk **neutral** | Indifferent; maximises EV | $CE = EV$ |
| $u'' > 0$ (convex) | Risk **loving** | Prefers the gamble | $CE > EV$ |

**Risk premium** $= EV - CE$: the amount you will pay to avoid the risk.

> **Note for your coursework:** being risk averse is **not** a deviation from IRC. It is a
> perfectly rational preference, fully inside the model. Do not write "I was irrational
> because I played it safe." The deviation has to be in the *structure* of how risk was
> handled — e.g. being risk averse over gains and risk *seeking* over losses in the
> same decision (that is Prospect Theory, and it *is* a violation).

---

## 4. Where EUT breaks — the two canonical attacks

### Allais Paradox (1953) — violates Independence
People prefer a **certain** £1m to a gamble with higher EV, but when both options are
scaled down so neither is certain, they switch to the high-EV gamble. The shared component
was supposed to be irrelevant; it isn't. → **Certainty effect**, → Prospect Theory's
**non-linear probability weighting** $\pi(p)$.

### Ellsberg Paradox (1961) — violates SEU
People prefer betting on **known** 50/50 odds over **unknown** odds, in both directions
simultaneously — which is incoherent under any single probability distribution.
→ **Ambiguity aversion.** People dislike not knowing the odds, over and above disliking risk.

Both are in `../03-experiments/01-canonical-experiments.md` with full setups.

---

## 5. Bayesian updating — the belief component

IRC requires beliefs to be revised by **Bayes' rule**:

$$p(H \mid E) = \frac{p(E \mid H)\, p(H)}{p(E)}$$

Documented systematic failures:

| Failure | What happens | Source |
|---|---|---|
| **Base-rate neglect** | Prior $p(H)$ ignored in favour of case-specific detail | Kahneman & Tversky (1973) |
| **Conservatism** | Beliefs updated *too little* relative to Bayes | Edwards (1968) |
| **Confirmation bias** | $p(E\mid H)$ assessed asymmetrically; disconfirming evidence discounted | Wason (1960); Nickerson (1998) |
| **Conjunction fallacy** | $p(A \cap B) > p(A)$ judged — logically impossible | Tversky & Kahneman (1983) |
| **Overconfidence** | Confidence intervals far too narrow | Alpert & Raiffa (1982) |

> If your decision involved **getting the probability wrong** rather than *acting* wrongly,
> this is your section — it is a failure of **Elster's condition (ii)**.

---

## 6. Sources

- Bernoulli, D. (1738/1954) 'Exposition of a new theory on the measurement of risk', *Econometrica*, 22(1), pp. 23–36.
- Knight, F.H. (1921) *Risk, Uncertainty and Profit*. Boston: Houghton Mifflin.
- von Neumann, J. and Morgenstern, O. (1944) *Theory of Games and Economic Behavior*. Princeton: Princeton University Press.
- Savage, L.J. (1954) *The Foundations of Statistics*. New York: Wiley.
- Ellsberg, D. (1961) 'Risk, ambiguity, and the Savage axioms', *Quarterly Journal of Economics*, 75(4), pp. 643–669.
- Kahneman, D. and Tversky, A. (1973) 'On the psychology of prediction', *Psychological Review*, 80(4), pp. 237–251.
- Tversky, A. and Kahneman, D. (1983) 'Extensional versus intuitive reasoning: the conjunction fallacy in probability judgment', *Psychological Review*, 90(4), pp. 293–315.
- Nickerson, R.S. (1998) 'Confirmation bias: a ubiquitous phenomenon in many guises', *Review of General Psychology*, 2(2), pp. 175–220.

> ⚠️ Verify all citations against the module reading list before use.
