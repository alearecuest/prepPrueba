#!/usr/bin/python3
"""
### **Exercise 5: Working with CSV Files**

1. Write a Python program to:
   - Create a CSV file `data.csv` with columns `Name`, `Age`, `City`.
   - Write at least 3 rows of data to the file.
   - Read the file back and print its contents in a formatted table.
"""


import csv

with open("data.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Name", "Age", "City"])
    writer.writerow(["Alice", 30, "New York"])
    writer.writerow(["Bob", 25, "Los Angeles"])
    writer.writerow(["Charlie", 35, "Chicago"])

with open("data.csv", "r") as csvfile:
    reader = csv.reader(csvfile)
    rows = list(reader)

col_widths = [max(len(str(item)) for item in col) for col in zip(*rows)]

for i, row in enumerate(rows):
    print(" | ".join(str(item).ljust(col_widths[j]) for j, item in enumerate(row)))
    if i == 0:
        print("-+-".join("-" * w for w in col_widths))
