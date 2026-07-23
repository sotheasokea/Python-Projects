# My Python Learning Journey

## Inspiration

The projects and others like it in this repository is inspired by **[The Big Book of Small Python Projects](https://inventwithpython.com/bigbookpython/)** by **AL Sweigart**, a collection of 81 small, beginner-friendly Python programs.

Rather than just reading through the book, I'm using it as a **starting point** to actively learn: reading the base version of each project, then rebuilding, tweaking, and extending the code myself to better understand how and why it works.

## My Approach

1. **Read** : Go through the project description and starter code in the book to understand the goal of the game/program.
2. **Type it out myself** : Rather than copy-pasting, I write the code from scratch based on my understanding, which forces me to actually think through the logic instead of just transcribing.
3. **Break it (on purpose)** : Run into errors, debug them, and understand *why* they happened — this has taught me more than getting it right on the first try ever could.
4. **Modify it** : Once the base version works, I try to change or add my own features: different input validation, better formatting, extra rules, renamed variables that make more sense to me, etc.
5. **Document it** : Write my own README for each project explaining how it works, in my own words, as a way of checking whether I truly understand it or I'm just following along.

## What I'm Learning

- Core Python syntax and control flow (loops, conditionals, functions)
- String manipulation (slicing, formatting, padding with `.zfill()`, f-strings)
- Working with the terminal / command line (PowerShell, Git commands)
- Debugging real errors (`IndexError`, `TypeError`, `ValueError`) by reading tracebacks instead of guessing
- Version control basics with Git — `init`, `add`, `commit`, `push`, and connecting to remote repositories on GitHub
- How to structure small programs into functions instead of one long script

## Example: Bagels

The **Bagels** game (`baglesGame.py`) in this repo is one of the projects from the book. I rebuilt the guessing logic myself, then went further by:

- Adding input validation so the game doesn't crash on bad input (too short, too long, or non-numeric guesses)
- Padding short guesses with leading zeros using `.zfill()`
- Cropping overly long guesses using slicing (`[:4]`)
- Writing my own explanation of how the clue system (`Fermi`, `Pico`, `Bagels`) works, to make sure I actually understood the logic rather than just copying it

## Why This Matters to Me

I don't just want to finish 81 projects — I want to understand *why* each line of code works the way it does, so I can eventually write my own programs from scratch without needing a reference. Modifying and breaking the book's code on purpose has been one of the most useful parts of the process so far.

## Progress

- [x] Bagels
- [x] Birthday Paradox
- [ ] More projects coming as I work through the book...

---

*Book reference: Al Sweigart, "The Big Book of Small Python Projects: 81 Easy Practice Programs," No Starch Press.*
