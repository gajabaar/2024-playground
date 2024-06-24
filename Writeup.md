## Introduction to Git Commits

A commit in a git repository records a snapshot of all the (tracked) files in your directory. Git maintains a history of all commits. 

Solution:

```bash
git commit
git commit
```

## Branching in Git

Branches are pointers to a specific commit.

Used to logically divide your work.

Branch essentially says “I want to include the work of this commit and all parent commits.”

Commands used in this level:

```bash
git branch branchName
git checkout branchName
```

Shortcut to do both the commands (and solve the level):

```bash
git checkout -b branchName
```

## Branches and Merging

Merge means to include all the works from both the “parents”

Commands to solve this level

```bash
git checkout -b bugFix
git commit
git checkout main
git commit 
git merger bugFix
```

## Git Rebase

Another way of combining work between branches.

Takes a set of commits, “copies” them, and plops them down somewhere else.

Helps to make a nice linear sequence of commits.
