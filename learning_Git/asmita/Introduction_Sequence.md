# Introduction Sequence

## LEVEL 1: INTRODUCTION TO GIT COMMITS

The first level teaches about the `git commit` command. Commits are snapshots of the changes in your project, allowing you to track progress and revert to previous states if needed. <br />
To progress from commit C1 to C2, use `git commit`. Another `git commit` takes you to C3, which is our goal. <br />

Commands:
```sh
    git commit
    git commit
```


## LEVEL 2: BRANCHING IN GIT
Branching in Git allows developers to create separate lines of development to work on different features or fixes without affecting the main codebase until they're ready to merge changes back. <br />
**Branch early, and branch often** <br />
The commands for this level are: <br />
```sh
    git checkout -b bugFix
```
This command creates a new branch named ‘bugFix’ and switched to it. 


## LEVEL 3: MERGING IN GIT
The command is <br />
'git merge branchName' <br />
The branchName here is bugFix <br />
The command to checkout and merge is  <br />
'git checkout bugFix;git merge main'

Stepwise commands are 
```sh
    git checkout -b bugFix
    git commit
    git checkout main
    git commit
    git merge bugFix
```


## LEVEL 4 : REBASE INTRODUCTION
The second way of combining work between branches is *rebasing.* Rebasing essentially takes a set of commits, "copies" them, and plops them down somewhere else.<br />
To complete this level, do the following <br />
    - Checkout a new branch named `bugFix`
    - Commit once
    - Go back to main and commit again
    - Check out bugFix again and rebase onto main
    
The commands are <br />
```sh
    git checkout -b bugFix
    git commit
    git checkout main
    git commit
    git checkout bugFix
    git rebase main
```