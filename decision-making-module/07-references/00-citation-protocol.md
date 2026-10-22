# 00 — Citation Capture Protocol

> You asked that when we absorb an idea or framework we record the source precisely —
> reference, page, paragraph, where in the text. This is the standing rule for this
> knowledge base.

## The rule

**Nothing enters this knowledge base as a usable idea without a locator.** If a locator
can't be given, the claim is marked `[LOCATOR MISSING]` and is not citable until it is.

## The locator format

```
Author (Year, p. X, §Section, ¶N)
```

- **p. X** — the printed page number in the source, not the PDF page
- **§Section** — the section heading, which survives different editions and printings
- **¶N** — paragraph number counted from the start of that section or page
- For a direct quotation: quote **verbatim**, in quotation marks, with the page

### Worked example
> *"Just as chemists know not to mix reagents in dirty test tubes, so we know that there is
> no point in testing economic propositions in circumstances to which they should not
> reasonably be expected to apply."*
> — Binmore (1999, p. F24, §Conclusion, ¶2)

## Where things go

| Artefact | Location |
|---|---|
| Full notes on a source, section by section | `../05-further-reading/notes/<author>-<year>.md` |
| **Quotes you might actually use, with locators** | `03-quote-ledger.md` |
| The Harvard reference itself | `02-bibliography.md` |
| How to format a Harvard citation | `01-harvard-style-guide.md` |

## Verification states

| Mark | Meaning |
|---|---|
| ✅ **VERIFIED** | Read in the original. Page, section and wording checked against the text. |
| ⚠️ **SECONDHAND** | Taken from another source citing it. Cite the original only after reading it. |
| ❌ **UNVERIFIED** | From general knowledge. **Not citable.** Verify or drop. |

Everything in `03-quote-ledger.md` is ✅ — read from the PDFs you supplied. Much of
`02-bibliography.md` is still ❌ and labelled as such.

## Three rules worth holding

1. **Cite the original, not the slide.** Where a lecture slide quotes Elster, cite Elster.
   Slides are secondary and read as thin in an economics assessment.
2. **Quote verbatim or don't quote.** A paraphrase in quotation marks is a misquotation.
   If you're compressing, drop the quotation marks and cite the page anyway.
3. **Record the locator at the moment of reading.** Reconstructing it later is where errors
   enter, and a wrong page number is worse than no quote — it suggests the source wasn't read.
