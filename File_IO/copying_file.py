#!/usr/bin/python3
"""
### **Exercise 3: Copying a File**

1. Write a program that:
   - Reads the contents of a file `source.txt`.
   - Writes the same contents to a new file `destination.txt`.
"""


with open("source.txt", "w") as f:
    f.write("Este es el contenido de source.txt\nPuedes poner lo que quieras aquí.\n")
    
with open("source.txt", "r") as src_file:
    contents = src_file.read()

with open("destination.txt", "w") as dest_file:
    dest_file.write(contents)