# Writeup of LearnGitBranching Lab
## Introduction Sequence
### Level1-Introduction to Git Commits
**Goal-** Commit twice 
![Introduction to git commit](./images/introToGitCommit.png)
**Solution**
```
git commit
git commit
```
### Level2-Branching in git
**Goal-** Make new branch named bugFix and switch it to that branch 
![Branching in Git](./images/Branching.png)

**Solution**
```
git checkout -b bugFix
```
### Level3-Merging in git
**Goal-** Make new branch named bugFix and switch it to that branch,commit once there then switch back to main,again commit once in main then with git merge command merge bugFix branch in to the main 
![Merging in git](./images/Merge.png)

**Solution**
```
git checkout -b bugFix
git commit
git checkout main
git commit
git merge bugFix

```
### Level4-Rebase
**Goal-** Make new branch named bugFix and switch it to that branch,commit once there then switch back to main,again commit once in main.Again switch to bugFix and with git rebase command rebase main branch
![rebasing in Git](./images/Rebase.png)

**Solution**
```
git checkout -b bugFix
git commit
git checkout main
git commit
git checkout bugFix
git rebase main

```
# Ramping up
### Level1-Datach Head
**Goal-** Detach head from bugFix and attach it to commit instead
![detaching head in Git](./images/detach.png)

**Solution**
```
git checkout c4

```
### Level2-Detaching Head using Relative Ref(^)
**Goal-** Checkout to parent commit of bugFix using relative refs
![detaching head using refs in Git](./images/detachRef.png)

**Solution**
```
git checkout bugFix^

```
### Level3-Detaching Head using Relative Re
f(~)
**Goal-** Move HEAD ,main,ugFix to destination position as shown in the images below
![detaching head using refs in Git](./images/detachRef2.png)

**Solution**
```
git branch -f bugFix HEAD~2
git branch -f main c6
git checkout HEAD^

```


