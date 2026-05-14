# Number Pattern Generator 🔢

A beginner-friendly Python project that generates a sequence of numbers from `1` up to a given positive integer using loops and string manipulation.

This project was built as part of Python programming practice to strengthen understanding of:

* Functions
* For loops
* The `range()` function
* String concatenation
* Input validation
* Conditional statements

---

## 📖 Project Overview

The `number_pattern()` function accepts a positive integer `n` and returns a string containing all numbers from `1` to `n`, separated by spaces.

### Example

```python id="sq5l20"
number_pattern(4)
```

### Output

```python
1 2 3 4
```

---

## 🧠 How the Algorithm Works

The program follows these steps:

1. Creates an empty string called `pattern`
2. Uses a `for` loop to iterate from `1` to `n`
3. Converts each number into a string
4. Adds each number to the pattern with a space
5. Removes the extra trailing space using `.strip()`
6. Returns the final formatted string

---

## 📂 Project Code

```python
# Define the function
def number_pattern(n):
   
   # Initialize an empty string to build the pattern 
    pattern = ""

    # Loop from 1 up to n (inclusive)
    for number in range(1, n + 1):

        # Add each number and a space to the string
        pattern += str(number) + " "
        
    # Remove the extra space at the end of the string
    return pattern.strip()

    # Check if the argument in NOT an integer
    if not isinstance(n, int):
        return "Argument must be an integer value."
	
    # Check if the integer is less than 1
    if n < 1:
        return "Argument must be an integer greater than 0."

    # Remove the extra space at the end of the string
    return pattern.strip()


# Test the function with a valid input
print(number_pattern(4))
```

---

## ⚠️ Note About the Current Code

The validation checks in the current program appear **after** the `return` statement, meaning they will never execute.

For proper validation, the checks should come **before** the loop and before returning the result.

---

## ✅ Improved Version

```python
def number_pattern(n):

    # Check if the argument is NOT an integer
    if not isinstance(n, int):
        return "Argument must be an integer value."

    # Check if the integer is less than 1
    if n < 1:
        return "Argument must be an integer greater than 0."

    # Initialize an empty string
    pattern = ""

    # Loop from 1 to n
    for number in range(1, n + 1):
        pattern += str(number) + " "

    # Remove trailing space
    return pattern.strip()
```

---

## ▶️ Example Usage

```python
print(number_pattern(5))
```

### Output

```python
1 2 3 4 5
```

---

## 🛠 Technologies Used

* Python 3

---

## 🎯 Learning Objectives

This project helps beginners understand:

* Python functions
* For loops
* The `range()` function
* String methods
* Data validation
* Basic algorithm design

---

## 🚀 How to Run the Project

### Clone the Repository

```bash
git clone https://github.com/ikwukao/number_pattern_generator.git
```

### Navigate Into the Folder

```bash
cd number_pattern_generator
```

### Run the Program

```bash
python main.py
```

---

## 📚 Ideal For

* Python beginners
* freeCodeCamp learners
* Coding interview preparation
* Backend engineering practice
* Algorithm practice

---

## 📄 License

This project is open-source and free to use for educational purposes.

---

## Program Output

![Number Pattern Generator output](./img/number_pattern_generator.png)
