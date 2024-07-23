# Learning Git Branching

## 1.1 Introduction to git commits
`git commit;`
`git commit;`

## 1.2 Branching in Git
`git branch bugFix;`
`git checkout bugFix;`

## 1.3 Merging in Git
`git branch bugFix`
`git checkout bugFix`
`git commit`
`git checkout main`
`git commit`
`git merge bugfix`

## 1.4 Rebase Introduction
`git checkout -b bugFix`
`git commit`
`git checkout main`
`git commit`
`git checkout bugfix`
`git rebase main`

## 2.1 Detach yo' HEAD
`git checkout c4`

## 2.2 Relative Refs (^)
`git checkout bugFix^`

## 2.3 Relative Refs #2 (~)
`git branch -f bugFix HEAD~2`
`git branch -f main c6`
`git checkout c1`

## 2.4 Reversing Change in Git
`git reset HEAD^`
`git checkout pushed`
`git revert HEAD`

## 3.1 Cherry-pick Intro
`git cherry-pick c3 c4 c7`

## 3.2 Interactive Rebase Intro
`git rebase -I HEAD~4`
A window will open where c2 need to be removed by clicking omit and c4 and c5 need to be rearranged as shown in the goal.