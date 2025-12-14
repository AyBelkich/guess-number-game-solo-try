# Guess the Number – Python CLI Game

## Overview

This is a simple command-line "guess the number" game written in Python.

The program:

- randomly picks a number between 1 and 100,
- asks you to guess the number,
- tells you if your guess is too high or too low,
- counts how many attempts you needed,
- lets you play multiple rounds in one run.

This project is mainly for practicing basic Python, input handling, loops, and simple program structure.

## Requirements

- Python 3.8+ (any recent Python 3 version should work)
- No external libraries are required (only the standard library `random` module is used).

## How to Run

1. Clone the repository:

    gh repo clone AyBelkich/guess-number-game-solo-try
    cd guess-number-game-solo-try

2. Run the game:

    python guess_game.py

## How the Code Is Structured

1. game_session()

    Contains the logic for one full game:
    - choose a random secret number,
    - prompt for guesses,
    - validate input,
    - trck attempts,
    - give feedback (too high / too low / correct).

2. main()

    Controls the overall program flow:
    - calls game_session() once,
    - asks if you want to play again,
    - loops until you choose to quit.

3. if __name__ == "__main__":

    Makes sure main() runs only when the file is executed as a script, not when it’s imported as a module.

## Possible Improvements (Future Work)

- Add difficulty levels (different ranges of numbers).
- Add a maximum number of attempts.
- Save best scores to a file.
- Add simple tests for the core logic.
