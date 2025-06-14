#!/usr/bin/python3
"""
### **Exercise 2: Handling Nested Structures**

1. Serialize a nested Python object (e.g., a dictionary containing a list of dictionaries) into JSON.
2. Deserialize the JSON back into the original object and confirm they are identical.

**Sample nested object:**

```python
nested_data = {
    "employees": [
        {"name": "John", "age": 30},
        {"name": "Emma", "age": 25},
    ],
    "department": "HR"
}
"""


import json

nested_data = {
    "employees": [
        {"name": "Alejandro", "age": 40},
        {"name": "Emanuel", "age": 30},
    ],
    "department": "Holberton"
}

with open("nested_data.json", "w") as json_file:
    json.dump(nested_data, json_file)

with open("nested_data.json", "r") as json_file:
    loaded_data = json.load(json_file)

print("Objects are identical:", nested_data == loaded_data)
print("Loaded data:", loaded_data)
