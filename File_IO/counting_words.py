#!/usr/bin/python3
"""
### **Exercise 2: Counting Words in a File**

1. Create a file `words.txt` with some text (you can create it manually or within the program).
2. Write a program to read the file and count the number of words in it.
"""


with open("words.txt", "w") as file:
    file.write("Python is a powerful programming language.\n")
    file.write("It is easy to learn and fun to use!\n")

word_count = 0
with open("words.txt", "r") as file:
    for line in file:
        words = line.split()
        word_count += len(words)

print(f"Total number of words in 'words.txt': {word_count}")
