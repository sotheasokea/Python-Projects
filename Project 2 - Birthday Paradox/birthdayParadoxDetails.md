# 🎂 Birthday Paradox Simulator

A Python program that demonstrates the **Birthday Paradox** (also called the Birthday Problem) using Monte Carlo simulation.

> Originally an exercise from *"The Big Book of Small Python Projects"* by Al Sweigart.

## What Is the Birthday Paradox?

The Birthday Paradox is the surprisingly high probability that two people in a group share the same birthday, even when the group is relatively small.

- In a group of just **23 people**, there's already about a **50%** chance of a shared birthday.
- In a group of **70 people**, that chance jumps to over **99.9%**.

It's called a "paradox" not because it's logically contradictory, but because the result feels unintuitive — most people guess the odds are much lower than they actually are.

Read more: [Birthday Problem on Wikipedia](https://en.wikipedia.org/wiki/Birthday_problem)

## How It Works

1. **Generate random birthdays** — The program creates a list of random birthdays (month + day, year is ignored since it doesn't matter for this problem).
2. **Check for a match** — It compares every birthday against every other birthday in the group to see if any two match.
3. **Run a Monte Carlo simulation** — To find the *probability* of a match for a given group size, the program repeats the random generation-and-check process **100,000 times** and counts how often at least one match occurs.
4. **Calculate the odds** — The final probability is simply:

   ```
   probability = (number of simulations with a match / total simulations) × 100
   ```

This approach — running many random trials to estimate a probability — is called a **Monte Carlo experiment**, and it's a common technique used when the exact math is hard to calculate directly but easy to simulate.

## Requirements

- Python 3.6 or higher (uses f-string-free syntax, but relies on the `datetime` and `random` standard library modules — no extra installation needed)

## How to Run

```bash
python birthdayParadox.py
```

You'll be prompted to enter a group size (1–100). The program will then:

1. Print a sample list of randomly generated birthdays for that group size.
2. Report whether any of them match.
3. Run 100,000 simulations to calculate the overall probability of a birthday match for that group size.

### Example Output

```
Birthday Paradox, by Al Sweigart al@inventwithpython.com

How many birthdays shall I generate? (Max 100)
> 23

Here are 23 birthdays:
Oct 9, Sep 1, May 28, Jul 29, Feb 17, Jan 8, Aug 18, Feb 19, Dec 1,
Jan 22, May 16, Sep 25, Oct 6, May 6, May 26, Oct 11, Dec 19, Jun 28,
Jul 29, Dec 6, Nov 26, Aug 18, Mar 18

In this simulation, multiple people have a birthday on Jul 29

Generating 23 random birthdays 100,000 times...
Press Enter to begin...

Let's run another 100,000 simulations.
0 simulations run...
10000 simulations run...
...
100000 simulations run.

Out of 100,000 simulations of 23 people, there was a
matching birthday in that group 50955 times. This means
that 23 people have a 50.95% chance of
having a matching birthday in their group.
That's probably more than you would think!
```

## Code Overview

| Function                             | Purpose |
|--------------------------------------|---|
| `introduction()`                     | Prints the program's welcome message and explanation |
| `generateBirthday(numberOfBirthday)` | Generates a list of `numberOfBirthday` random `date` objects, all within the same year |
| `getMatchBirthday(birthdays)`        | Checks a list of birthdays for any matching pair; returns the matching date or `None` |

### Key Concepts Used

- **`datetime.date` and `timedelta`** — Used to generate valid random calendar dates without worrying about invalid combinations (like Feb 30th).
- **Sets for quick duplicate detection** — `len(birthdays) == len(set(birthdays))` is a fast way to check if *any* duplicates exist before doing a more detailed comparison.
- **Underscore in numeric literals** — Numbers like `100_000` are functionally identical to `100000`; the underscore is just there to make large numbers easier to read.
- **Monte Carlo simulation** — Repeated random trials used to estimate a probability that would be complex to calculate analytically.

## Possible Improvements

- Add a way to skip the confirmation prompt (e.g., a `--yes` flag) for scripting/automation.
- Plot the probability curve across different group sizes (e.g., 1–100) using `matplotlib`.
- Add unit tests for `getMatchBirthday()` to verify edge cases (empty list, single birthday, all matching, etc.).

## License

Free to use and modify for learning purposes.