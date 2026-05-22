# MLB Strikeout Projection Calculator

A Python command-line tool that pulls live MLB statistics from the official MLB Stats API and projects how many strikeouts a given pitcher is likely to record against a specific opposing team. The result is compared against a user-defined benchmark to indicate whether the pitcher is projected to go over or under.

## What it does

Given a pitcher's name, a strikeout benchmark, and an opposing team, the program:

1. Looks up the pitcher and retrieves their season pitching stats (innings pitched, games started, strikeouts per 9 innings).
2. Looks up the opposing team and retrieves their season hitting stats (strikeouts, plate appearances).
3. Calculates the pitcher's projected strikeouts against that team's tendency to strike out.
4. Compares the projection to the benchmark and prints whether the pitcher is expected to go over or under.

## How the projection works

The calculation combines individual pitcher performance with the opposing team's strikeout tendency:

- **Innings pitched per start (IP)** = Total Innings Pitched / Games Started
- **Projected strikeouts per game (PG)** = (Strikeouts per 9 innings) × (IP / 9)
- **Opposing team strikeout rate (SO)** = Team Strikeouts / Plate Appearances
- **Projection** = PG × SO × IP, compared against the benchmark

## Requirements

- Python 3.x
- [`python-mlb-statsapi`](https://pypi.org/project/python-mlb-statsapi/)

Install the dependency:

```bash
pip install python-mlb-statsapi
```

## Usage

Run the program from the terminal:

```bash
python MLBCalc.py
```

You'll be prompted to enter:

- The pitcher's full name (e.g., `Gerrit Cole`)
- A strikeout benchmark (e.g., `6.5`)
- The opposing team's abbreviation (e.g., `NYY`)

The program then prints the pitcher's stats, the projection, and whether they're expected to go over or under the benchmark.

## Example output

```
Player's average strikeouts per 9 innings: 9.50
Player's total innings pitched (TI): 180.00
Player's games started (GS): 30.00
Player's average innings pitched per game started (IP): 6.00
Player's average strikeouts per game (PG): 6.33
Opposing team's average strikeout rate (SO): 0.220
Player's average strikeout per IP against opposing team (R): 8.36
The player is expected to go over the benchmark
```

## Notes & possible improvements

This started as a personal project to practice working with REST APIs and applying statistical logic to real-world data.
Most likely won't be updated for future years (currently based off 2025 year)

## Author

Joshua Fernandez
