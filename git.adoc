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

Using the git stash command
---------------------------
working from a feature branch, run git add -A, to stage your changes, then run git stash which will stash changes and revert to original branch
Now you can make other changes, and return to your feature branch at a later stage and run git stash apply to return to your original state (with files
you were working on) to carry on with feature branch changes.

== 20 tips for mastering Git and GitHub
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
