# React and Javascript testing

### Install
- npm install @testing-library/react
- npm install jest
- Jest by Orta vscode extension

### Setup
- import "@testing-library/jest-dom" // this will give you access to the expect matchers (toBe... etc)

### React testing library concepts
- Make the distinction between the initial imports of screen and render from "@testing-library/react" and the objects they return. What this means is that the __screen__ object is like a representation of the document object, but has all of the RTL (or jest-dom TODO: check this is true) helper functions to get chunks of the DOM for further testing and assertions. {__container__} destructured from the __render__ method where you pass it a React component is like a regular DOM node where you can also use functions like querySelector() etc...
- The helper function, desctructerd directly from render method, called debug. can be called with no arguments or can be called with a dom node queried by the screen object.

```javascript
import {render} from "@testing-library/react"

describe(...() => {
  it( ... () => {
    const {screen, debug} = render(<WhateverComponent/>);
  })
})

const pieceOfTheDOM = screen.querySelector('a');
debug(pieceOfTheDOM)

expect(pieceOfTheDOM).toBe... etc etc

```

Whatever test runner and assertion library you use, a failing unit test should tell you at a glance:

. Which component is under test?
. What is the expected behavior?
. What was the actual result?
. What is the expected result?
. How is the behavior reproduced?

#### Useful libraries to use

Functional testing
.Nightwatch.js

Unit testing
.Tape.js

