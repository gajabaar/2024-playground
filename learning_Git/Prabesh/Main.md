#  Introduction Sequence 

A nicely paced introduction to the majority of git commands 

## 1: Introduction to Git Commits

![1.1](./ss/1.1.png)

```sh
git commit
git commit
```

## 2: Branching in Git

![1.2](./ss/1.2.png)

```sh
git branch bugFix
git checkout bugFix
```

## 3: Merging in Git

![1.3](./ss/1.3.png)

```sh
git branch bugFix
git checkout bugFix
git commit
git checkout main
git commit
git merge bugFix
```

## 4: Rebase Introduction

![1.4](./ss/1.4.png)

```sh
git branch bugFix
git checkout bugFix
git commit
git checkout main
git commit
git checkout bugFix
git rebase main
```

# Ramping Up 

The next serving of 100% git awesomes-ness. Hope you're hungry 

## 1: Detach yo' HEAD

![2.1](./ss/2.1.png)

```sh
git checkout C4
```

## 2: Relative Refs (^)

![2.2](./ss/2.2.png)

```sh
git checkout C3
```
OR,
```sh
git checkout C4^
```
OR,
```sh
git checkout C4
git checkout HEAD^
```

## 3: Relative Refs #2 (~)

![2.3](./ss/2.3.png)

```sh
git branch -f bugFix bugFix~3
git branch -f main C6
git checkout HEAD~1
```

## 4: Reversing Changes in Git

![2.4](./ss/2.4.png)

```sh
git reset C1
git checkout C2
git revert HEAD
git branch -f pushed C2'
```
OR,
```sh
git reset HEAD^
git checkout pushed
git revert HEAD
```

# Moving Work Around 

"Git" comfortable with modifying the source tree :P 

## 1: Cherry-pick Intro

![3.1](./ss/3.1.png)

```sh

```

## 2: Interactive Rebase Intro

![3.2](./ss/3.2.png)

```sh

```

# A Mixed Bag 

A mixed bag of Git techniques, tricks, and tips 

## 1: Grabbing Just 1 Commit

![4.1](./ss/4.1.png)

```sh

```

## 2: Juggling Commits

![4.2](./ss/4.2.png)

```sh

```

## 3: Juggling Commits #2

![4.3](./ss/4.3.png)

```sh

```

## 4: Git Tags

![4.4](./ss/4.4.png)

```sh

```

## 5: Git Describe

![4.5](./ss/4.5.png)

```sh

```

# Advanced Topics 

For the truly brave! 

## 1: Rebasing over 9000 times

![5.1](./ss/5.1.png)

```sh

```

## 2: Multiple parents

![5.2](./ss/5.2.png)

```sh

```

## 3: Branch Spaghetti

![5.3](./ss/5.3.png)

```sh

```