# 01 — The Instrumental Rational Choice (IRC) Model

> **The single most important file in this knowledge base.** Component A of the coursework
> is a definition of this model and its components; component B requires you to run your
> own decision through it. Everything else is commentary.

---

## 1. The core idea in one paragraph

Instrumental Rational Choice holds that an agent is rational when their **actions are the
best available means to their own ends**, given what they believe about the world. The word
**instrumental** is doing the decisive work: reason is an *instrument* that serves ends it
does not itself choose. The model evaluates the **means–ends relationship**, not the ends.
A person who wants something strange is not thereby irrational; a person who acts in a way
that does not get them what they want, given what they know, is.

This is the Humean position — *"Reason is, and ought only to be the slave of the passions"*
(Hume, 1739) — formalised into economics as the standard model of choice.

**Why this matters for your coursework:** the brief asks what *"an instrumentally rational
decision-maker **with your preferences**"* would do. Because IRC takes preferences as given,
you cannot locate your deviation in *what you wanted*. It must sit in the **means**, the
**beliefs**, or the **consistency**. See §5.

---

## 2. Formal statement

**Under certainty**

$$\max_{x \in B} \; U(x)$$

Choose the element $x$ of the feasible set $B$ that maximises the utility function $U$.

**Under risk** (von Neumann & Morgenstern, 1944)

$$EU(a) \;=\; \sum_{s \in S} p(s)\, u\big(c(a,s)\big)$$

For each action $a$, sum the utility $u$ of its consequence $c$ in each state of the world
$s$, weighted by the probability $p(s)$ of that state. Choose the $a$ with the highest $EU$.

**Under uncertainty** (Savage, 1954) — the same, but $p(s)$ are the agent's *subjective*
probabilities, which must obey the probability axioms and update by Bayes' rule:

$$p(s \mid e) = \frac{p(e \mid s)\, p(s)}{p(e)}$$

---

## 3. The components

This is the list component A of the coursework must name. Six components, grouped into
three families.

### The inputs

#### (1) The agent
The individual decision-maker is the unit of analysis — **methodological individualism**.
Groups, firms and societies are explained by aggregating individual choices, not by
treating the collective as a chooser in its own right.

#### (2) Preferences
A **complete** and **transitive** ordering $\succsim$ over outcomes, assumed **given**,
**stable**, and **exogenous** to the choice situation. Formally represented by a utility
function $U$ — where utility is a *ranking device*, not a psychological quantity of pleasure.

> Critically: IRC says **nothing about the content** of preferences. Altruistic, spiteful,
> short-sighted or eccentric preferences are all admissible. Only their **structure** is
> constrained. (Full axiom list: `02-preference-axioms.md`.)

#### (3) Beliefs
A probability distribution over states of the world and over the consequences of each
action. Rational beliefs are those that are (a) internally consistent, (b) **proportioned
to the available evidence**, and (c) **updated by Bayes' rule** as evidence arrives.

#### (4) Constraints — the feasible set
The set $B$ of options genuinely available: budget, time, technology, information,
institutions, law, physical possibility. An option outside $B$ is not a failure of
rationality — it was never available.

### The process

#### (5) The choice rule — optimisation
Rank all feasible options by expected utility and **select the maximum**. Not "good enough"
— the *best*. This is the component most often violated in practice, and the one Simon's
bounded rationality directly attacks (`02-deviations-and-theories/01-bounded-rationality.md`).

### The output

#### (6) Consequentialism
Actions are valued **solely by their consequences**. The act itself carries no intrinsic
value — no duty, no rule-following, no symbolic meaning, no identity expression, except
insofar as these show up as consequences the agent values.

---

## 4. Elster's three conditions — the diagnostic you will actually use

Jon Elster decomposes rational action into **three separate optimality conditions**. This is
the most useful formulation for your coursework, because it gives you **three distinct places
a decision can break**, and your answer needs to say precisely which one broke.

| | Condition | Fails when… |
|---|---|---|
| **(i)** | The **action** is the best means of satisfying the desire, **given the belief** | You knew the right thing to do and did something else — akrasia, present bias, impulse, emotion |
| **(ii)** | The **belief** is the best that could be formed, **given the evidence** | You had the evidence and drew the wrong inference — availability, representativeness, anchoring, confirmation bias, base-rate neglect |
| **(iii)** | The **amount of evidence collected** is itself optimal, **given the desire** | You searched too little (snap judgement) or too much (analysis paralysis, over-research) relative to what the decision was worth |

*(Elster, 1983; 1989 — verify exact source and page against the module reading list.)*

**How to use it:** take your decision, test each condition in turn, and identify which
one(s) failed. That sentence — *"my decision satisfied (iii) but violated (i)"* — is a
precise, high-credit statement of how your process differed from the model. It is worth
far more than "I was irrational."

---

## 5. Thin vs thick rationality — and the trap in the brief

| | **Thin** rationality | **Thick** rationality |
|---|---|---|
| Claim | Preferences are **internally consistent**; action follows from preferences + beliefs | Adds **substantive** assumptions: agents are self-interested, materially motivated, forward-looking |
| Content of preferences | Unconstrained | Constrained (narrow self-interest) |
| Can it be falsified by "I gave money away"? | **No** | Yes |

The brief's phrase *"an instrumentally rational decision-maker **with your preferences**"*
pins you to the **thin** version. Your counterfactual agent wants exactly what you want.

**Consequence — the Deviation Test.** A candidate decision only works for this coursework if
you can answer **yes** to at least one of:

1. **Inconsistency** — did I violate transitivity, invariance, independence or dominance?
   Did I choose differently depending on how the option was *described* or *elicited*?
2. **Belief failure** — did I process the available evidence in a way Bayes' rule would not
   sanction? Did I ignore base rates, over-weight a vivid instance, anchor on an arbitrary number?
3. **Means–ends failure** — did I take an action that, *by my own lights at the time*, did
   not best serve my own goal? Did I later reverse my own judgement without new information?
4. **Search failure** — was my information-gathering grossly mismatched to the stakes?

If the honest answer to all four is "no", you have described a **preference, not a
deviation** — and the piece will not score. Pick another decision.
Worked examples: `04-irc-worked-template.md`. Candidate screening: `../06-coursework-build/01-decision-candidates.md`.

---

## 6. What IRC is good for (do not write a hatchet job)

A 300-word answer that treats IRC as simply wrong will read as naive. The model is the
benchmark *because* it is powerful:

- **Parsimony** — three primitives (preferences, beliefs, constraints) generate predictions
  across every domain of choice.
- **Normative force** — it tells you what you *should* do, which is why deviations from it
  count as *errors* rather than mere differences. Without the benchmark, "bias" is meaningless.
- **Tractability** — it supports comparative statics, equilibrium analysis and welfare
  evaluation, and underwrites most of microeconomics.
- **Empirical reach** — Becker (1976) extended it to crime, marriage, discrimination and
  fertility with real explanatory success.
- **"As if" defence** — Friedman (1953): the model need not describe conscious reasoning,
  only predict behaviour *as if* agents optimised. Competition and learning may weed out
  non-optimisers even if nobody computes anything.

The strongest version of your answer treats IRC as **a benchmark your behaviour departed
from in a systematic, predictable, well-documented way** — which is precisely the
behavioural economics claim. Deviations are not noise; they are patterned.

---

## 7. Key sources

- Hume, D. (1739) *A Treatise of Human Nature*. Book II, Part III, Section III.
- von Neumann, J. and Morgenstern, O. (1944) *Theory of Games and Economic Behavior*. Princeton: Princeton University Press.
- Savage, L.J. (1954) *The Foundations of Statistics*. New York: Wiley.
- Friedman, M. (1953) 'The methodology of positive economics', in *Essays in Positive Economics*. Chicago: University of Chicago Press, pp. 3–43.
- Becker, G.S. (1976) *The Economic Approach to Human Behavior*. Chicago: University of Chicago Press.
- Elster, J. (1986) *Rational Choice*. Oxford: Blackwell.
- Elster, J. (1989) *Nuts and Bolts for the Social Sciences*. Cambridge: Cambridge University Press.
- Sen, A. (1977) 'Rational fools: a critique of the behavioral foundations of economic theory', *Philosophy & Public Affairs*, 6(4), pp. 317–344.
- Hargreaves Heap, S., Hollis, M., Lyons, B., Sugden, R. and Weale, A. (1992) *The Theory of Choice: A Critical Guide*. Oxford: Blackwell.

> ⚠️ **Verify every citation against the module reading list before use.** Page numbers and
> editions above are from general knowledge and must be checked against the actual source.
