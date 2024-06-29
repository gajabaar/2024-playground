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

## 4. Reversing Changes in Git
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
# Moving Work Around

## 1. Cherry-pick Intro

- The first command in this series is called `git cherry-pick`. It takes on the following form:
    - `git cherry-pick <Commit1> <Commit2> <...>`
- To solve,

![Untitled](Git%20and%20GitHub%20WriteUps%20images/Untitled%208.png)

- Solution

```bash
$ git cherry-pick C3 C4 C7
```

## 2. Interactive Rebase Intro

- Git cherry-pick is great when you know which commits you want
- But what about the situation where you don't know what commits you want? Thankfully git has you covered there as well! We can use interactive rebasing for this
- All interactive rebase means Git is using the `rebase` command with the `-i` option.
- For "real" git, the UI window means opening up a file in a text editor like `vim`

```bash
rebase -i HEAD~
```

- To solve,

![Untitled](Git%20and%20GitHub%20WriteUps%20images/Untitled%209.png)

- Solution

```bash
$ git rebase -i HEAD~4
```

![Untitled](Git%20and%20GitHub%20WriteUps%20images/Untitled%2010.png)

# A Mixed Bug

## 1. Grabbing just one commit

- To solve,

![Untitled](Git%20and%20GitHub%20WriteUps%20images/Untitled%2011.png)

- Solution

```bash
$ git checkout main
$ git cherry-pick C4

OR

$ git rebase -i HEAD~3
$ git checkout main
$ git merge bugFix
```

## 2. Juggling Commits

- We will re-order the commits so the one we want to change is on top with `git rebase -i`
- We will `git commit --amend` to make the slight modification
- Then we will re-order the commits back to how they were previously with `git rebase -i`
- Finally, we will move main to this updated part of the tree to finish the level (via the method of your choosing)
- To solve,

![Untitled](Git%20and%20GitHub%20WriteUps%20images/Untitled%2012.png)

- Solution

```bash
$ git rebase -i HEAD~2
$ git commit --amend
$ git rebase -i HEAD~2
$ git checkout main
$ git merge caption

OR

$ git rebase -i HEAD~2
$ git commit --amend
$ git rebase -i HEAD~2
$ git rebase caption main
```

## 3. Juggling Commits #2

- To solve

![Untitled](Git%20and%20GitHub%20WriteUps%20images/Untitled%2013.png)

- Solution

```bash
$ git checkout main
$ git cherry-pick C2
$ git commit --amend
$ git cherry-pick C3
```

## 4. Git Tags

- Branches are easily mutated, often temporary, and always changing.
- To solve,

![Untitled](Git%20and%20GitHub%20WriteUps%20images/Untitled%2014.png)

- Solution

```bash
$ git checkout HEAD~1
$ git tag v1
$ git tag v0 C1
```

## 5. Git Describe

- Because tags serve as such great "anchors" in the codebase, git has a command to *describe* where you are relative to the closest "anchor" (aka tag). And that command is called `git describe`!
- To solve,
- motive is to learn about `git describe`

![Untitled](Git%20and%20GitHub%20WriteUps%20images/Untitled%2015.png)

- Solution is simple `git commit` but let’s check the git describe command and view output

```bash
$ git describe main
$ git describe side
$ git describe bugFix
$ git commit
```

- We see that, by using this command we get the tag name how much behind that commit and from which node

# Advanced Topics

## 1. Rebasing over 9000 times

- To solve,

![Untitled](Git%20and%20GitHub%20WriteUps%20images/Untitled%2016.png)

- Solution

```bash
$ git rebase main bugFix
$ git rebase bugFix side
$ git rebase side another
$ git rebase another main
```

## 2. Multiple Parents

- Rather than specifying the number of generations to go back (what `~` takes), the modifier on `^` specifies which parent reference to follow from a merge commit.
- To solve,

![Untitled](Git%20and%20GitHub%20WriteUps%20images/Untitled%2017.png)

- Solution

```bash
$ git branch bugWork main^^2^
```

## 3. Branch Spaghetti

- To solve

![Untitled](Git%20and%20GitHub%20WriteUps%20images/Untitled%2018.png)

- Solution

```bash
$ git rebase C2 three
$ git checkout one
$ git cherry-pick C4 C3 C2
$ git checkout two
$ git cherry-pick C5 C4 C3 C2
```