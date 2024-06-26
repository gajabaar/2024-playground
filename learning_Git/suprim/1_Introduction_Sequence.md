# Introduction Sequence
In this document, we will explore various aspects of Git, including making commits, creating branches, merging branches, and rebasing branches. Each section will include commands and explanations for what each command does.


## 1: Introduction to Git commits
To begin with, we need to understand how to create commits in Git. Commits are snapshots of the changes in your project, and they allow you to keep track of your progress and revert to previous states if needed. The commands below demonstrate how to make commits.
```sh
git commit
git commit
```
Here, we are making two separate commits. Each git commit command records the current state of the project. You would typically include a message describing the changes in each commit by using the `-m` flag followed by your message, like `git commit -m "Your message here`.


## 2: Branching in Git
Branching is a powerful feature in Git that allows you to diverge from the main line of development and continue to work without affecting that main line. Below is a command to create and switch to a new branch.
```sh
git checkout -b bugFix
```
This command creates a new branch named `bugFix` and switches to it. The `-b` flag stands for branch and `checkout` is the command used to switch branches. By creating a new branch, you can work on fixing a bug without affecting the main branch.


## 3: Branch, Commit, Merge
In this section, we'll create a new branch, make commits, and merge changes back into the main branch. This is a common workflow when working on new features or bug fixes.
```sh
git checkout -b bugFix
git commit
git checkout main
git commit
git merge bugFix
```
First, we create and switch to the `bugFix` branch. After making some changes, we commit them. Then, we switch back to the `main` branch and make another commit there. Finally, we merge the `bugFix` branch into the `main` branch using `git merge bugFix`. This integrates the changes from bugFix into main.


## 4: Branch, Commit, Rebase
Rebasing is another way to integrate changes from one branch into another. It is different from merging in that it rewrites the commit history. This section demonstrates how to rebase a branch.

```sh
git checkout -b bugFix
git commit
git checkout main
git commit
git checkout bugFix
git rebase main
```

First, we create and switch to the `bugFix` branch and make a commit. Then, we switch back to the `main` branch and make another commit. After that, we switch back to the `bugFix` branch and rebase it onto main using `git rebase main`. Rebasing rewrites the commit history of bugFix to appear as if it was developed from the tip of main, providing a cleaner project history.

Each of these sections builds upon the previous ones, providing a comprehensive introduction to using Git for version control in software development.