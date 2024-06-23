# Git and GitHub WriteUps

Learngitbranching.js.org

# **Introduction Sequence**

## 1. Introduction to Commits

- A commit in git repository records a snapshot of all the tracked files in your directory.
- It’s like gaint copy and paste but even better
- Goal to reach

![Untitled](Git%20and%20GitHub%20WriteUps%20images/Untitled.png)

- To solve the level just

```bash
$ git commit
$ git commit
```

## 2. Branching in Git

- Branches in Git are incredibly lightweight as well.
- They simply pointers to a specific commit.
- Goal
    
    ![Untitled](Git%20and%20GitHub%20WriteUps%20images/Untitled%201.png)
    
- To solve

```bash
$ git checkout -b bugFix
```

## 3. Merging in Git

- Merge combines the work from two different branches together.
- This will allow us to branch off, develop new feature and then combine it back in.
- Goal

![Untitled](Git%20and%20GitHub%20WriteUps%20images/Untitled%202.png)

- To solve,

```bash
$ git checkout -b bugFix
$ git commit
$ git checkout main
$ git commit
$ git merge bugFix
```

## 4. Rebase Introduction

- This is the second way of combining work between branches
- Rebasing essentially takes a set of commits, "copies" them, and plops them down somewhere else.
- Goal

![Untitled](Git%20and%20GitHub%20WriteUps%20images/Untitled%203.png)

- To solve this level,

```bash
$ git checkout -b bugFix
$ git commit
$ git checkout main
$ git commit
$ git checkout bugFix
$ git rebase main
```

# Ramping Up

## 1. Detach yo’ Head

-