#!/usr/bin/python3
"""
### **Exercise 5: Serialize Complex Objects**

1. Serialize an object containing datetime or other non-serializable types using `json` by writing a custom encoder.
2. Deserialize the JSON string back into the original object using a custom decoder.

**Example:**

```python
from datetime import datetime

data = {"event": "Meeting", "time": datetime.now()}
```
"""


import json
from datetime import datetime

data = {"event": "Meeting", "time": datetime.now()}

class CustomEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return {"__datetime__": True, "iso": obj.isoformat()}
        return super().default(obj)

def custom_decoder(obj):
    if "__datetime__" in obj:
        return datetime.fromisoformat(obj["iso"])
    return obj

with open("event.json", "w") as f:
    json.dump(data, f, cls=CustomEncoder)

with open("event.json", "r") as f:
    loaded_data = json.load(f, object_hook=custom_decoder)

print("Deserialized object:", loaded_data)
print("Type of 'time' after deserialization:", type(loaded_data['time']))