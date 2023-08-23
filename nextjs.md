### NextJS version 13

Using server components now means less client side javascript. The app router is the new way of creating server generated html content as oppose to the former process of having a pages router which would have client side javascript and jsx which uses getServerSideProps() and getStaticProps() to inject content.

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

Passing props from server to client is known as serialization, which means the content to be displayed needs to be serializable. So things like function and date objects cannot simply be passed down through the network boundary. 

*Poisoning* - This occurs when server side code gets into client side code. 

To use environment variables in client side code you need to decalre them publiccly by appending the NEXT_PUBLIC to the env name. 

To avoid running into problems you can flag these issues at development compile time, by using the two respective libraries. 
` import server-only` or `import client-only` and for example if you try to call **window** object in the context of a server environment. That is to say on the server side of the network boundary it will give an error.

#### Sharing data in server components
One can use the **global singletons** pattern, so export a const reference to the shared resource such as a db ref. And then server components can use them without using things like context. 



[return to toc](README.md)
