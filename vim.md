Vim commands

There really is a combination of running tmux and nvim commands together which is what you have to get used to.


I am currently using Lazyvim, it comes with many sensible defaults.
<Leader> b d - use this to close the current tab

### Common commands and actions

The idea behind this section is to record exactly the keystrokes you regularly use and the idea is 
that at some time the actions will become more natural and built into your muscle memory


#### Update dependencies in a package json file

- The package json file is open in nvim


#### Rename the current file
- press : key to bring up the command panel
- type file <new filename>



  

How to run javascript files directly without leaving the editing window.

:!{cmd} syntax

The ! (bang operator) says to vim execute a shell command
The % refers to the current file

TYPE: :!node %

# Verbs 
d: delete
c: change (overwrite)
y: yank (copy)
>: indent
<: unindent

# Actions
h,j,k,l: left, down, up, right
w: next word
b: previous word
0: start of line
$: end of line
i: inside (excluding the following character)
a: around (including the encasing characters)
