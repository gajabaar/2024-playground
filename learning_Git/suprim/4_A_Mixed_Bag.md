# A Mixed Bag

## 1: Grabbing just one commit
`git cherry-pick` allows us to just grab any number of commits we want and place it on the branch we are currently at.
```sh
git checkout main
git cherry-pick bugfix
```
First, we need to switch to the `main` branch using `git checkout main`. After that, we can apply a specific commit from another branch (in this case, the `bugfix` branch) to the `main` branch by using `git cherry-pick bugfix`.

## 2: Juggling Commits
We can use the interactive `git rebase -i` command to reorder commits and omit them. This is useful when the branch we want to make changes is further back the commit tree. 
```sh
git rebase -i HEAD~2
git commit --amend
git rebase -i HEAD~2
git branch -f main HEAD
```
We need to reorder the commits so that the commit labeled `newImage` is on top of the commit tree. We achieve this by starting an interactive rebase with `git rebase -i HEAD~2`, which allows us to reorder the last two commits. After reordering, we amend the commit with `git commit --amend` if any changes are necessary. Then, we reapply the rebase to restore the original order with another `git rebase -i HEAD~2`. Finally, we reset the branch pointer to the main branch's HEAD with `git branch -f main HEAD`.

## 3: Juggling Commits #2
We can use `cherry-pick` to even `cherry-pick` the commits that have been cherry-picked. This is indicated by a `'` in the website's commit tree.
```sh
git checkout C1
git cherry-pick C2
git checkout main
git cherry-pick C2' C3
```
First, check out the commit `C1` using `git checkout C1`. Then, apply the changes from commit `C2` onto `C1` using `git cherry-pick C2`. Switch back to the main branch with `git checkout main`, and apply the changes from the cherry-picked commit (now `C2'`) and commit C3 using `git cherry-pick C2' C3`.
## 4: Git Tags
Tags are a way of marking specific commits permanently. They are usually used to point to major version releases or milestones in a project.
```sh
git tag v0 C1
git tag v1 C2
git checkout C2
```
We tag commit `C1` with the version label `v0` using `git tag v0 C1`. Similarly, we tag commit `C2` with `v1` using `git tag v1 C2`. After tagging, we switch to commit `C2` using `git checkout C2`.

## 5: Git Describe
The `git describe` command will generate the descriptive output based on the nearest tag, the number of commits since that tag, and the current commit hash in the form of `<closest tag name>_<distance to that tag>_<hash>`. However to solve this level we can simply commit.
```sh
git commit
```
These steps provide a structured approach to understanding and using Git commands for picking individual commits, tagging specific commits and describing commits and branches.