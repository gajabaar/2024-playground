*1: Introduction to Git Commits*

## Git Commits

A commit in a git repository records a snapshot of all the (tracked) files in your directory.

# **Level intro1**

!img→git1(C:\Users\acer\Downloads\git-writeups\git1)

Hint: Just type in “git commit” twice to finish

Commands to solve the level:

git commit

git commit


*2: Branching in Git*

## Git Branches

Branches in Git are incredibly lightweight as well. They are simply pointers to a specific commit -- nothing more.

# **Level intro2**

hint: Make a new branch with “git branch” and check it out with “git checkout”

img→ git2

Commands used:

git branch bugFix

git checkout bugFix

*3: Merging in Git*

## Branches and Merging

In Git, branches allow you to develop features, fix bugs, or experiment in isolation from the main codebase, while merging integrates changes from different branches into a single unified branch, facilitating collaboration and version control.

### **Level intro3**

hint: Remember to commit in the order specified (bugFix before main)

Commands:

git branch bugFix

git checkout bugFix

git commit

git checkout main

git commit

git merge bugFix

*4: Rebase Introduction*

## Git Rebase

Git rebase is a command that allows you to integrate changes from one branch into another by moving or combining a sequence of commits, providing a cleaner project history.

# **Level intro4**

hint: make sure you commit from bugFix first

Commands:

git checkout -b bugFix

git commit

git checkout main

git commit

git checkout bugFix

git rebase main