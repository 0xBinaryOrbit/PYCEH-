# Python Basics – Variables and Data

In this section, you will learn about:
- The different kinds of data you can work with in Python programs.
- How to use **variables** to represent data.
- How Python executes your code.

---

## What Happens When You Run a Python Program?

When you run a Python file (e.g., `main.py`), Python does a fair amount of work, even for a simple program.

### Example
```python
print("Hello World")
```

**Output:**
```
Hello World
```

Here’s what happens step-by-step:
1. The `.py` extension tells your system this is a Python program.
2. Your **code editor** sends the file to the **Python interpreter**.
3. The interpreter **reads** your program and determines what each word means.
4. For example:
   - When Python sees the `print` function followed by parentheses `()`, it prints whatever is inside the parentheses.
   - Strings like `"Hello World"` are displayed in a different color in most editors because they are **string literals**, not code.

---

## Variables in Python

A **variable** is a name that refers to a value stored in memory.

### Example
```python
mySuperMessage = "Hello everyone, welcome to the Python course."
print(mySuperMessage)
```

**Output:**
```
Hello everyone, welcome to the Python course.
```

---

### Key Points About Variables
- **Definition:** A variable stores information that can be used and modified later.
- **Connection:** Every variable is connected to a **value**.
- **Rules:**
  1. Variable names can contain **letters**, **numbers**, and **underscores** (`_`).
  2. They **must** start with a **letter** or an **underscore**, **not** with a number.
  3. No spaces are allowed in variable names.
  4. Do not use **Python keywords** (reserved words) as variable names.
  5. Python is **case-sensitive** (`Message` and `message` are different).

✅ **Valid variable names:**
```python
message_1 = "Hello"
_message = "Hi"
greetingMessage = "Welcome!"
```

❌ **Invalid variable names:**
```python
1message = "Wrong"   # Starts with a number
message 1 = "Wrong"  # Contains a space
print = "Wrong"      # Uses a Python keyword (overrides the function)
```

---

## Best Practices for Variable Naming
- Use **descriptive** names so the purpose is clear.
- Use **snake_case** for variable names in Python:
```python
user_name = "Faisal"
account_balance = 5000
```
- Keep variable names **short but meaningful**.

---

## Understanding Data Types
Common data types you will work with in Python:
- **String** – Text data (`"Hello"`)
- **Integer** – Whole numbers (`42`)
- **Float** – Decimal numbers (`3.14`)
- **Boolean** – `True` or `False`
- **List** – Ordered collection (`[1, 2, 3]`)
- **Dictionary** – Key-value pairs (`{"name": "Faisal", "age": 22}`)

You can check the data type with the `type()` function:
```python
age = 22
print(type(age))  # <class 'int'>
```

---

## Summary
- Python interprets and runs `.py` files using the Python interpreter.
- The `print()` function displays text or variables on the screen.
- Variables store values and must follow **naming rules**.
- Python is **case-sensitive**.
- Understanding data types helps you store and manipulate data effectively.

---


**Author:** [FaisalKhan (0xBinaryOrbit)]  
**GitHub:** [0xBinaryOrbit](https://github.com/0xBinaryOrbit) 
