# Introduction to Git

## Overview

Git is a powerful version control system used extensively in software development. It allows developers to track changes, collaborate on projects, and manage code efficiently.

### What is Version Control?

Version control systems are software tools that help manage changes to source code over time. They enable teams to track modifications, revert to previous versions, and collaborate seamlessly.

## Getting Started with Git

### Initializing a Git Repository

To start using Git for a project, you first need to initialize a Git repository:

```bash
git init
```

### Adding Files to Git

Once initialized, add files to Git using:

```bash
git add <filename>   # Add a specific file
git add .            # Add all files in the current directory
git add *            # Add all files in the current directory and its subdirectories
```

For a more interactive learning experience, visit [Learn Git Branching](https://learngitbranching.js.org/).

### Introduction to Git Commits

A **commit** in Git captures a snapshot of your project at a specific point in time:

```
git commit -m "commit_message"
```

This command records changes staged using `git add`.

#### Task 1: Understanding Git Commits

To complete this task, execute the following commands:

```bash
git commit    # Commit changes (repeat to finish)
```

## Branching in Git

### What is Branching?

Branching in Git allows developers to create separate lines of development. It enables working on features or fixes without affecting the main codebase.

#### Task 2: Creating and Checking Out Branches

To create and switch branches:

```bash
git branch <branch_name>     # Create a new branch
git checkout <branch_name>   # Switch to the newly created branch
# Or, use `git switch <branch_name>`
```

### Merging in Git

#### Understanding Merging

Merging integrates changes from one branch into another, combining their histories:

```bash
git merge <branch_name>     # Merge changes from <branch_name> into current branch
```

#### Task 3: Merging a Feature Branch

To merge a feature branch (`bugFix`) into `main`:

```bash
git branch bugFix
git checkout bugFix
# Make changes and commit
git checkout main
git merge bugFix
```

### Introduction to Rebase

#### What is Rebase?

Rebasing in Git is another way to integrate changes from one branch to another, creating a linear sequence of commits:

```bash
git rebase <branch_name>    # Rebase current branch onto <branch_name>
```

#### Task 4: Using Rebase

To rebase `bugFix` onto `main` for a linear commit history:

```bash
git branch bugFix
git checkout bugFix
# Make changes and commit
git checkout main
git rebase bugFix
```

## Ramping Up

### Detach yo' HEAD

#### Understanding HEAD Detachment

Detaching `HEAD` allows moving to a specific commit:

```bash
git checkout <commit_hash>
```

### Relative Refs (^)

#### Using Relative References

Relative references like `^` and `~` simplify navigation through commit history:

```bash
git checkout HEAD^    # Move to the first parent of the current commit
git checkout HEAD~3   # Move back three commits from HEAD
```

### Reversing Changes in Git

#### Undoing Changes

Git provides `git reset` and `git revert` to undo changes:

```bash
git reset HEAD~1    # Undo the most recent commit
git revert HEAD     # Create a new commit that reverses changes of the most recent commit
```

#### Task 5: Reverting Changes

To revert commits locally and remotely:

```bash
git reset HEAD~1    # Undo commit locally
git checkout <remote_branch>
git revert HEAD     # Reverse commit remotely
```

## Moving Work Around

### Cherry-pick Introduction

#### Using Cherry-pick

Cherry-picking allows applying specific commits from one branch to another:

```bash
git cherry-pick <commit_hash>
```

#### Task 6: Cherry-picking Commits

To cherry-pick commits `c3`, `c4`, and `c7` into `main`:

```bash
git checkout main
git cherry-pick c3 c4 c7
```

### Git Interactive Rebase

#### Interactive Rebase Overview

Interactive rebase lets you edit commit history interactively:

```bash
git rebase -i <commit_hash>
```

#### Task 7: Interactive Rebase

To interactively rebase commits and rearrange them:

```bash
git rebase -i HEAD~4
# Follow on-screen instructions to reorder or edit commits
```

### A Mixed Bag

#### Additional Techniques

Explore advanced Git operations like commit manipulation:

```bash
git rebase -i HEAD~2   # Manipulate commits interactively
git commit --amend     # Amend the last commit
git branch -f main <commit_hash>   # Force move the main branch
```

### Git Tags

#### Tagging Commits

Tags in Git mark specific commits for easy reference:

```bash
git tag <tag_name> <commit_hash>
```

#### Task 8: Using Git Tags

To tag commits as `v0` and `v1`:

```bash
git tag v0 <commit_hash>
git tag v1 <commit_hash>
git checkout <commit_hash>
```

### Git Describe

#### Describing Commits

Git describe provides human-readable names to specific commits:

```bash
git describe
```

#### Task 9: Using Git Describe

Explore Git describe to label commits effectively:

```bash
git describe
git commit
```

## Conclusion

In this comprehensive guide, I've covered the fundamentals of Git, from basic commands to advanced operations like branching, merging, and rebasing. Mastering these tools will empower you to manage your projects efficiently and collaborate seamlessly with teams.

## Additional Resources

- [Official Git Documentation](https://git-scm.com/documentation)
- [Learn Git Branching](https://learngitbranching.js.org/)
- [Git Cheat Sheet](https://education.github.com/git-cheat-sheet-education.pdf)

---


