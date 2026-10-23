# 02 — The Axioms of Preference

> These are the **structural constraints** IRC places on preferences. Each axiom is a
> potential site of violation — and therefore a potential subject for your coursework.
> Showing you violated a *named axiom* is a far stronger answer than "I was irrational".

Notation: $x \succ y$ = "x strictly preferred to y"; $x \sim y$ = "indifferent";
$x \succsim y$ = "at least as good as".

---

## A. Ordering axioms (required for a utility function to exist)

### 1. Completeness
For any pair $x, y$: either $x \succsim y$ or $y \succsim x$ (or both).
**You always have an opinion.** No "I can't compare these."

> **Violated when:** options are incommensurable (a career vs. a relationship), or when the
> comparison itself is distressing and you avoid forming a ranking at all.

### 2. Transitivity
If $x \succsim y$ and $y \succsim z$, then $x \succsim z$.
**The backbone of the whole model.**

> **Violated when:** preferences cycle. Classic cause: **just-noticeable-difference** effects
> and **multi-attribute** choice where you compare pairs on different dimensions each time
> (A beats B on price, B beats C on quality, C beats A on convenience).
>
> **Why it is fatal:** an intransitive agent is a **money pump**. If you prefer A to B, B to
> C, and C to A, I can sell you A for B plus a penny, B for C plus a penny, C for A plus a
> penny — and return you to your starting point, poorer. This is the sharpest argument for
> why transitivity is a *normative* requirement, not just a descriptive assumption.

### 3. Reflexivity
$x \succsim x$. Trivial, usually assumed silently.

### 4. Continuity
Small changes in options produce small changes in preference; no sudden jumps. Technically
required for preferences to be representable by a *continuous* utility function.

> **Violated by:** lexicographic preferences ("I will not trade *any* amount of safety for
> *any* amount of money"), and by sacred/protected values.

---

## B. Choice axioms (required for expected utility under risk)

### 5. Independence (of irrelevant alternatives)
If $x \succsim y$, then for any lottery $z$ and probability $p \in (0,1]$:
$$ p x + (1-p) z \;\succsim\; p y + (1-p) z $$
**A common component shared by two gambles should not affect the ranking between them.**

> **Violated by:** the **Allais Paradox** (1953) — the single most important experimental
> violation of expected utility theory, and the direct ancestor of Prospect Theory's
> probability weighting. See `../03-experiments/01-canonical-experiments.md`.

### 6. Monotonicity / Dominance
If option A is at least as good as B in every state and strictly better in at least one,
choose A. **Never choose a dominated option.**

> **Violated when:** framing conceals the dominance relation (Tversky & Kahneman, 1986).

### 7. Reduction of compound lotteries
A two-stage gamble is evaluated identically to the single-stage gamble with the same final
probability distribution. **Only final outcomes and probabilities matter; the path does not.**

---

## C. Invariance axioms (the behavioural flashpoints)

These are not always listed as formal axioms, but they are implied by the model — and they
are where behavioural economics does most of its damage.

### 8. Description invariance (frame invariance)
Preferences should not depend on how a choice is **described**. 600 lives: "200 saved" and
"400 die" are the same state of the world and must be ranked identically.

> **Violated by:** the **Asian Disease Problem** (Tversky & Kahneman, 1981). This is the
> cleanest, most citable framing violation in the literature.

### 9. Procedure invariance
Preferences should not depend on how they are **elicited** — choosing between A and B should
give the same ranking as pricing A and B separately.

> **Violated by:** **preference reversals** (Lichtenstein & Slovic, 1971; Grether & Plott,
> 1979). People *choose* the high-probability/low-payoff bet but *price* the
> low-probability/high-payoff bet higher. Formally devastating.

### 10. Menu independence / context independence
Adding an irrelevant third option should not change the ranking of the first two.

> **Violated by:** the **decoy (asymmetric dominance) effect** and the **compromise effect** —
> both heavily used in pricing and retail. If your decision involved choosing a
> middle-tier option because it was the middle tier, this is your axiom.

### 11. Procedural / reference independence
Valuation should not depend on what you currently **own** or what you take as the baseline.

> **Violated by:** the **endowment effect** (Kahneman, Knetsch & Thaler, 1990) and
> **status quo bias** (Samuelson & Zeckhauser, 1988).

---

## D. Which axiom did *you* violate? — quick diagnostic

| If your decision involved… | Suspect axiom | Go to |
|---|---|---|
| Changing your mind based on wording ("90% fat free" vs "10% fat") | Description invariance (8) | Prospect Theory / framing |
| Choosing the middle option, or a decoy making one look good | Menu independence (10) | Context effects |
| Refusing to sell something you'd never have bought at that price | Reference independence (11) | Endowment effect |
| Sticking with the default because it was the default | Reference independence (11) | Status quo bias |
| Cycling / regretting / reversing without new information | Transitivity (2) or time consistency | Intertemporal choice |
| Paying over the odds for certainty | Independence (5) | Allais / probability weighting |
| Being unable to decide at all, or deferring indefinitely | Completeness (1) | Choice overload |
| Continuing because of money already spent | Consequentialism (not an axiom — a component) | Sunk cost fallacy |

---

## E. Sources

- Allais, M. (1953) 'Le comportement de l'homme rationnel devant le risque: critique des postulats et axiomes de l'école américaine', *Econometrica*, 21(4), pp. 503–546.
- Lichtenstein, S. and Slovic, P. (1971) 'Reversals of preference between bids and choices in gambling decisions', *Journal of Experimental Psychology*, 89(1), pp. 46–55.
- Grether, D.M. and Plott, C.R. (1979) 'Economic theory of choice and the preference reversal phenomenon', *American Economic Review*, 69(4), pp. 623–638.
- Tversky, A. and Kahneman, D. (1981) 'The framing of decisions and the psychology of choice', *Science*, 211(4481), pp. 453–458.
- Tversky, A. and Kahneman, D. (1986) 'Rational choice and the framing of decisions', *Journal of Business*, 59(4), pp. S251–S278.
- Samuelson, W. and Zeckhauser, R. (1988) 'Status quo bias in decision making', *Journal of Risk and Uncertainty*, 1(1), pp. 7–59.
- Kahneman, D., Knetsch, J.L. and Thaler, R.H. (1990) 'Experimental tests of the endowment effect and the Coase theorem', *Journal of Political Economy*, 98(6), pp. 1325–1348.

> ⚠️ Verify all citations against the module reading list before use.
