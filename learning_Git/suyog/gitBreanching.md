# Learning Git Branching

## 1.1 Introduction to Git Commits
`git commit;`  
Records changes to the local repository.

## 1.2 Branching in Git
`git branch bugFix;`  
Creates a new branch named `bugFix`.

`git checkout bugFix;`  
Switches to the `bugFix` branch.

## 1.3 Merging in Git
`git branch bugFix`  
Creates a new branch `bugFix`.

`git checkout bugFix`  
Switches to the `bugFix` branch.

`git commit`  
Commits changes in `bugFix`.

`git checkout main`  
Switches back to the `main` branch.

`git commit`  
Commits changes in `main`.

`git merge bugFix`  
Merges `bugFix` into `main`.

## 1.4 Rebase Introduction
`git checkout -b bugFix`  
Creates and switches to `bugFix`.

`git commit`  
Commits changes in `bugFix`.

`git checkout main`  
Switches to `main`.

`git commit`  
Commits changes in `main`.

`git checkout bugFix`  
Switches back to `bugFix`.

`git rebase main`  
Reapplies `bugFix` changes on top of `main`.

## 2.1 Detach HEAD
`git checkout c4`  
Switches to commit `c4`.

## 2.2 Relative Refs (^)
`git checkout bugFix^`  
Checks out the parent commit of `bugFix`.

## 2.3 Relative Refs #2 (~)
`git branch -f bugFix HEAD~2`  
Forces `bugFix` to point to two commits back.

`git branch -f main c6`  
Forces `main` to point to commit `c6`.

`git checkout c1`  
Switches to commit `c1`.

## 2.4 Reversing Changes in Git
`git reset HEAD^`  
Resets the current branch to the parent commit.

`git checkout pushed`  
Switches to the `pushed` branch.

`git revert HEAD`  
Creates a new commit that undoes the last commit.

## 3.1 Cherry-pick Intro
`git cherry-pick c3 c4 c7`  
Applies commits `c3`, `c4`, and `c7` to the current branch.

## 3.2 Interactive Rebase Intro
`git rebase -i HEAD~4`  
Opens an editor to rebase the last 4 commits interactively.
