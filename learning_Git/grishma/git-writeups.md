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


# **A Mixed Bag**

### 1: Grabbing Just 1 Commit

## level mixed1

hint: Remember, interactive rebase or cherry-pick is your friend here

![git11](./git11.png)

Commands:

git checkout main

git cherry-pick c4



### 2: Juggling Commits

## level mixed2

hint: The first command is git rebase -i HEAD~2

![git12](./git12.png)

Commands:

git rebase -i HEAD~2

![git13](./git13.png)

git commit —amend

git rebase -i HEAD~2

![git14](./git14.png)

git branch -f main caption


### 3: Juggling Commits #2

## level mixed3

hint: Don’t forget to forward main to the updated changes!

![git15](./git15.png)

Commands:

git checkout main

git cherry-pick c2

git commit —amend

git cherry-pick c3


### 4: Git Tags

## level mixed4

hint: you can either check out the commit directly or simply checkout the tag

![git16](./git16.png)

Commands:

git tag v0 c1

git tag v1 c2

git checkout v1



### 5: Git Describe

## level mixed5

hint: Just commit once on bugFix when you’re ready to move on

![git17](./git17.png)

Command:

git commit -m bugFix




# **Advanced Topics**

### 1: Rebasing over 9000 times

## level advanced1

hint: Remember, the only efficient way might be to only update main at the end. . .

![git18](./git18.png)

## In 7 commands

git checkout bugFix

git rebase main

git checkout side

git rebase bugFix

git checkout another

git rebase side

git branch -f main



## In 4 commands

git rebase main bugFix

git rebase bugFix side

git rebase side another

git rebase main side



### 2: Multiple parents

## level advanced2

hint: use ‘git branch bugWork’ with a target commit to create a missing reference.

![git19](./git19.png)

Command:

git branch bugWork HEAD~^2~



### 2: Multiple parents

## level advanced3

Make sure to do everything in proper order! Branch one first, then two, then three

![git19](./git19.png)

Commands:

git checkout one

git cherry-pick c4 c3 c2

git checkout one

git cherry-pick c5 c4 c3 c2

git branch -f three c2