Snippets useful in a Linux terminal context,

This snippet allow you to set the PATH in a go environment so that your compiled binaries run from anywhere without having to navigate through to $HOME/go/bin

```
$ export PATH=$PATH:$(dirname $(go list -f '{{.Target}}' .))
$ hello
Hello, world.
$
```
