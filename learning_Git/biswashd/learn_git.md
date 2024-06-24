# Github writeups

Link : https://learngitbranching.js.org/

# You can see all the commands available with show commands at the terminal.

# Introduction Sequence

## Level : Introduction to Git Commits
- A commit in a git repository records a snapshot of all the (tracked) files in your directory. It's like a giant copy and paste, but even better!.
- Git also maintains a history of which commits were made when, so most commits have ancestor commits above them.
- Git keeps commits lightweight by compressing them as a set of changes from one version to the next, instead of copying the entire directory every time.

### Goal to reach
![demo_practice](md_images/thirdimg_3.jpg)

**Just type in "git commit" twice to finish!**

```bash
$ git commit
$ git commit
```

## Level : Branching in Git
- Branches in Git are incredibly lightweight as well.They are simply pointers to a specific commit.
- This is why many Git enthusiasts chant the mantra:
```
branch early, and branch often
```
- A branch includes the work of its commit and all parent commits.
- When we start mixing branches and commits, we will see how these two features combine. For now though, just remember that a branch essentially says "I want to include the work of this commit and all parent commits."

- In Git version 2.23, a new command called `git switch` was introduced to eventually replace `git checkout`, which is somewhat overloaded (it does a bunch of different things depending on the arguments)

### Goal to reach
- Make a new branch with "git branch " and check it out with "git checkout "
![Goal_Branching_in_git](md_images/Goal_branchinggitimg_7.jpg)

- If you want to create a new branch AND check it out at the same time, you can simply type:
`git checkout -b [yourbranchname]`

### To solve
```
git checkout -b bugFix
```

## Level 3 : Merging in git
- After learning how to commit and branch, the next step is combining work from different branches. This allows us to develop new features separately and then integrate them back into our main branch.
- Using git merge, we create a special commit with two unique parents. This commit effectively incorporates changes from two branches, along with their entire histories, into one cohesive unit. This process streamlines collaborative development and maintains project organization.

### Goal to reach

![Goal_merging_in_git](md_images/Merging_gitimg_8.jpg)

### To complete this level, do the following steps:
- Make a new branch called `bugFix`
- Checkout the `bugFix` branch with `git checkout bugFix`
- Commit once
- Go back to `main` with `git checkout`
- Commit another time
- Merge the branch `bugFix` into `main` with `git merge`

```bash
$ git checkout -b bugFix
$ git commit
$ git checkout main
$ git commit
$ git merge bugFix
```

## Level 4 : Rebase Introduction
- Another way to combine work between branches is `git rebase`. Rebasing takes a set of commits, "copies" them, and applies them elsewhere.
- The advantage of rebasing is that it can be used to make a nice linear sequence of commits.
- The commit log / history of the repository will be a lot cleaner if only rebasing is allowed.

### Goal
![Goal_merging_in_git](md_images/rebase_branchimg_9.jpg)

### To complete this level, do the following

- Checkout a new branch named `bugFix`
- Commit once
- Go back to main and commit again
- Check out bugFix again and rebase onto main

```bash
$ git checkout -b bugFix
$ git commit
$ git checkout main
$ git commit
$ git checkout bugFix
$ git rebase main
```

### Ramping Up