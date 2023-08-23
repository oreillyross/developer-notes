### NextJS version 13

Using server components now means less client side javascript. 

NextJS best practice is to use Typescript as indicated in the create-next-app CLI starter options.

The layout.tsx page then has the type children typed as a React.ReactNode

In the RootLayout file that is default exported, return the default 
```html
<html> tags surrounding <body> tags and use the javascript jsx {children} escaped
```
So essentially you are passing in the children prop to the function typed as React.ReactNode

---
#### Client side rendering
*use* the client side directive `"use client"`

> NOTE
>An anti patttern of passing a server component to a client rendered component is to use a concept known as *slot*
>This works by passing the `slot` server component as a child to the client rendered function as a prop


[return to toc](README.md)
