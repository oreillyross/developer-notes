Vim commands

There really is a combination of running tmux and nvim commands together which is what you have to get used to.


I am currently using Lazyvim, it comes with many sensible defaults.
<Leader> b d - use this to close the current tab

### Common commands and actions

The idea behind this section is to record exactly the keystrokes you regularly use and the idea is 
that at some time the actions will become more natural and built into your muscle memory

#### Moving around
- Ctrl + f = moves down a page

- Ctrl + b = moves up a page

- To move half a page down Ctrl + d
- To move half a page up Ctrl + u

#### Update dependencies in a package json file

- The package json file is open in nvim
- type Ctrl + a : opens a command lnie at bottom
- type split-window -h
- Use Ctrl + a o to toggle windows
- OR type Ctrl + a q then quickly either 1, 2, or 3

  ##### How to toggle between Neo-tree and editor
  - to activate the neo-tree type <leader> + E
  - then type Ctrl + h or Ctrl l
  - 


#### Rename the current file
- press : key to bring up the command panel
- type file <new filename>


#### Search and Replace in NVIM
leader s r = brings up search and replace 

##### Spin up a terminal window on the fly in nvim
leader f t = opens a terminal window, to close it type exit

  

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

#### LazyVIM commands
- leader f b = bring up telescope with only open buffers to search
- [ + b ] + b to left and right or just use shift + h or l
- Lazyvim search for help = <leader> s h
- if the recording turns up press q to stop it.
  
#### LazyVIM splits
-  leader key + | = to create a vertical split
- to navigate is like navigating the buffers with hjkl but you use shift + hjkl
- to change the size of each pane use ctrl and arrow keys
- shift + : to bring up command, then type q to quit.
- 
### Debugging / Diagnostics
leader x x = bring up trouble for more information on error in console

### Code actions

leader c a = do some action on a reccomendation from LSP

leader u C = change the theme

#### TMUX 

Ctrl + a + q (quickly show the open panes with a number over)
Press the number to switch to the window 
ctrl + a + z = maximise the screen if the screen is split

##### NVIM commands

: for cmdline, then type bd to close or delete current buffer
Hold SHIFT key down then hl to move left or right respectively.

###### Neotree 

When the NeoTree side bar is open allowing you to navigate the folder structure then you can type
type **a** and it will bring up a dialog to create a file or filder at the cursor location. 
