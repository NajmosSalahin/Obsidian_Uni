---
title: Python cheatsheet
course:
type: academic
status: in-progress
topics:
  - python
semester: "1.2"
priority: high
tags:
  - 
created: 2025-09-29
updated: 2025-09-29
related:
  -
---
## Math Operators

From **highest** to **lowest** precedence:

| Operators | Operation         | Example         |
| --------- | ----------------- | --------------- |
| \*\*      | Exponent(Square)  | `2 ** 3 = 8`    |
| %         | Modulus/Remainder | `22 % 8 = 6`    |
| //        | Integer division  | `22 // 8 = 2`   |
| /         | Division          | `22 / 8 = 2.75` |
| \*        | Multiplication    | `3 * 3 = 9`     |
| \-        | Subtraction       | `5 - 2 = 3`     |
| +         | Addition          | `2 + 2 = 4`     |

Examples of expressions:

```python
>>> 2 + 3 * 6
# 20

>>> (2 + 3) * 6
# 30

>>> 2 ** 8
#256

>>> 23 // 7
# 3

>>> 23 % 7
# 2

>>> (5 - 1) * ((7 + 1) / (3 - 1))
# 16.0
```

## Augmented Assignment Operators

| Operator | Equivalent |
| --- | --- |
| `var += 1` | `var = var + 1` |
| `var -= 1` | `var = var - 1` |
| `var *= 1` | `var = var * 1` |
| `var /= 1` | `var = var / 1` |
| `var //= 1` | `var = var // 1` |
| `var %= 1` | `var = var % 1` |
| `var **= 1` | `var = var ** 1` |

Examples:

```python
>>> greeting = 'Hello'
>>> greeting += ' world!'
>>> greeting
# 'Hello world!'

>>> number = 1
>>> number += 1
>>> number
# 2

>>> my_list = ['item']
>>> my_list *= 3
>>> my_list
# ['item', 'item', 'item']
```

## Walrus Operator

The Walrus Operator allows assignment of variables within an expression while returning the value of the variable

Example:

```python
>>> print(my_var:="Hello World!")
# 'Hello world!'

>>> my_var="Yes"
>>> print(my_var)
# 'Yes'

>>> print(my_var:="Hello")
# 'Hello'
```

The *Walrus Operator*, or **Assignment Expression Operator** was firstly introduced in 2018 via [PEP 572](https://peps.python.org/pep-0572/), and then officially released with **Python 3.8** in October 2019.

Syntax Semantics & Examples

The [PEP 572](https://peps.python.org/pep-0572/) provides the syntax, semantics and examples for the Walrus Operator.

## Data Types

Python has nine core built-in data types that cover almost everything you’ll need:

| Data Type | Examples | Description |
| --- | --- | --- |
| **Numbers** |  |  |
| [`int`](https://www.pythoncheatsheet.org/builtin/int) | `-2, -1, 0, 1, 2, 3, 4, 5` | Whole numbers (integers) |
| [`float`](https://www.pythoncheatsheet.org/builtin/float) | `-1.25, -1.0, -0.5, 0.0, 0.5, 1.0, 1.25` | Numbers with decimal points |
| [`complex`](https://www.pythoncheatsheet.org/builtin/complex) | `2+3j, complex(1, 4)` | Numbers with real and imaginary parts |
| **Text** |  |  |
| [`str`](https://www.pythoncheatsheet.org/builtin/str) | `'a', 'Hello!', "Python"` | Text and characters |
| **Boolean** |  |  |
| [`bool`](https://www.pythoncheatsheet.org/builtin/bool) | `True, False` | True or False values |
| **None** |  |  |
| `NoneType` | `None` | Represents “no value” or “nothing” |
| **Collections** |  |  |
| [`list`](https://www.pythoncheatsheet.org/builtin/list) | `[1, 2, 3], ['a', 'b', 'c']` | Ordered, changeable collections |
| [`dict`](https://www.pythoncheatsheet.org/builtin/dict) | `{'name': 'Alice', 'age': 30}` | Key-value pairs |
| [`tuple`](https://www.pythoncheatsheet.org/builtin/tuple) | `(1, 2, 3), ('a', 'b')` | Ordered, unchangeable collections |
| [`set`](https://www.pythoncheatsheet.org/builtin/set) | `{1, 2, 3}, {'a', 'b', 'c'}` | Unordered collections of unique items |

### Quick Examples

```python
# Numbers
age = 25                    # int
price = 19.99              # float
coordinate = 2 + 3j        # complex

# Text
name = "Alice"             # str

# Boolean
is_student = True          # bool

# None
result = None              # NoneType

# Collections
scores = [85, 92, 78]      # list
person = {'name': 'Bob', 'age': 30}  # dict
coordinates = (10, 20)     # tuple
unique_ids = {1, 2, 3}     # set
```

For a comprehensive guide with visual examples and detailed explanations of when to use each type, see: [Python Data Types: A Visual Guide for Beginners](https://www.pythoncheatsheet.org/blog/python-data-types).

## Concatenation and Replication

String concatenation:

```python
>>> 'Alice' 'Bob'
# 'AliceBob'
```

String replication:

```python
>>> 'Alice' * 5
# 'AliceAliceAliceAliceAlice'
```

## Variables

You can name a variable anything as long as it obeys the following rules:

1. It can be only one word.
```python
>>> # bad
>>> my variable = 'Hello'

>>> # good
>>> var = 'Hello'
```
1. It can use only letters, numbers, and the underscore (`_`) character.
```python
>>> # bad
>>> %$@variable = 'Hello'

>>> # good
>>> my_var = 'Hello'

>>> # good
>>> my_var_2 = 'Hello'
```
1. It can’t begin with a number.
```python
>>> # this wont work
>>> 23_var = 'hello'
```
1. Variable name starting with an underscore (`_`) are considered as “unuseful”.
```python
>>> # _spam should not be used again in the code
>>> _spam = 'Hello'
```

Inline comment:

```python
# This is a comment
```

Multiline comment:

```python
# This is a
# multiline comment
```

Code with a comment:

```python
a = 1  # initialization
```

Please note the two spaces in front of the comment.

Function docstring:

```python
def foo():
    """
    This is a function docstring
    You can also use:
    ''' Function Docstring '''
    """
```

## The print() Function

The `print()` function writes the value of the argument(s) it is given. \[…\] it handles multiple arguments, floating point-quantities, and strings. Strings are printed without quotes, and a space is inserted between items, so you can format things nicely:

```python
>>> print('Hello world!')
# Hello world!

>>> a = 1
>>> print('Hello world!', a)
# Hello world! 1
```

### The end keyword

The keyword argument `end` can be used to avoid the newline after the output, or end the output with a different string:

```python
phrase = ['printed', 'with', 'a', 'dash', 'in', 'between']
>>> for word in phrase:
...     print(word, end='-')
...
# printed-with-a-dash-in-between-
```

### The sep keyword

The keyword `sep` specify how to separate the objects, if there is more than one:

```python
print('cats', 'dogs', 'mice', sep=',')
# cats,dogs,mice
```

## The input() Function

This function takes the input from the user and converts it into a string:

```python
>>> print('What is your name?')   # ask for their name
>>> my_name = input()
>>> print('Hi, {}'.format(my_name))
# What is your name?
# Martha
# Hi, Martha
```

`input()` can also set a default message without using `print()`:

```python
>>> my_name = input('What is your name? ')  # default message
>>> print('Hi, {}'.format(my_name))
# What is your name? Martha
# Hi, Martha
```

It is also possible to use formatted strings to avoid using.format:

```python
>>> my_name = input('What is your name? ')  # default message
>>> print(f'Hi, {my_name}')
# What is your name? Martha
# Hi, Martha
```

## The len() Function

Evaluates to the integer value of the number of characters in a string, list, dictionary, etc.:

```python
>>> len('hello')
# 5

>>> len(['cat', 3, 'dog'])
# 3
```

Test of emptiness

Test of emptiness of strings, lists, dictionaries, etc., should not use `len`, but prefer direct boolean evaluation.

Test of emptiness example:

```python
>>> a = [1, 2, 3]

# bad
>>> if len(a) > 0:  # evaluates to True
...     print("the list is not empty!")
...
# the list is not empty!

# good
>>> if a: # evaluates to True
...     print("the list is not empty!")
...
# the list is not empty!
```

## The str(), int(), and float() Functions

These functions allow you to change the type of variable. For example, you can transform from an `integer` or `float` to a `string`:

```python
>>> str(29)
# '29'

>>> str(-3.14)
# '-3.14'
```

Or from a `string` to an `integer` or `float`:

```python
>>> int('11')
# 11

>>> float('3.14')
# 3.14
```