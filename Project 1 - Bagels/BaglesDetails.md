# Bagels 🥯

A deductive logic guessing game written in Python.

Recoded by **Sothea Sokea**

## About

The computer thinks of a random 4-digit number. You have 15 guesses to figure out what it is. After each guess, you get clues to help you narrow it down.

## Clues

| Clue     | Meaning                                              |
|----------|-------------------------------------------------------|
| `Pico`   | One digit is correct but in the wrong position        |
| `Fermi`  | One digit is correct and in the right position         |
| `Bagels` | No digit is correct                                    |

## How to Play

1. Run the script:
   ```bash
   python baglesGame.py
   ```
2. Enter your guess as a 4-digit number when prompted.
3. Read the clues and use them to refine your next guess.
4. Guess the exact number within 15 tries to win!

## Example

```
Bagels, a deductive logic game.
Recoded by Sothea Sokea

I am Thinking of a 4-digit positive number. Try to guess what it is.
Here are some clues:

When I say: That means:
+ Pico       One digit is correct but in the wrong direction.
+ Fermi      One digit is correct and in the right position.
+ Bagels     No digit is correct.

I have thought up a number.
-> You have 15 guesses to get it.

Guess #1: 1234
Pico Pico

Guess #2: 0125
Bagels

Guess #3: 3480
Fermi Fermi Pico

Guess #4: 3468
You got it!
```

In this example, the secret number was `3468`. Here's how the clues guided each guess:

- **Guess #1 (`1234`)** → `Pico Pico`: the digits `3` and `4` exist in the secret number, but neither is in the correct position.
- **Guess #2 (`0125`)** → `Bagels`: none of these digits (`0`, `1`, `2`, `5`) appear in the secret number at all, ruling them out completely.
- **Guess #3 (`3480`)** → `Fermi Fermi Pico`: `3` and `4` are now in the exact right positions (2 Fermis), `8` is a correct digit but in the wrong spot (Pico), and `0` doesn't appear in the secret number at all.
- **Guess #4 (`3468`)** → `You got it!`: every digit matches exactly, in the exact right positions — game over, win!

Each guess narrows down the possibilities, combining position clues (Fermi), digit clues (Pico), and elimination (Bagels) until you can deduce the full number.

## Code Overview

- `instruction()` — Prints the game rules and welcome message.
- `getRandomNumber()` — Generates a random 4-digit secret number (as a zero-padded string).
- `getClue(guessNumber, secretNumber)` — Compares the guess to the secret number and returns clues (`Fermi`, `Pico`, `Bagels`, or `"You got it!"`).
- Main game loop — Prompts the user for guesses, validates/pads input to 4 digits, shows clues, and tracks guess count (max 15).

## Requirements

- Python 3.6+ (uses f-strings)

## License

Free to use and modify.