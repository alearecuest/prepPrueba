#!/usr/bin/python3
"""
### **Exercise 1: Basic JSON Serialization and Deserialization**

1. Write a Python program to serialize a dictionary into a JSON string and save it to a file.
2. Read the JSON file and deserialize it back into a dictionary.

**Sample dictionary:**

```python
data = {"name": "Alice", "age": 25, "city": "New York"}
```
"""


import json

data = {"name": "Alice", "age": 25, "city": "New York"}

with open("data.json", "w") as json_file:
    json.dump(data, json_file)

with open("data.json", "r") as json_file:
    loaded_data = json.load(json_file)

print("Deserialized dictionary:", loaded_data)
