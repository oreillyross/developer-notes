# Git usage

== Git commands

git checkout - # This switches between recent branch and older branch last used. 
git pull is the same thing as saying git fetch and then git merge
git checkout -b <NEW_BRANCH> is a shortcut to create a branch then switch to it.
git clone --bare <repo> .git
git add -A # adds everything that has changed
git status # to check what is commited, changed, new etc.
git commit -m "Message to say what changed"
After making changes on a feature branch, git checkout to the main branch and then git merge <feature branch>
This will either FAST FORWARD or create a three way merge.
git branch -d <feature branch> # delete branch merged into main


git config --bool core-bare false
git reset --hard

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
- Only one - or + refers to a line in a file being changed
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

### Git Revision Selection
An example of how to fix a mistake in your codebase the hardway

```console
        git checkout B # DETACHED HEAD state
        git checkout -b temp # create a temp branch

```


Using the git stash command
---------------------------
working from a feature branch, run git add -A, to stage your changes, then run git stash which will stash changes and revert to original branch
Now you can make other changes, and return to your feature branch at a later stage and run git stash apply to return to your original state (with files
you were working on) to carry on with feature branch changes.

#### A typical use case

A colleague interupts you to make changes to the codebase but you have changes that are not yet checked in. So you run
```git stash save```
Make your changes, and then to return to your original state and reverting the stashed files, you run ```git stash pop```

20 tips for mastering Git and GitHub
====================================

http://www.infoworld.com/article/3205884/application-development/20-tips-for-mastering-git-and-github.html?upd=1499415090366[Mastering Git by Martin Heller]


.1 Clone almost anything
.2 Pull frequently
.3 Commit early and often
.4 Comment your commits as you would have others comment theirs
.5 Push when your changes are tested
.6 Branch freely
.7 Merge carefully
.8 Stash before switching branches
.9 Use gists to share snippets and pastes
.10 Explore GitHub
.11 Contribute to open source projects
.12 Use editors and IDEs that “git it”
.13 Fork a repo
.14 Watch projects
.15 Follow friends
.16 Send pull requests
.17 Create and resolve issues
.18 Write informative README pages
.19 Use Markdown
.20 Convert your older repos to Git


