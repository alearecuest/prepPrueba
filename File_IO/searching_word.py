#!/usr/bin/python3
"""
### **Exercise 4: Searching for a Word in a File**

1. Write a program to:
   - Prompt the user for a filename and a word to search for.
   - Read the file and count the occurrences of the word (case-insensitive).
"""


filename = input("Enter the filename: ")
search_word = input("Enter the word to search for: ")

count = 0

try:
    with open(filename, "r") as file:
        for line in file:
            words = line.lower().split()
            count += sum(word.strip(".,!?;:()[]\"'") == search_word.lower() for word in words)
    print(f"The word '{search_word}' appears {count} times in '{filename}'.")
except FileNotFoundError:
    print(f"File '{filename}' not found.")