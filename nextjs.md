### NextJS version 13

Using server components now means less client side javascript. 

NextJS best practice is to use Typescript as indicated in the create-next-app CLI starter options.

The layout.tsx page then has the type children typed as a React.ReactNode

In the RootLayout file that is default exported, return the default 
```html
<html> tags surrounding <body> tags and use the javascript jsx {children} escaped
```
So essentially you are passing in the children prop to the function typed as React.ReactNode

[return to toc](README.md)
