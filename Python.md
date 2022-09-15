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

## List operations and common hacks
---

Handy **slicing syntax** to reverse a list

```python
my_car_list = ['Nissan Altima', 'Kia Soul', 'Kia Optima', 'Honda Civic']
print(my_car_list[::-1])
```
---
  <details>
   <summary markdown="span">Is the list end index inclusive or exclusive?</summary>
   
    It is exclusive.
  
  </details>

---

Use the in command to see if a value is in a list

```python
my_car_list = ['Nissan Altima', 'Kia Soul', 'Kia Optima', 'Honda Civic']
print('Kia Soul' in my_car_list) # True
```
---



#### Working with strings as lists

You can use destructuring, but you have to be exact with your variables. Use a _ to represent a placeholder

```python
a,b,c,d,e = "World"
print(a,b,c)
val = input("What you say? ") # input is a handy function to take input from the user
print("you said ", val)
```

*negative indexes* also work well in strings.

the **del** keyword should come in handy to free up variable assignments to large lists no longer being used.

#### slicing operations on strings

the square brackets **[ startidx : endidx ]** are used to index into a string. end index is exclusive

Use the negative step size value to reverse over the list, using [::-1] reverses the list

#### string functions

```python
.startswith()
.endswith() # pass in a char to check
.count() # count how many chars you pass in the char to check, case matters
.upper()
.find() # returns the index position of a char or string passed into the function
.index() # same as above, but will error is substr not found, as oppose to the -1 which gets returned from find()
.split() # split a string on a char, str -> list
.join) # is the opposite of split, but on lists -> string
```

#### Tuples and immutablity


> Tuples once created  cannot be changed or updated.
> list items within a tuple howver can be modified.

The zip function is a very useful function working with tuples.
the type of tuple is an **object**
zip return a collection of items. pass in two tuples.

- HANDY TRICK: 
---
To return the original tuples, call the zip function and prepend an asterisk to the passed in tuple value, this will be assigned to the left hand side as two tuple variables. zip also works on lists., after calling zip, pass its result to the **list*** constructor to get a list of zipped tuples., or a **dict**, JSON ready.

```python
   tuple_x, tuple_y = zip(*zipped_tuple)
```

- create a tuple use rounded brackets as oppose to square brackets.
- you can create a tuple using the assignemnt to comma separated values.
  -   tuples can be nested, or lists can be nested inside tuples
  -   accessing fields in a tuple similar to list/string indexing
  -   nested square bracket notaiton can be used for multi-dimensional lists, tuples
  -   like in a list you can also pass a tuple to the set() constructor


#### List types

Ordered collection of elements.
- created using [] brackets, can contain elements of different datatypes

#### Dictionary
- key-value pair, like an object in javascript
- JSON ready
- key is always a string ???
- ``` type(dictionary_var) # dict```

#### sets
- sets are unordered, but unique
- ``` type(set_var) # set ```






















