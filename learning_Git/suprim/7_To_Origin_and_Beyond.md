# To Origin and Beyond -- Advanced Git Remotes

## 1: Push Main!
```
git checkout side1
git pull --rebase origin main
git rebase --onto side1 main side2
git rebase --onto side2 main side3
git checkout -B main C7'
git push
```

Switch to the `side1` branch, then pull the latest changes from the `main` branch on the remote origin and rebase the current branch (`side1`) onto `main`. Rebase `side2` onto `side1` starting from `main`, then rebase `side3` onto `side2` starting from `main`. Reset the `main` branch to commit `C7` and switch to it, and finally push the main branch to the remote repository.

## 2: Merging With Remotes
```
git checkout side1
git pull origin main
git checkout side2
git merge side1
git merge side3
git checkout -B main C11
git push
```

Switch to the `side1` branch and pull the latest changes from the `main` branch on the remote origin and merge it with `side1`. Then, switch to the `side2` branch and merge the `side1` branch into `side2`, followed by merging the `side3` branch into `side2`. Reset the main branch to commit `C11` and switch to it, and finally push the main branch to the remote repository.


## 3: Remote Tracking
```
git checkout -b side o/main
git commit
git pull --rebase
git push
```

Create a new branch `side` tracking `o/main` and switch to it. Commit changes in the `side` branch, pull changes from the `upstream` branch and rebase the local commits, and finally push the `side` branch to the remote repository.

## 4: Git Push Arguments
```
git push origin main
git push origin foo
```

Push the `main` branch to the remote origin and then push the `foo` branch to the remote origin.


## 5: Git Push Arguments Expanded
```
git push origin main^:foo
git push origin foo:main
```

Push the parent of `main` to `foo` on the remote origin, then push the `foo` branch to `main` on the remote origin.

## 6: Fetch Arguments
```
git fetch origin C3:foo
git fetch origin C6:main
git checkout foo
git merge main
```

Fetch commit `C3` from origin and store it in the `foo` branch, then fetch commit `C6` from origin and store it in the `main` branch. Switch to the `foo` branch and merge the `main` branch into the `foo` branch.


## 7: Source of Nothing
```
git push origin :foo
git fetch origin :bar
```

Delete the `foo` branch on the remote origin and create a new branch `bar` locally.


## 8: Pull Arguments
```
git pull origin C3:foo
git pull origin C2:side
```
Pull commit `C3` from origin and store it in the `foo` branch, then pull commit `C2` from origin and store it in the `side` branch.

By understanding these advanced Git commands and their arguments, you can effectively manage your remote repositories and streamline your development workflow.