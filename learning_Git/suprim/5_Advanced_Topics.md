# Advanced Topics

## 1: Rebasing over 9000 times
Rebasing is a powerful feature in Git that allows you to integrate changes from one branch into another. The following series of commands demonstrates how to rebase a series of branches onto each other and then update the main branch to the latest state.
```
git checkout bugfix
git rebase main
git checkout side
git rebase bugFix
git checkout another
git rebase side
git branch -f main HEAD
```

## 2: Multiple Parents
In some cases, you might want to create a branch that points to a commit with multiple parents, such as a merge commit. The following code demonstrates how this can be done. Note `^2` indicates that we want to move to the second parent of the commit.
```
git branch bugWork
git branch -f bugWork HEAD~^2~
```

## 3: Branch Spaghetti
Sometimes you need to deal with unordered commit trees. Using `git cherry-pick` and `git branch -f` can help simplify things and untangle branches.
```
git checkout one
git cherry-pick C4 C3 C2
git checkout two
git cherry-pick C5 C4' C3' C2'
git branch -f three C2
```

These exercises illustrate a way to organize commit trees using commands such as `rebase` and `cherry-pick` which can be helpful in organizing commits. Commit trees can quickly become tangled up and messy in large projects with multiple people contributing and features being developed in branches parallely.
