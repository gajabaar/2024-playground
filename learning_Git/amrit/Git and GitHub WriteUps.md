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

# Remote

## Push and Pull — Git Remotes!

### 1. Clone Intro

- `git clone` in the real world is the command you'll use to create *local* copies of remote repositories
- To solve,

![Untitled](Git%20and%20GitHub%20WriteUps%20images/Untitled%2019.png)

- Solution

```bash
$ git clone
```

## 2. Remote Branches

- The first thing you may have noticed is that a new branch appeared in our local repository called `o/main`. This type of branch is called remote branch
- Remote branches have the special property that when you check them out, you are put into detached `HEAD` mode.
- if you look at a branch named `o/main`, the branch name is `main` and the name of the remote is `o`.
- To solve,

![Untitled](Git%20and%20GitHub%20WriteUps%20images/Untitled%2020.png)

- Solution

```bash
$ git commit
$ git checkout o/main
$ git commit
```

## 3. Git Fetch

- `git fetch` performs two main steps, and two main steps only. It:
    - downloads the commits that the remote has but are missing from our local repository, and...
    - updates where our remote branches point (for instance, `o/main`)
- `git fetch` essentially brings our *local* representation of the remote repository into synchronization with what the *actual* remote repository looks like (right now).
- `git fetch`, however, does not change anything about *your* local state. It will not update your `main` branch or change anything about how your file system looks right now.
- To solve,

![Untitled](Git%20and%20GitHub%20WriteUps%20images/Untitled%2021.png)

- Solution

```bash
$ git fetch
```

## 4. Git Pullin’

- `git pull` is equivalent to the two command `git fetch` and `git merge`
- For e.g: `git fetch` and `git merge o/main` is equivalent to `git pull`
- To solve,

![Untitled](Git%20and%20GitHub%20WriteUps%20images/Untitled%2022.png)

- Solution, can be solved by `git fetch` and `git merge o/main` or,

```bash
$ git pull
```

## 5. Faking Teamwork

- pull down changes that were introduced in the remote.
- That means we need to essentially "pretend" that the remote was updated by one of your coworkers / friends / collaborators, sometimes on a specific branch or a certain number of commits. That can be done using the command `git fakeTeamwork`
- To solve,

![Untitled](Git%20and%20GitHub%20WriteUps%20images/Untitled%2023.png)

- Solution

```bash
$ git clone
$ git fakeTeamwork
$ git fakeTeamwork
$ git commit
$ git pull
```

## 6. Git pushing

- the way to upload shared work is the opposite of downloading shared work. And what's the opposite of `git pull`? `git push`!
- `git push` is responsible for uploading *your* changes to a specified remote and updating that remote to incorporate your new commits.
- To solve,

![Untitled](Git%20and%20GitHub%20WriteUps%20images/Untitled%2024.png)

- Solution

```bash
$ git commit
$ git commit
$ git push
```

## 7. Diverged History

- To solve,

![Untitled](Git%20and%20GitHub%20WriteUps%20images/Untitled%2025.png)

- Solution

```bash
$ git clone
$ git fakeTeamwork
$ git commit
$ git pull --rebase
$ git push
```

## 8. Locked Main

- The remote rejected the push of commits directly to main because of the policy on main requiring pull requests to instead be used.
    
    You meant to follow the process creating a branch then pushing that branch and doing a pull request, but you forgot and committed directly to main. Now you are stuck and cannot push your changes.
    
- To solve,

![Untitled](Git%20and%20GitHub%20WriteUps%20images/Untitled%2026.png)

- Solution

```bash
$ git reset --hard o/main
$ git checkout -b feature C2
$ git push origin feature
```

# **To Origin And Beyond -- Advanced Git Remotes!**

## 1. Push Main!

- To solve,

![Untitled](Git%20and%20GitHub%20WriteUps%20images/Untitled%2027.png)

- Soultion

```bash
$ git fetch
$ git rebase o/main side1
$ git rebase side1 side2
$ git rebase side2 side3
$ git checkout main
$ git merge side3
$ git push
```

## 2. Merging with Remotes

- To solve,

![Untitled](Git%20and%20GitHub%20WriteUps%20images/Untitled%2028.png)

- Soution

```bash
$ git fetch
$ git checkout o/main
$ git merge side1
$ git merge side2
$ git merge side3
$ git checkout main
$ git merge C11
$ git push
```

## 3. Remote Tracking

- In this level, we learn about how to make main unchange in remote where we will be using `git checkout -b foo o/main` by which the main remains unchange and work is done in foo branch.
- To solve,

![Untitled](Git%20and%20GitHub%20WriteUps%20images/Untitled%2029.png)

- Solution

```bash
$ git checkout -b side o/main
$ git commit 
$ git fetch
$ git rebase o/main side
$ git push
```

## 4. Git Push Arguments

- `git push <remote> <place>` For e.g. `git push origin main`
- By specifying `main` as the "place" argument, we told git where the commits will *come from* and where the commits *will go*. It's essentially the "place" or "location" to synchronize between the two repositories.
- To solve,

![Untitled](Git%20and%20GitHub%20WriteUps%20images/Untitled%2030.png)

- Solution

```bash
$ git push origin main
$ git push origin foo
```

## 5. Git push arguments -- Expanded!

- If we want the source and destination to be different to do so, we simple join two place separated by the semi-colon `git push origin <source>:<destination>`. If branch is absent it creates new one
- To solve,

![Untitled](Git%20and%20GitHub%20WriteUps%20images/Untitled%2031.png)

- Solution

```bash
$ git push origin foo^:foo
$ git push origin foo^2:main
$ git push origin foo:main
$ git push origin main^:foo
```

## 6. Fetch Arguments

- So similar to `push` argument can be `fetch` as well? `fetch` argument is similar to the `push` argument.
- It is the same type of concept but applied in the opposite direction
- The `<place>` parameter will go to the branch, grab all the commits and then plop them down to the `o/<place>` branch locally.
- The `<souce>:<destination>` is also true.
- To solve,

![Untitled](Git%20and%20GitHub%20WriteUps%20images/Untitled%2032.png)

- Solution

```bash
$ git fetch origin C3:foo
$ git fetch origin C6:main
$ git checkout foo
$ git merge main
```

## 7. Source of Nothing

- Git abuses the `<source>` parameter in two weird ways. These two abuses come from the fact that you can technically specify "nothing" as a valid `source` for both git push and git fetch.
- To solve,

![Untitled](Git%20and%20GitHub%20WriteUps%20images/Untitled%2033.png)

- Solution,

```bash
$ git push origin :foo
$ git fetch origin :bar
```

## 8. Pull Arguments

- To solve,

![Untitled](Git%20and%20GitHub%20WriteUps%20images/Untitled%2034.png)

- Solution

```bash
$ git fetch origin C3:foo
$ git merge foo
$ git fetch origin C2:side
$ git merge side

OR,

$ git pull origin C3:foo
$ git pull origin C2:side
```