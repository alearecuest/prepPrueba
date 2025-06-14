#!/usr/bin/python3
"""
### **Exercise 1: Reading and Writing a File**

1. Write a Python program to:
   - Write the following lines to a file called `example.txt`:

     ```text
     Hello, world!
     Welcome to file I/O in Python.
     ```

   - Read the contents of `example.txt` and print them line by line.
"""


with open("example.txt", "w") as file:
    file.write("Hello, World!\n")
    file.write("Welcome to file I/O in Pyton.\n")

with open("example.txt", "r") as file:
    for line in file:
      print(line, end="")
