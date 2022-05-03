# Typescript

### Classes

There is a short hand to creating properties on a class.
Inside the constructor function arguments provide the keywords of public before each parameter and this does the this.property = argument call.

```javascript
  class SuperHero {
	 //This call below can be shortened to next below 
	  constructor(name: string, leve: number) {
              this.name = name;
	      this.level = level
	  }
          constructor(public name: string, public level: string)  
  }
```

Setting up React project for Typescript.

1) Use files with the esxtension .tsx (instead of .ts)
2) Use "jsx":"react" in your tsconfig's compilerOptions
3) Install the definitions for JSX and React into your project: (npm i -D @types/react @types/react-dom)
4) Import react into your .tsx files
