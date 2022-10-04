TEMPLATE TO COPY EVERY TIME

<details>
  <summary>QUESTION FOR ACTIVE RECALL</summary>
  ANSWER IN BULLET POINT
</details>

---

## in-built functions

For a full list of the built in functions go to [built-in](https://www.programiz.com/python-programming/methods/built-in)

<details>
  <summary>What two functions can you use to determine if a char is a digit or if a char is a text char?</summary>
  
  ```python
  for char in str:
     char.isalpha() # True or False
     char.isdigit() # True or False
  ```
</details>


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

## Useful libraries that can be imported

### random

```python
  import random
  random.choice() # pass in a list of items which will be randomly returned
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

#### Type conversions
---

*int* function rounds down an input either a string or float and will round value down.

*str* converts inputs to a string datatype

*hex* and *oct* *bin* are also functions that can be applied

*chr* and *ord* can be called on chars

##### Complex datatypes

call *list* function passing in a string will result in a list of chars of that string, also use *tuple* built-in function

calling *dict* needs a lsit of key-value pairs as tuples or a list of lists with two values in each sublist

Calling *set* on a string will cature all unique characters from that string, ignoring repeat chars









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


<details>
  <summary>What function will you use to iterate over two lists and add their values in a dict</summary>
  
    **zip** function, and here is an example:
    
    ```python
        count = [23, 45, 78, 12, 32]
        cars = ["BMW", "Merc", "Jaguar", "Volvo", "Nissan"]
        dict = {}
        for i,j in zip(cars, count):
            dict.update({i: j})
        print(dict)
    ```
  
</details>

---


Use the in command to see if a value is in a list

```python
my_car_list = ['Nissan Altima', 'Kia Soul', 'Kia Optima', 'Honda Civic']
print('Kia Soul' in my_car_list) # True
```
---
#### lists and copy and deepcopy

While you can use the copy and deepcopy functions from th copy package (import copy) you can also use the slicing operator shorthand to create a deep copy of the list.

```python
  new_list = old_list[:]
  
```

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

An empty dict is just instantiated as {}

```python
  bike_owners = {"James":"Ducati","Jacob":"BMW S 1000","Aiden":"Harley"}
  bike_owners["James"] # will return the value
  .keys() # gives you a list of the keys
  .values() # access all the values
  .get() # pass in a key and you get the value in return
  del bike_owners["James"] # will delete the key-value pair
  .copy() # makes an immutable copy
  .pop() # pass in the key and it returns the value and removes item from dict
  .popitem() # arbitrarily remove an item from the dict, cannot be certain which one
  .update # takes another list with key-value pairs which are merged, or replaced / update
  .clear() # removes all key-value pairs, leaving an empty # use del command to free up memory, var is gone
  
```

The **sorted** function also works on dicts, and passing a second argument reverse = True

If you need to return a tuple of key-value pairs use the **.items()** function






KeyError will be thrown if key doesn't exist. str in keys are case-sensitive

**NOTE** int and str can be used as keys, actually even bool. However, keys must be unique
The values can be complex data types, so storing lists in the values is allowed. Even dicts
So using [][] will look up multidimensional values (nested dictionaries)

#### sets

Sets are unordered, but unique
---

```python type(set_var) # set 
    .add(<value>) to add an item to the set
     len(pass in a set) # also works
    min and max functions also work
    .discard(element) # does nothing if it doesn't exist, silent
    .remove(element) # # throws an error if item does not exist
    .clear() # also works
    .union(comma seperated list of sets) # removes duplicates
    .intersection(comma seperated list of sets) # find common numbers and keep these, return them from the function call
    .difference(comma seperated list of sets) # only those that are not in either of the other sets
    {1,2,3}.isdisjoint(4,5,6) # True
    {1,2,3}.isdisjoint(1,5,6) # False
    {10,20}.isubset(20,10, 30,40) # True
    .issuperset()
```

When creating a set us the { } and it only has a value, so no key-value pair like a dict. As long as values are unique you can have any type stored or DS structures, except for a list. A tuple is immutable, a list, and dict in python is not.

an empty set can be created by calling 

```python
empty_set = set() 
```
### List conversions

Nested lists, i.e. a list in a list can be converted to a tuple. Gives you a tuple of lists.

``` python
    mylist = 
```

Nested lists of only two items in the nested lists *CAN* be mapped to a dict, by calling ```dict()``` constructor.


### Conditionals

#### Ternary operators

These are inline if else statements

``` python
   num = num - 20 if num > 20 else num + 20
```


## for..loops

You can use the **range** function to set up a determinate looping sequence.

```python
    val = range(20, 100, 4)
    # give range the start, end (exclusive) and step count if necessary, default is 1
    
    # reversed works on all collections, including strings
    list(reversed(val))
    
    
    
```

You can also pass **negative** indices to the above.

---
These values are the same notation used in iterables as in list **slices**
start, stop step

---


---

### Functions

Keyword arguments and positional arguments. Positional arguments must be specified first.

---
**some rules**

- Keyword arguments are often used in built-in functions, they are often default values in user defined functions.

- default arguments must come at the end

```python
sorted(num_list, reverse=True)

print("Alice", "Bob", sep="|")



```

---


#### Variable length arguments

---

```python
    def print_fn(*args): # note the * asterisk
      args_type = type(args) # tuple
```
This gives you powers to pass in a list but include the * in the invocation to spread the list.

Python offers another way to pass variable length arguments to a function
---

```python
def student_details(**kwargs): # packs the variables up as a dictionary
      print(type(kwargs)) # dictionary
      

```

To pass in a dictionary, se the ** to pass the dictionary in.



### Lambda functions

---

Functions are first class citizens

```python
# anoymous functions are lambdas

cube_of = lambda x: x * x * x

add = lambda x, y: x + y
mul = lambda x,y: x * y

# Note lambdas can be defined and invoked immediately

(lambda x: x + 10)(10) # 20

# handy sum function

(lambda *numbers: sum(numbers))(3,5,6,7)



```

Lambdas cannot have keywords or statements in the body
Lambdas are often used with filter function,


---

### Complex functions

#### Recursion

```python

import sys
sys.getrecursionlimit() # 3000
sys.setrecursionlimit(100) # to set a new recurison limit

```

- Recursive calls always need a solid base case(s) with a return statement,
- Make sure the return values in recursive call and base case match
- Recursive calls can often be formed through using while loops

```python

##### Fibonacci is a nice illustration of Python recursion in action

def fibonacci(number, fib_series):
  if number < 2:
  return
  
  l = len(fib_series)
  
  new_number = fib_series[l - 1] + fib_series[l - 2]
  
  fib_series.append(new_number)
  
  print("Series so far ", fib_series)
  
  fibonacci(number - 1, fib_series)

fibonacci(10, [0,1])

```
---

##### Generator functions
---

<details>
  <summary>What is an Iterator in Python?</summary>
  
  Any object that responds to the built-in next() function
</details>

---

<details>
  <summary>What is a generator function?</summary>
  
  - A function that is a simple way of creating iterators over a sequence
  - The function differs from normal, in taht the retun statement is replaced by yield command
  - The yield takes control of function
  - invoking the generator function creates a generator object
      - this is an iterator
      - The built in next function can take a generator object, and returns first up until first yield.
      - StopIteration Error is raised once all yield statements run
      - local variables inside a generator function maintain their state between function calls
    - generator functions are often used with for or while loops
    - You can also pass generator object to list()
    
  ---
  To generate infinite sequence
  ---
  ```python
    num = o
  while True:
    num += 1
    yield 2 ** num
  ```
  
  
  
  ---
</details>

#### Closures

Nested functions within outer functions.
That can be returned. Now invoking that function the inner function will be called.
Closures can access local variables.
They hold a reference to local state even after the outer function that dfines the local state no longer exists. (Backpack)

---























