# 03 — Prospect Theory (Kahneman & Tversky, 1979)

**Attacks IRC components:** (2) preferences — by making them *reference-dependent*;
(3) beliefs — by making probabilities non-linearly weighted; and the **invariance axioms**.

> The most cited paper in economics. If the module covers behavioural economics, this is
> almost certainly on it. It is also the most *formal* alternative to EUT, which makes it
> the strongest choice if your decision genuinely fits.

---

## The three pillars

### 1. Reference dependence
Outcomes are evaluated as **gains and losses relative to a reference point**, not as final
states of wealth. IRC evaluates terminal wealth; prospect theory evaluates *changes*.

> The reference point is typically the status quo, but can be an expectation, an aspiration,
> a purchase price, or whatever the framing suggests. **It is manipulable** — which is
> precisely why framing works.

### 2. Loss aversion
**"Losses loom larger than gains."** The value function is **steeper for losses than for
gains** — empirically by a factor of roughly **λ ≈ 2 to 2.5**.

### 3. Diminishing sensitivity → the reflection effect
The value function is **concave over gains** (risk averse) and **convex over losses**
(risk *seeking*). The same person, in the same decision, switches risk attitude depending
on whether the outcome is framed as a gain or a loss. **This is a direct violation of EUT**,
which requires a single consistent risk attitude over final wealth states.

### The value function

$$
v(x) = \begin{cases}
x^{\alpha} & x \geq 0 \\[4pt]
-\lambda(-x)^{\beta} & x < 0
\end{cases}
$$

with $\alpha, \beta \approx 0.88$ and $\lambda \approx 2.25$ (Tversky & Kahneman, 1992).

```
              value
                │      ╭───────  concave over gains
                │   ╭──╯            (risk averse)
                │ ╭─╯
   ─────────────┼─────────────  outcome
         ╭──────┤ 0
      ╭──╯      │   reference point
   ╭──╯         │
  ╱             │   steeper over losses
 ╱              │   (loss aversion, λ≈2.25)
                │   convex ⇒ risk seeking
```

### 4. Probability weighting
Probabilities are replaced by a **decision weight** $\pi(p)$: small probabilities are
**over-weighted**, moderate-to-large probabilities **under-weighted**. This is why people
buy both lottery tickets and insurance — and it resolves the **Allais Paradox**.

### 5. Editing and framing
Before evaluation, prospects are **edited**: coded as gains/losses, combined, segregated,
cancelled. The editing phase is where framing does its work — and editing is *not*
invariant to description.

---

## The documented consequences

| Phenomenon | Mechanism | Source |
|---|---|---|
| **Framing effects** | Reference point shifts with wording | Tversky & Kahneman (1981) |
| **Endowment effect** | Ownership makes giving up a *loss*; WTA > WTP (often 2×) | Kahneman, Knetsch & Thaler (1990) |
| **Status quo bias** | Moving away from the default is coded as a loss | Samuelson & Zeckhauser (1988) |
| **Disposition effect** | Sell winners early (risk averse over gains), ride losers (risk seeking over losses) | Shefrin & Statman (1985); Odean (1998) |
| **Equity premium puzzle** | Myopic loss aversion from frequent portfolio evaluation | Benartzi & Thaler (1995) |
| **Default effects in organ donation** | Opt-out countries show vastly higher consent rates | Johnson & Goldstein (2003) |

---

## Using it in the coursework

**Fits if:** the wording/framing of the option changed your choice; you over-weighted a
potential loss; you refused to sell or abandon something you would not have bought at that
price; you took a bigger risk to avoid crystallising a loss; you stayed with a default.

**Does not fit if:** there was no identifiable reference point, no gain/loss framing, and no
risk. A pure search-failure or a pure belief error belongs elsewhere.

**Specimen sentence (≈40 words):**
> *Prospect theory (Kahneman & Tversky, 1979) explains this: I evaluated the option relative
> to a reference point rather than in terms of final wealth, and because the value function
> is steeper for losses (λ≈2.25), the prospective loss outweighed an objectively larger gain.*

## Future-application ideas (component D)

- **Re-frame in terms of final states**, not changes: ask *"if I had neither, which would I
  choose today?"* This neutralises the endowment effect directly and is testable in seconds.
- **Flip the default**: make the action you want the status quo, so inertia works for you.
- **Broad bracketing**: evaluate decisions as a portfolio over a long horizon rather than
  one at a time. Benartzi & Thaler (1995) show narrow bracketing is what makes loss aversion
  so costly.
- **Apply the reversal test**: present the identical choice to yourself in both gain and loss
  framing. If your answer changes, the answer is frame-driven, not preference-driven.

## Sources

- Kahneman, D. and Tversky, A. (1979) 'Prospect theory: an analysis of decision under risk', *Econometrica*, 47(2), pp. 263–291.
- Tversky, A. and Kahneman, D. (1981) 'The framing of decisions and the psychology of choice', *Science*, 211(4481), pp. 453–458.
- Tversky, A. and Kahneman, D. (1991) 'Loss aversion in riskless choice: a reference-dependent model', *Quarterly Journal of Economics*, 106(4), pp. 1039–1061.
- Tversky, A. and Kahneman, D. (1992) 'Advances in prospect theory: cumulative representation of uncertainty', *Journal of Risk and Uncertainty*, 5(4), pp. 297–323.
- Kahneman, D., Knetsch, J.L. and Thaler, R.H. (1990) 'Experimental tests of the endowment effect and the Coase theorem', *Journal of Political Economy*, 98(6), pp. 1325–1348.
- Kahneman, D., Knetsch, J.L. and Thaler, R.H. (1991) 'Anomalies: the endowment effect, loss aversion, and status quo bias', *Journal of Economic Perspectives*, 5(1), pp. 193–206.
- Samuelson, W. and Zeckhauser, R. (1988) 'Status quo bias in decision making', *Journal of Risk and Uncertainty*, 1(1), pp. 7–59.
- Benartzi, S. and Thaler, R.H. (1995) 'Myopic loss aversion and the equity premium puzzle', *Quarterly Journal of Economics*, 110(1), pp. 73–92.
- Johnson, E.J. and Goldstein, D. (2003) 'Do defaults save lives?', *Science*, 302(5649), pp. 1338–1339.

> ⚠️ Verify against the module reading list.
