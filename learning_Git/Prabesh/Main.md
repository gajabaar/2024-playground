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
git cherry-pick C3 C4 C7
```

## 2: Interactive Rebase Intro

![3.2](./ss/3.2.png)

```sh
git rebase -i C1
```
![3.2.1](./ss/3.2.1.png)

# A Mixed Bag 

A mixed bag of Git techniques, tricks, and tips 

## 1: Grabbing Just 1 Commit

![4.1](./ss/4.1.png)

```sh
git reset HEAD^
git checkout main
git cherry-pick C4
```

## 2: Juggling Commits

![4.2](./ss/4.2.png)

```sh
git rebase -i C1
```
![4.2.1](./ss/4.2.1.png)
```sh
git commit --amend
```
```sh
git rebase -i C1
```
![4.2.2](./ss/4.2.2.png)
```sh
git branch -f main C3''
```

## 3: Juggling Commits #2

![4.3](./ss/4.3.png)

```sh
git checkout main
git cherry-pick C2
git reset HEAD^
git cherry-pick C2' C3
```

## 4: Git Tags

![4.4](./ss/4.4.png)

```sh
git tag v0 C1
git tag v1 C2
git checkout v1
```

## 5: Git Describe

![4.5](./ss/4.5.png)

```sh
git describe C1
git commit
```

# Advanced Topics 

For the truly brave! 

## 1: Rebasing over 9000 times

![5.1](./ss/5.1.png)

- Pathetic Attempt -1:

![5.1.1](./ss/5.1.1.png)

- Ugh. I give up!
```sh
show solution
```
![5.1.2](./ss/5.1.2.png)

- Oh... Ok I will try again.

- Unsatisfactory sucess: Site said I had solved it, but my solution wasn't quite resembling the goal. Just look at the side branch.
```sh
git rebase main bugFix
git rebase side another
git rebase bugFix another
git branch -f main another
```
![5.1.3](./ss/5.1.3.png)

- Satisfactory sucess:
```sh
* git rebase main bugFix
* git rebase bugFix side
* git rebase side another
|\
| \
|  * (HEAD -> screenshot_image) git branch -f main another
|  * git checkout main
|
* (origin/main) git rebase another main
```
![5.1.4](./ss/5.1.4.png)

## 2: Multiple parents

![5.2](./ss/5.2.png)

```sh
git checkout HEAD^
git checkout HEAD^2
git checkout HEAD^
```
OR,
```sh
git checkout HEAD~^2~
```
THEN,
```sh
git branch bugWork
git checkout main
```

## 3: Branch Spaghetti

![5.3](./ss/5.3.png)

- My solution:
```sh
git rebase C2 three
git checkout one
git cherry-pick c4 c3 c2  
git rebase -i two C5: C5 > C4 > C3 > C2
git rebase C2'' two
```

- Their Solution
```sh
git checkout one
git cherry-pick C4 C3 C2
git checkout two
git cherry-pick C5 C4 C3 C2
git branch -f three C2
```