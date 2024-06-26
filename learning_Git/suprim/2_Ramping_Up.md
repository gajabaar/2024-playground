# Introduction Sequence
In this document, we will explore more features of Git such as handling branches, references, and reversing changes in Git. Each section will include commands and explanations for what each command does.

## 1: Detach yo' HEAD 
Detaching the HEAD means checking out a specific commit directly rather than a branch. `git checkout <commit>` is used to move the HEAD to a particular commit.
```sh
git checkout C4
```
This command checks out commit `C4`, detaching the HEAD from any branch. You are now in a `detached HEAD` state, which allows you to explore and make changes without affecting any branch.

## 2: Relative Refs (^)
`^` denotes the parent of a particular commit and can be used to move HEAD backwards. To use relative references with the `^` operator:
```sh
git checkout bugFix
git checkout HEAD^ 
```
First, check out the `bugFix` branch. The `git checkout HEAD^` command then moves the HEAD to the parent commit of the current commit in `bugFix`. This is useful for navigating the commit history efficiently.

## 3: Relative Refs #2 (~)
`~` is essentially an alternative to `^` as a relative reference. For example: `~num` is used to move the HEAD backward by `num` times.	It can be used to specify the number of commits to backtrack. `git branch -f` is used to forcefully move branches in this context. To use relative references with the `~` operator and update branches:
```sh
git branch -f bugFix HEAD~2
git branch -f main C6
git checkout C1
```
The `git branch -f bugFix HEAD~2` command forces the `bugFix` branch to point to the commit two parents before the current commit. The `git branch -f main C6` command forces the `main` branch to point to commit `C6`. Finally, the `git checkout C1` command moves the `HEAD` pointer to commit `C1`.

## 4: Reversing Changes in Git
To reverse changes in Git it depends on whether the action is to be done locally or remotely. For reversing local changes, we use the `git reset` command which causes the branch to move one step above to its parent whereas since remote repositories are used by many people, this is not possible. Instead we use the `git revert` command to create a new commit which effectively has the state of the repository before the commit to be reverted.
```sh
git reset HEAD^
git checkout pushed
git revert
```
The `git reset HEAD^` command moves the HEAD and the current branch to the previous commit, effectively undoing the last commit. Then, `git checkout pushed` switches to the `pushed` branch. The `git revert` command is used to create a new commit that undoes the changes from a previous commit, without altering the commit history.

These steps provide a structured approach to understanding and using Git commands for handling branches, navigating commit history, and reversing changes.