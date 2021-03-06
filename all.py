"""This script reads from a file `input.csv` that has been *directly* exported
from our spreadsheet in CSV format and a file `main.csv` thas has been
generated by the script `main.py`. It outputs a list of *all* users and their
match to standard output.
"""

import csv
from util import username

with open("input.csv", newline="") as inputcsv:
    with open("main.csv", newline="") as maincsv:
        maincsv = list(csv.reader(maincsv))
        for inputrow in list(csv.reader(inputcsv))[1:]:
            if not inputrow[2]:
                match = ""
                name = username(inputrow[1])
                for mainrow in maincsv:
                    if name == mainrow[0]:
                        match = mainrow[1]
                        break
                    elif name == mainrow[1]:
                        match = mainrow[0]
                        break
                print(f"{name},{match}")
            else:
                print()