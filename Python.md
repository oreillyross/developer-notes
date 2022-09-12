## in-built functions

For a full list of the built in functions go to [built-in](https://www.programiz.com/python-programming/methods/built-in)

### print 

```python
print("Hello World!") # Hello World!
```

### len

```python
len("Hello World!") # 13 
```

### abs

```python
abs(-17) # 17
```


### type

```python
type(17.5) # float 
type("23") # string
```

### round

```python
round(17.6) # 18
```
### max or min

```python
  max(2,5,7,71,3) # 71
  min(-2,3,5,33) # -2
```

## Variables in python

Containers that hold values

```python
    salary = 24000
```
## Types in Python

### primitive types in python are:

- bool # True False
You can use logical operators here. **and, or **
  - bool is the type

- str # ""
  -   

- int, float # 5 , 5.6
  -   int is a built in class, of int
  -   float is a built in class of float
  -   complex numbers can be invoked by appending j to number 

- NoneType

- binary types
  - use 0b to prepend the numbers 0 or 1
  - 0b111 = 7

## Assigning values to variables

string variable assignments are immutable by default. Whatever the value was at the time of assignment.

### muliple assignments, shortcut

```python
x = y = z = "Python"

# one can also assign multiple values

x,y = 5, "Python" # x = 5, y = "Python"
```

### Comparison operators

== # equal to
>= <= > < > # greater than less than


### Working with strings in python

- use single or double quotes
- use three double quotes, """ python """
- string can be multiplied by an int # "python" * 3 will result in "python python python"

use the builtin ```input() ``` function to get iput from the user. the result will be the string value the user provides.

use the \ escape character before the value to ignore the meaning of the char
so \" will ignore the " inside a " " value
"Hello \"There\" "

You can also use \n - for new line, or use the triple quote for multi lines
\t for a tab char


Use the f prefix to inject variables into a string

```python
my_var = "barks
print(f'A dog {my_var}!' # a dog barks
```
alternatively call the .format function onthe string class


















