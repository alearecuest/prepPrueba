### **Exercise 1: Basic Class and Object**
1. Create a class Car with the following attributes:
   - brand
   - model
   - year
2. Add a method display_info() to print the details of the car.
3. Instantiate an object of the Car class and call the display_info() method.

---

### **Exercise 2: Inheritance**
1. Create a base class Animal with:
   - Attributes: name, species
   - Method: make_sound() (prints "Some generic sound")
2. Create a subclass Dog that overrides make_sound() to print "Woof!"
3. Instantiate objects of both classes and call make_sound() for each.

---

### **Exercise 3: Encapsulation**
1. Create a class BankAccount with:
   - Private attributes: __balance
   - Methods:
     - deposit(amount) (add to the balance)
     - withdraw(amount) (subtract from the balance if sufficient funds are available)
     - get_balance() (return the current balance)
2. Test the class by creating an account, performing deposits and withdrawals, and accessing the balance.

---

### **Exercise 4: Polymorphism**

1. Create a class Shape with a method area() that raises a NotImplementedError.
2. Create two subclasses Circle and Rectangle that implement the area() method.
3. Write a function that takes a Shape object and prints its area. Test it with instances of Circle and Rectangle.

---

### **Exercise 5: Abstraction with Abstract Classes**

1. Import `ABC` and `abstractmethod` from the `abc` module.
2. Create an abstract class `Payment` with an abstract method `process_payment()`.
3. Implement subclasses `CreditCardPayment` and `PayPalPayment`, each providing their own implementation of `process_payment()`.
4. Demonstrate polymorphism by processing payments using both subclasses.

---

### **Exercise 6: Class vs Instance Attributes**

1. Create a class `Person` with:
   - A class attribute `species` set to "Homo sapiens"
   - Instance attributes `name` and `age`
2. Show how to access and modify the class attribute and the instance attributes.

---

### **Exercise 7: Method Overriding**

1. Create a class `Employee` with:
   - Attributes: `name`, `salary`
   - Method `get_details()` to print employee details.
2. Create a subclass `Manager` that overrides the `get_details()` method to include additional information (e.g., team size).

---

### **Exercise 8: Static and Class Methods**

1. Create a class `Calculator` with:
   - A static method `add(a, b)` that returns the sum of two numbers.
   - A class method `create_default()` that returns a default instance of `Calculator`.
2. Demonstrate the usage of both methods.

---

### **Exercise 9: Multiple Inheritance**

1. Create two classes:
   - `Flyable` with a method `fly()`
   - `Swimmable` with a method `swim()`
2. Create a class `Duck` that inherits from both `Flyable` and `Swimmable`.
3. Instantiate a `Duck` and call both methods.

---

## File/IO

### **Exercise 1: Reading and Writing a File**

1. Write a Python program to:
   - Write the following lines to a file called `example.txt`:

     ```text
     Hello, world!
     Welcome to file I/O in Python.
     ```

   - Read the contents of `example.txt` and print them line by line.

---

### **Exercise 2: Counting Words in a File**

1. Create a file `words.txt` with some text (you can create it manually or within the program).
2. Write a program to read the file and count the number of words in it.

---

### **Exercise 3: Copying a File**

1. Write a program that:
   - Reads the contents of a file `source.txt`.
   - Writes the same contents to a new file `destination.txt`.

---

### **Exercise 4: Searching for a Word in a File**

1. Write a program to:
   - Prompt the user for a filename and a word to search for.
   - Read the file and count the occurrences of the word (case-insensitive).

---

### **Exercise 5: Working with CSV Files**

1. Write a Python program to:
   - Create a CSV file `data.csv` with columns `Name`, `Age`, `City`.
   - Write at least 3 rows of data to the file.
   - Read the file back and print its contents in a formatted table.

---

## Serialization & Deserialization

### **Exercise 1: Basic JSON Serialization and Deserialization**

1. Write a Python program to serialize a dictionary into a JSON string and save it to a file.
2. Read the JSON file and deserialize it back into a dictionary.

**Sample dictionary:**

```python
data = {"name": "Alice", "age": 25, "city": "New York"}
```

---

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
```

---

### **Exercise 3: Serialization with Pickle**

1. Create a custom Python class and instantiate an object of that class.
2. Serialize the object using the `pickle` module and save it to a file.
3. Deserialize the object from the file and verify its properties.

**Example class:**

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Person(name={self.name}, age={self.age})"
```

---

### **Exercise 4: Error Handling During Deserialization**

1. Attempt to deserialize corrupted or improperly formatted data (e.g., a malformed JSON string) and handle the exceptions gracefully.

---

### **Exercise 5: Serialize Complex Objects**

1. Serialize an object containing datetime or other non-serializable types using `json` by writing a custom encoder.
2. Deserialize the JSON string back into the original object using a custom decoder.

**Example:**

```python
from datetime import datetime

data = {"event": "Meeting", "time": datetime.now()}
```
