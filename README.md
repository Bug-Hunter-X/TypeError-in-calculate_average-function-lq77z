# Python Code Bug: Handling Non-numeric Input in Average Calculation

This repository demonstrates a common error in Python code: improper handling of non-numeric input in a function designed to calculate the average of a list of numbers.

## Bug Description

The `calculate_average` function in `bug.py` does not explicitly check for non-numeric input.  If the input list contains any non-numeric values, it will result in a `TypeError`. 

## Solution

The solution is provided in `bugSolution.py`.  It adds error handling to gracefully handle lists containing non-numeric data.
