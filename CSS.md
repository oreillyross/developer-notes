# CSS 

### Defaults

```css
* {
  box-sizing: border-box;
}

/* This is a good default to prevent img overflowing content when screen size shrinks */
img {
   max-width: 100%
}
```
### ems and rems

Use rems for all font sizing
Use ems for everything else, but very IMPORTANT to know that the em references that elements font-size, and not the parents.

### Viewport units

vh, vw, vmax, vmin

view port height and viewport width is the whole viewport (100%) of viewport
Mobile views can cause issues, use @mediaqueries toifx overflowing

use this on width and height properties and padding.
width: 100vw
height: 80vh (80%)
padding: 10vh, 0

Settinga font size using vw is super useful. Use it mainly for titles and not paragraph text
font-size: 8vw // makes things very responsive, makes font grow without media queries
font-size: 8vmin // compares the smallest of the width and height and bases the sizing on that, can stop text from growing and growing as width increases

In VsCode use emmet and type ! [tab]

to get an html5 template filled in






