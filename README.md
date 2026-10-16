# tmscli

**Minesweeper, in your terminal, all at once.**

`tmscli` is a lightweight Python module that brings classic Minesweeper into your terminal. No GUI, no dependencies beyond the standard library — just you, a grid, and a few mines.

---

## Why tmscli?

Bored of sitting there, with all your work done, but unable to do anything?

`tmscli` brings Minesweeper to the terminal and is customisable, so you can shape the board to suit your mood — from a quick 9×9 coffee break to a punishing 16×16 minefield.

---

## Installation

Install from PyPI:

```bash
pip install tmscli

# Default game
tmscli

# Bigger board, more mines
tmscli -s 16 -m 40

# Read the rules first
tmscli --rules

# Combine flags
tmscli -s 12 -m 20