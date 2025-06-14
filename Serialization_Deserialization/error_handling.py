#!/usr/bin/python3
"""
### **Exercise 4: Error Handling During Deserialization**

1. Attempt to deserialize corrupted or improperly formatted data
(e.g., a malformed JSON string) and handle the exceptions gracefully.
"""


import json

bad_json = '{"name": "Alejandro", "age": 40, "city": "Montevideo"}'

try:
    data = json.loads(bad_json)
    print("Deserialized data:", data)
except json.JSONDecodeError as e:
    print("Error decoding JSON:", e)
