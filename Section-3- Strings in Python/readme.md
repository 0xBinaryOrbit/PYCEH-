# Python Basics – Assignment, Strings, and Formatting

In this section, you will learn:
- How the **assignment operator** works in Python.
- How to work with **strings** and their methods.
- How to use **f-strings** for formatting.
- How to handle **newlines, tabs**, and string manipulation.
- The difference between **single** and **double quotes**.

---

## 1. Understanding the Assignment Operator (`=`)

In mathematics, `=` means **"is equal to"**, but in programming, it means **"assign the value"**.

### Example
```python
userAge = 19
```

This means:
* Take the value **19** (right side)
* Assign it to the variable **userAge** (left side)

---

### More Example
```python
a = 5
b = 10
a = b

print("a:", a)
print("b:", b)
```

**Output:**
```
a: 10
b: 10
```

**Explanation:**
1. Initially:
   * `a` = 5
   * `b` = 10
2. The statement `a = b` assigns **b's value (10)** to `a`.
3. Now both variables store the value **10**.

---

## 2. Strings in Python

A **string** is a sequence of characters enclosed in quotes.

Examples:
```python
"Hello World"
'Python is fun'
```

* Strings can be enclosed in **single** (`'`) or **double** (`"`) quotes.
* This flexibility allows quotes and apostrophes **inside** strings.

---

## 3. String Methods

Python strings have **methods** that help you format or manipulate text.

### Changing Case
```python
name = "this is the world best python course"
print(name.title())   # Title Case
print(name.upper())   # UPPERCASE
print(name.lower())   # lowercase
```

**Output:**
```
This Is The World Best Python Course
THIS IS THE WORLD BEST PYTHON COURSE
this is the world best python course
```

**Explanation:**
* `.title()` → Capitalizes the first letter of each word.
* `.upper()` → Converts to uppercase.
* `.lower()` → Converts to lowercase.

---

### Other Useful String Methods

| Method           | Description                    | Example                                             |
| ---------------- | ------------------------------ | --------------------------------------------------- |
| `.strip()`       | Removes spaces from both ends  | `"  hello  ".strip()` → `"hello"`                   |
| `.lstrip()`      | Removes spaces from the left   | `"  hello".lstrip()` → `"hello"`                    |
| `.rstrip()`      | Removes spaces from the right  | `"hello  ".rstrip()` → `"hello"`                    |
| `.replace(a, b)` | Replace text                   | `"Hi John".replace("John", "Alice")` → `"Hi Alice"` |
| `.count(x)`      | Count occurrences              | `"banana".count("a")` → `3`                         |
| `.find(x)`       | Find index of first occurrence | `"banana".find("n")` → `2`                          |

---

## 4. Using F-Strings

F-strings allow inserting variables into strings easily.

Example:
```python
car_make = "BMW"
car_model = "5er 2014"
car = f"{car_make} {car_model}"
print(car)
```

**Output:**
```
BMW 5er 2014
```

**Explanation:**
* `f"{}"` tells Python to evaluate variables inside `{}`.
* This is cleaner than using `+` for string concatenation.

---

## 5. Playing with Newlines and Tabs

You can control spacing and formatting in strings using special characters:

| Character | Meaning              |
| --------- | -------------------- |
| `\n`      | Newline (line break) |
| `\t`      | Tab (indentation)    |

Example:
```python
print("Hello\nWorld")
print("Python\tRocks")
```

**Output:**
```
Hello
World
Python	Rocks
```

---

## 6. String Manipulation

You can combine strings in multiple ways:

### Concatenation
```python
first_name = "Faisal"
last_name = "Khan"
full_name = first_name + " " + last_name
print(full_name)
```

**Output:**
```
Faisal Khan
```

### Repetition
```python
print("Hi! " * 3)
```

**Output:**
```
Hi! Hi! Hi!
```

---

## 7. Single vs Double Quotes

Both **single quotes** (`'`) and **double quotes** (`"`) work for strings.

### Example:
```python
message1 = 'Hello World'
message2 = "Hello World"
print(message1)
print(message2)
```

They behave the same, but double quotes are often useful if your string contains an apostrophe:

```python
quote = "It's a beautiful day!"
print(quote)
```

If you use single quotes, you need to escape the apostrophe:
```python
quote = 'It\'s a beautiful day!'
print(quote)
```

---

## Summary
* `=` assigns a value, it does not mean equality.
* Strings can be single or double quoted.
* String methods help with formatting and cleaning data.
* F-strings make combining variables simple.
* Newlines (`\n`) and tabs (`\t`) improve formatting.
* String manipulation includes concatenation and repetition.

---

**Author:** [FaisalKhan (0xBinaryOrbit)]  
**GitHub:** [0xBinaryOrbit](https://github.com/0xBinaryOrbit) 
