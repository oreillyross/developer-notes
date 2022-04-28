# Git usage

## git log
if the git log is large git will open the page into the UNIX less pager output.
### useful commands in LESS
- q = quit the terminal
- use PGUP PGDOWN or cursors, or j and k, ctrl+f ctrl+b to go fwd and back
- use the / char to search, n and shift+n to go fwd in search or back

### useful commands in terminal 
- git log --oneline
- git log --decorate
- git log --graph # shows the branching structure of commits
- git log --p # shows what was changed
- git log --stat # shows the additions / deletions per file changed
- git log -3 # show the 3 most recent commits
- git log --after="yesterday" # only show commits between now and yesterday, or use 30 minutes ago, or last week, or 2 weeks ago, 3/15/16
- git log --before to constrain the above # you can also use since and until 
- git log --author="Trevor" # search all git commits by author, also can use a reg exp 
- git log --grep="copyright"  # look for commit where search term appears
- git log -p -S"Math"  # use pickaxe option to look since files for search term, include -p to see changes, use the -i to ignore case
- git log -p GMath\|Random # this is a search using regexp to search in files for Math or Random, use the -i to ignore case
- git log --no-merges # only show files which have not been merged
- git log main..cool-feature # to see where the branches diverge, from main and then cool-feautre branch, the two dots are required, see the commits contained between the two refs. These commands can be composed together on one line as well.

### Git diff
- --- or +++ (three plus or minus) means it refers to a file
- Only one - or + refers to a lie in a file being changed
- Run git diff with --stat option to get a condensed view with lines counts that have been modified
- By default the comparison is made with working directory and last commit
- git diff --cached shows comparison between working directory and staging area
- git diff HEAD shows both staging and working directory against last commit
- __HANDY TIP__ run git fetch, then git diff origin/main to see local changes that have not merged yet with current pulled data from remote main branch

### git blame
- used to tell who made what changes when
- can be used to get the commit id, which can beinterrogated further
- Then run ```git log {commit id} -p ``` to see more info

### git tag
- run like so ``` git tag V1.0.0``` to version for specific releases, semantic versioning.
- Major (breaking changes) Minor (feature changes) and Patch (fix bugs)
- __must use__ ```git push --tags``` to ensure the tags are recorded on remote repo.
- use ```git tag -a V1.0.2 -m "Some message annotated"``` to annotate messages to tags
- Leave the -m option off to open up a code editor where you can provide your release notes.
- 

