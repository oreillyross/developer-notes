# Design patterns in Python

### SOLID 
  - Single responsibility principle
  - Open closed principle
  - Liskovs Substitution principle
  - Interface Segragation principle
  - Dependency inversion principle
  
#### Single Responsibility Principle 

A class ought to have one and only one responsibility. Keep your component as granular as possible. Do one thing and do it well. 
Violating this principle makes chaning or extending the class very difficult. 

#### Open closed principle

Code should be open for extension, but closed for modification. Once you have written a class, try to leave it alone, do not add new functionality. No new member 
variables, methods, or interfaces. Keep it as a guideline, bug fixes and some imporovements are ok.

To make new functionality, use your class in new ways. Use extension, not modification. Extension refers to creating a derived class. Base class should not be changed.
To change how something is accomplished extend the original class. Inheritance setups a has a relationship. Delegation creates a new class with new functionality, and you 
delegate from the old class. Composition, structure your original code in such as a way as you have pluggable components, plug and play.

Choose three ways:
1. Inheritance - template design pattern
2. Delegation - observer, chain of responsibility (state changes etc)
3. Composition - If you take in member variables to determine behaviour - strategy pattern

You can use multiple ways together to achieve the open/closed principle effect.


1. Interface segregation principle
Interface is effectively a contract that binds the class to implmenting certain beahviours
Do not mix too many different behaviours

2. Dependency Inversion principle
Program to an interface not an implementation
Depend on abstractions, abstract base classes, a method without an implementation, exposing an interface.
Never make any assumptions about the inside / implementation
   


#### Principle of least knowledge
Only talk to friends not friends of friends (strangers) - Law of Demeter
promotes loose coupling
friends include params of methods, objects, global vars

#### The hollywood principle
Dont call us we will call you.
High level object to low level object, using events
Low level objects should not communicate up, like pinging etc.
Observer design pattern is an implementation

#### The principle of single responsibility

keep classes focused in what they do.



#### Liskovs substitution principle
- The inheriting or derived class from a Base class should be predicable in behaviour.
- The interface contract is the same, i.e. you can subsititue the base calss with derived flag.
- Breaking this contract would happen where the derived class methods change their parameters, i.e. its invoked differently.
- The api of both classes should ideally match, then you are observing or respecting Liskovs substitution principle.
- If you start having isinstance checks in your derived methods this should be a RED flag that you are breaking this principle.
- 


#### Interface Segragation principle
- Clients should not have to implement bulky interfaces
- Keep the interface focussed and granular
- By declaring custom functions, you can pass a derived class through. 

```python 
class Eagle(Flying, Feeding):

  # here you can overide the methods that will inherit from the inherited interfaces
  
  # call functions
  eat_food(eagle)
  
  # or another example using a base class
  class Mammal:
    def aerial(self):
      raise NotImplementedError
      
   # then a derived class
   class Human(Mammal):
    def aerial(self):
      pass
      # because humans cant fly
    
```

#### Dependency Inversion Principle

- Clients should only depend on abstractions and not on implmentation
- Higher level modules should not depend on lower level modules



#### Global Object pattern

Module is a logical unit that can be imported and consists of functions, variables.

Use __ at beginning to indicate its a private label. 


#### Factory and Abstract pattern

Seperate the creation from their use, can be class creation or object creation.

class creation use inheirtence
Object creation often uses delegation

---

 ```python

class Product:
  def __init__(self, name, price):
    self.__name = name
    self.__price = price
    
  def get_price(self):
     return self.__price
  
 class AppleIpad(Product):
 
  def __init__(self, generation):
    Product.__init__(self, 'AppleIpad')


class ProductFactory()

  @staticmethod
  def create(item_name, *args):
    if item_name == "AppleIpad":
      return AppleIpad("gen2")
      
  


 ```
## Structural design patterns
  focus on how classes and components can be composed to form new complex structures
### Adapter pattern

- It is a structural object pattern
- Adapters let classes work together that couldn't otherwise because of incompatible interfaces
- It works by creating a third class that is the adapter and it inherits from the common interface
- This then must __init__ and take the old legacy class and store a reference to it locally
- All expected contract methods, i.e. the shape of interface, must then delegate the calls to legacy 
- methods.

### decorator pattern
- Use this when you need to add behaviour at runtime
- Inheritence will not work as it is static
- Wrap each object with another. derived from abstract classes
- Think of the application as wrapping functions around functions, like the HOC pattern in JS

### Facade pattern
- A class that hides a complex system
- makes the subsystem easier to use, unified interface to a more complex sub interfaces
- decouple complex, granular systems from clients
- **watch out**: should not be only way to access system
- can be a bunch of microservies, facade stands infront, hides complexity.
