# Typescript

### Classes

#### Shorthand 
There is a short hand to creating properties on a class.
Inside the constructor function arguments provide the keywords of public before each parameter and this does the this.property = argument call.

```javascript
  class SuperHero {
    //This call below can be shortened to next below 
    constructor(name: string, leve: number) {
      this.name = name;
      this.level = level
     }
     
     // This is the shorthand, note the public keyword used and empty braces
     constructor(public name: string, public level: string) {}  
  }
```
---

### Assertions

There are two ways to write the assertion syntax,
the first is using the as keyword. Use in JSX files

```// note the use of the brackets to isolate object then typecast it.
  (someObject as Another).property
```

the other syntax is angle brackets and it goes before the value or object
```
  <Another>someObject
```

Setting up React project for Typescript.

1) Use files with the esxtension .tsx (instead of .ts)
2) Use "jsx":"react" in your tsconfig's compilerOptions
3) Install the definitions for JSX and React into your project: (npm i -D @types/react @types/react-dom)
4) Import react into your .tsx files


#### Questions for active recall
1. In a class constructor can the syntax be shortened to avoid typing out the this.property... every time? [answer](#shorthand) 
2. How can one get around type assertions using angle brackets in JSX files? [answer](#assertions)  