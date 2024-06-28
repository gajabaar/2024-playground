# Push & Pull -- Git Remotes

## 1: Clone Intro
This command differs from the usual `git clone`. In reality, `git clone` clones a remote repository into a local one. However here, it converts a local repository into a remote one. This highlights the difference and sets the context for converting a local repository into a remote one.
```
git clone
```

## 2: Remote Branches
Here `o` is simply an alias for origin. Any branch with a preceding `o/` indicates a remote repository. The commands `git commit` and `git checkout o/main` are used to demonstrate working with remote branches. `o/` prefix helps identify branches that are tracked from the remote repository.
```
git commit
git checkout o/main
git commit
```

## 3: Git Fetchin'
The `git fetch` command is used to retrieve updates from the remote repository without merging them into the local branch. This allows users to review changes before integrating them.
```
git fetch
```

## 4: Git Pullin'
The `git pull` fetches changes from the remote repository and directly merges them into the current branch. It combines `git fetch` and `git merge` in a single step.
```
git pull
```

## 5: Faking Teamwork
This section simulates a teamwork scenario. The commands include cloning the repository, using a fictional `git fakeTeamwork` command to simulate changes by teammates, committing changes, and pulling updates from the remote repository to stay in sync with the team.
```
git clone
git fakeTeamwork 2
git commit
git pull
```

## 6: Git Pushin'
Here, the focus is on pushing changes to the remote repository. The `git commit` commands are used to save changes locally, and `git push` uploads these commits to the remote repository, making them available to other collaborators.
```
git commit
git commit
git push
```

## 7: Diverged History
This section deals with handling diverged commit histories. After cloning and simulating teamwork changes, the `git pull --rebase` command is used to rebase local commits onto the fetched branch, ensuring a linear commit history. Finally, `git push` updates the remote repository.
```
git clone
git fakeTeamwork
git commit
git pull --rebase
git push
```

## 8: Locked Main
In this section, a new feature branch is created and pushed to the remote repository. The `git branch -f main C1` command is used to forcefully move the `main` branch to a specific commit (`C1`), demonstrating how to update branch references manually.
```
git checkout -b feature
git push origin feature
git branch -f main C1
```

These exercises make us more familiar with remotes and how to work in a collaborative environment with a remote repository by pulling changes, fetching them and updating branches in a non-destructive manner.







