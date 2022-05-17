# Typescript

## Setup and running typescript

__tsc usage__

You can run ``` tsc index.ts && node index.js ``` to run a sort of repl of your code. A better way is to use the npm package __tsc-watch__ and --onSuccess flag to then run js file ```tsc-watch --onSuccess "node index.js"```

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

### Optional chaining operator

- this consists of a ? and then a dot ?.
- Can be chained on an object multiple depths

### Nullish coalescing operator

- this is indicated with two ?, so ?? 
- it evaluates a left hand side and a right hand side of the ??
- the nullish coalescing operator can be used in conjunction with optional chaining operator

### Defensive coding using typescript
- Use unknown instead of any when typing up any unknown parameters.
- Using unknown this way, typescript then forces you to get dfensive about your values inside the function
- For example using typeguards up front such as typeof checks, and early return or throw Error
- Using an assert utility function you need to pass keyword asserts after function call to assert that function either errors or if it returns from function call in control flow it is assumed true.
  ```typescript
    function assert(condition: boolean) : asserts condition {
      if ()
    }
  ```

#### Questions for active recall
1. In a class constructor can the syntax be shortened to avoid typing out the this.property... every time? [answer](#shorthand) 
2. How can one get around type assertions using angle brackets in JSX files? [answer](#assertions)  