# **Introduction Sequence**

## Introduction to Git Commits

A commit in a Git repository records a snapshot of all the (tracked) files in your directory.

## Level intro1

![git1](./git1.png)

Hint: Just type in “git commit” twice to finish

Commands to solve the level:

git commit

git commit


## Branching in Git

Branches in Git are incredibly lightweight as well. They are simply pointers to a specific commit -- nothing more.

## Level intro2

Hint: Make a new branch with “git branch” and check it out with “git checkout”

![git2](./git2.png)

Commands used:

git branch bugFix

git checkout bugFix


## Merging in Git

In Git, branches allow you to develop features, fix bugs, or experiment in isolation from the main codebase, while merging integrates changes from different branches into a single unified branch, facilitating collaboration and version control.

## Level intro3

Hint: Remember to commit in the order specified (bugFix before main)

![git3](./git3.png)

Commands:

git branch bugFix

git checkout bugFix

git commit

git checkout main

git commit

git merge bugFix


## Rebase Introduction

Git rebase is a command that allows you to integrate changes from one branch into another by moving or combining a sequence of commits, providing a cleaner project history.

## Level intro4

Hint: Make sure you commit from bugFix first

![git4](./git4.png)

Commands:

git checkout -b bugFix

git commit

git checkout main

git commit

git checkout bugFix

git rebase main




# **Ramping up**

## Detach yo' HEAD
In Git, "detaching the HEAD" means checking out a commit that is not associated with any branch.

## Level rampup1

hint: use the label (hash) on the commit for help

![git5](./git5.png)

Command:

git checkout C4


## Relative Refs (^)
In Git, relative references (relative refs) allow you to refer to commits in a way that is relative to a given starting point, typically the current commit (HEAD).

## Level rampup2

hint: Remember the caret (^) operator

![git6](./git6.png)

Command:

git checkout bugFix^


## Relative Refs #2 (~)

## Level rampup3

hint: you need to use at least one direct reference (hash) to complete this level.

![git7](./git7.png)

Commands:

git branch -f main c6

git branch -f bugFix c0

git checkout c1


## Reversing Changes in Git

In Git, relative references (relative refs) allow you to refer to commits in a way that is relative to a given starting point, typically the current commit (HEAD). They are useful for navigating the commit history efficiently.

## Level rampup4

hint: Notice that revert and reset take different arguments

![git8](./git8.png)

Commands:

git reset local~1

git checkout pushed

git revert pushed



# **Moving Work Around**

### 1: Cherry-pick Intro

Git cherry-pick is a command used to copy a specific commit from one branch and apply it onto another branch.

## level move1

hint: git cherry-pick followed by commit names

![git9](./git9.png)

Command:

git cherry-pick c3 c4 c7



## Interactive Rebase Intro

Git interactive rebase is a powerful tool that allows you to change the commit history of your branch before you push your changes to a remote repository.

## level move2

hint: you can use either branches or relative refs(HEAD~) to specify the rebase target

![git10](./git10.png)

Command:

git rebase -i HEAD~5


In the interactive rebase:

- C1
- omit C2
- C3
- C5
- C4
