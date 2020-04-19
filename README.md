## Overview

The main point of interest is [`main.py`](main.py), as it is the muscle behind the automated matching.
If you want to tweak the scoring system, take a look at [`scoreboard.py`](scoreboard.py).

* [`all.py`](all.py): Generates a list of all users with their match. Useful for pasting data back into the spreadsheet.
* [`main.py`](main.py): Generates user pairs from a CSV input file.
Not very optimized and will often take up to 5 minutes to process large datasets.
* [`scoreboard.py`](scoreboard.py): Implements the scoring system used by [`main.py`](main.py).
* [`util.py`](util.py): Provides utilities for working with the CSV input.