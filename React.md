### React

. https://jsfiddle.net/reactjs/69z2wepo/[React Base fiddle (jsx)]


Always try to use stateless components and write idiomatic React. Be a pragmatic 
programmer: go for stateless components where possible, but state is there to 
be used when you really need it.

``` code

const FunctionalTest = (props) => {
    return {props.message};
};

```


=== Why the parens within the render function / method.

Why do we need the parentheses around the return statement? 
This is because of JavaScript's automatic semicolon insertion. 
Without the parentheses, JavaScript would ignore the following lines and 
return without a value. If the JSX starts on the same line as the return, 
then parentheses are not needed.

=== When to use bind 

Advice from .https://www.reddit.com/r/reactjs/comments/54xnao/fat_arrow_vs_autobind_vs_bindbindbindbindbind/d85wj0l/ 
[Dan Abramov]

You do, however, need to bind functions that you take off this. So if you write 
onChange={this.handleChange}, you get an unbound function unless you bind it
yourself. In practice this means that with React, you generally only want to 
bind event handlers and timer/interval/AJAX callbacks. You don’t need to bind 
render or React lifecycle methods. 

``` code Bind pattern inside a class for react component
class Example extends Component {
  constructor(props) {
    super(props);
    this.handleThing = this.handleThing.bind(this);
  }

  handleThing () {
    // ...
  }
}

```

###Context

What is context, and what use is it in React?

Context is a mechanism that allows you to pass data through the app without prop drilling (passing data through each components props to get deeper into component tree.

It is useful for global state such as theming, authenticated users etc.

Alternatives to using context is to consider using the inversion of control and component composition patterns including the render prop pattern if the child component needs to communicate with the parent before rendering. 





How do you set it up?

Use the react utility function React.createContext() which returns a Context component. Wrap the Context.Provider component around the React elements you want context to be available on, it takes a prop called value which can be what you pass down. 

Deep down in your component tree you can call on the next available provider up in the tree for its stored state using the useContext hook.




=== Designing from Wireframes (taken from Manav Sehgal book ReactSpeedCoding)

The steps followed to design React components from a wireframe can be outlined
like so.
---

1. Scenario ideal for creating custom, non-standard, or complex UI controls.
2. Create wireframe using boxes for elements, layout, composition, and arrows
for properties, state, and events.
3. Split individual elements of the wireframe into own style classes. Follow
styles structure from wireframe.
4. Use Flexbox to order elements, align element layout, compose element
hierarchy.
5. Create HTML/DOM render matching your wireframe, using the new styles.
6. Define properties to handle component data required for each element.
7. Add default property data fixtures if creating a demo component.
8. Create event handler methods and bind these in constructor. Call these
methods from element event handlers.
9. Specify component state based on event driven UI state change.
10. Import and render component in an owner component.

=== Lifecycle meothds for class based components

Overall the mounting process has 4 lifecycle methods. They are invoked in the following order:
• constructor()
• componentWillMount()
• render()
• componentDidMount()

But what about the update lifecycle of a component that happens when the state or the props change?
Overall it has 5 lifecycle methods in the following order:

• componentWillReceiveProps()
• shouldComponentUpdate()
• componentWillUpdate()
• render()
• componentDidUpdate()

Last but not least there is the unmounting lifecycle. It has only one lifecycle method: componentWillUnmount().

=== React Component props interface - validating your props

. types of props:

* PropTypes.array
* PropTypes.bool
* PropTypes.func
* PropTypes.number
* PropTypes.object
* PropTypes.string

Use isRequired to enforce this.

Button.propTypes = {
onClick: PropTypes.func.isRequired,
className: PropTypes.string,
children: PropTypes.node.isRequired,
};

Advanced React Patterns

* Context module Functions pattern  // taken from Kent C Dodds Epic React course 


