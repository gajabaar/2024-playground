# Ramping Up

## LEVEL 1: DETACH YO’ HEAD
To complete this level, let's detach HEAD from `bugFix` and attach it to the commit instead. <br />
Specify this commit by its hash. The hash for each commit is displayed on the circle that represents the commit. <br />

The command is  <br />
```sh
    git checkout C4
```


## LEVEL 2: RELATIVE REFS (^)
Relative commits are powerful, but we will introduce two simple ones here:
    - Moving upwards one commit at a time with `^`
    - Moving upwards a number of times with `~<num>`
To complete this level, check out the parent commit of `bugFix`. This will detach `HEAD`.<br />
The command is 
```sh
    git checkout C3
```
    

## LEVEL 3: RELATIVE REFS #2 (~)
The ~ operator<br />
You can directly reassign a branch to a commit with the `-f` option. So something like:<br />
    `git branch -f main HEAD~3`<br />
The commands I used the first time to solve are
```sh
    git checkout C4
    git branch -f main HEAD~2
    git checkout C5
    git branch -f bugFix HEA~3
    git checkout C1
    git branch -f main C6
```
    

## LEVEL 4 : Reversing Changes in Git
There are two primary ways to undo changes in Git -- one is using `git reset` and the other is using `git revert`.<br />
To complete this level, reverse the most recent commit on both `local` and `pushed`. You will revert two commits total (one per branch).<br />
    `git reset` works as in the commit never happened.
    `git reset HEAD~1
    git revert HEAD`
    <br />
The commands are :
```sh
    git reset HEAD~1
    git checkout pushed
    git revert pushed
```