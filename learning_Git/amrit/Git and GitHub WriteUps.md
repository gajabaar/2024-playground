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

- HEAD is the symbolic name for the currently checked out commit -- it's essentially what commit you're working on top of.
- HEAD always points to the most recent commit which is reflected in the working tree.
- To solve,

![alt text](Git%20and%20GitHub%20WriteUps%20images/image.png)
- Solution
```
$ git checkout c4
```

## 2. Relative Refs (^)
- Hashes are usually a lot longer in the real Git world as well.
    - Moving upwards one commit at a time with `^`
    - Moving upwards a number of times with `~<num>`
- So saying `main^` is equivalent to "the first parent of `main`".
- `main^^` is the grandparent (second-generation ancestor) of `main`
- To solve
![alt text](Git%20and%20GitHub%20WriteUps%20images/4.png)
- Solution
```
$ git checkout C4^
```
## 3. Relative Refs (~)
- The tilde operator (optionally) takes in a trailing number that specifies the number of parents you would like to ascend.
- To solve,
![alt text](Git%20and%20GitHub%20WriteUps%20images/5.png)
- Solution
```
$ git checkout HEAD~1
$ git branch -f main C6
$ git branch -f bugFix C0
```

## 4. Relative Refs (~)
- `git reset` reverses changes by moving a branch reference backwards in time to an older commit.
- In order to reverse changes and *share* those reversed changes with others, we need to use `git revert`.
- To solve,
![alt text](Git%20and%20GitHub%20WriteUps%20images/6.png)
- Solution
```
$ git branch -f local C1
$ git checkout pushed
$ git revert pushed
```