# Bilingual Teaching Standard

## Purpose
This repository is one curriculum with two synchronized localizations: English and Persian. Neither language is a secondary or delayed edition.

## Source of truth
Every chapter must be planned from one shared learning outline. The English and Persian versions must teach the same concepts, in the same order, at equivalent depth.

## Required chapter structure
1. Overview
2. Learning objectives
3. Prerequisites
4. Lessons and explanations
5. Worked examples
6. Common mistakes
7. Practice exercises
8. Chapter recap
9. Self-check
10. Glossary

## Technical consistency
- Python behavior, algorithms, identifiers, filenames, outputs, tests, and type annotations must match between languages.
- Keep code executable and examples equivalent.
- Localize learner-facing prose, prompts, comments, and docstrings where appropriate.
- Introduce technical vocabulary with the English term and a clear Persian equivalent in the Persian edition.
- Type hints must be accurate and must not imply runtime enforcement.

## Pairing workflow
1. Agree on objectives, concepts, examples, and exercise IDs.
2. Draft both language editions from the same outline.
3. Compare section-by-section for omissions and meaning drift.
4. Run or verify code examples and expected outputs.
5. Review language, terminology, accessibility, and difficulty.
6. Update both progress trackers together.
7. Publish only after both editions pass the checklist.

## Status values
Planned → Draft → Needs pairing → In review → Paired → Verified → Published.

A chapter cannot be marked Published if its other-language counterpart is missing, outdated, or unreviewed.

## Release checklist
- [ ] Matching chapter identifiers and filenames
- [ ] Same objectives and prerequisites
- [ ] Same concepts and section order
- [ ] Equivalent examples and outputs
- [ ] Matching exercise IDs, counts, and difficulty
- [ ] Code and type hints checked
- [ ] Terminology reviewed in both languages
- [ ] Both progress trackers updated
- [ ] Cross-language links verified
