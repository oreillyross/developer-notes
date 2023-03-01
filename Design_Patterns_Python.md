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









  
