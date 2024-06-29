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

##Level 1 : Detach yo' HEAD

## Head
- In Git, "HEAD" is the symbolic reference to the current commit you're working on. It points to the latest commit in your working directory. Most Git commands that modify the working directory start by updating HEAD.

- Typically, HEAD points to a branch name (e.g., bugFix). When you make a commit, it updates the branch's status, which is reflected by HEAD.

- Detaching HEAD just means attaching it to a commit instead of a branch.
- This is what it looks like beforehand:HEAD -> main -> C1 then perform `git checkout c1` And now it's HEAD -> C1.

### Goal to reach
![goal to reach](md_git_images/detach_goal.png)

### To solve this level 
- To complete this level, let's detach HEAD from bugFix and attach it to the commit instead.

```
git checkout c4
```

## level 2: Relative Refs (^)

- Navigating Git using commit hashes can be cumbersome, especially since you don't have a visual commit tree in the terminal. You'll need to use git log to view these hashes.

- Hashes in Git are long and complex, like `fed2da64c0efc5293610bdd892f82a58e8cbc5d8`. However, Git allows you to use shortened versions of these hashes. You only need to type enough characters to uniquely identify the commit, such as `fed2` instead of the full hash.

- specifying commits by their hash isn't the most convenient thing ever, which is why Git has relative refs.

- Relative commits are powerful, but we will introduce two simple ones here:

- Moving upwards one commit at a time with `^`
- Moving upwards a number of times with `~<num>`


### Goal to reach
![goal to reach](md_git_images/relative_ref.png)


### To solve this level
- To complete this level, check out the parent commit of bugFix. This will detach HEAD.

- So saying bugFix^ is equivalent to "the first parent of main".

## to solve type
```
git checkout C4
```

## level 3: Relative Refs #2 (~)

# `~` operator
- The `~` operator in Git lets you move up multiple levels in the commit tree easily by specifying a number, like `git checkout HEAD~3` to go up three commits, instead of using ^ repeatedly.

### Branch forcing
- Branch forcing allows you to reassign a branch to a different commit using relative references. For example, `git branch -f main HEAD~3` forcefully moves the main branch to the commit three levels up from HEAD. Note: In a real Git environment, you cannot use git branch -f on the current branch.

### Goal to reach
![goal to reach](md_git_images/relative_ref2.png)

### To solve this level
- To complete this level, move `HEAD`, `main`, and `bugFix` to their goal destinations shown.

```
git branch -f main C6
git branch -f bugFix C0
git checkout C2^
```

## level 4: Reversing Changes in Git
- There are many ways to reverse changes in Git.And just like committing, reversing changes in Git has both a low-level component (staging individual files or chunks) and a high-level component (how the changes are actually reversed).

- There are two primary ways to undo changes in Git -- one is using git reset and the other is using git revert.

### Git reset
- git reset reverses changes by moving a branch reference backwards in time to an older commit. In this sense you can think of it as "rewriting history;" git reset will move a branch backwards as if the commit had never been made in the first place.`git reset HEAD~1`

### Git revert
- While resetting works great for local branches on your own machine, its method of "rewriting history" doesn't work for remote branches that others are using.
- In order to reverse changes and share those reversed changes with others, we need to use `git revert`.
- `git revert HEAD`

### Goal to reach
![revert](md_git_images/revert_img.png)

### To solve this Level
- To complete this level, reverse the most recent commit on both local and pushed. You will revert two commits total (one per branch).

```
$ git reset local~1

$ git checkout pushed

$ git revert pushed
```



## Moving Work Around

# Level 1 : Cherry-pick Intro

`"I want this work here and that work there"`

`git cherry-pick <Commit1> <Commit2> <...>`
- It's a very straightforward way of saying that you would like to copy a series of commits below your current location (HEAD).

`git cherry-pick C2 C4`

### Goal to reach
![cherry_pick_goal](md_git_images/cherry_pick.png)

### To solve this lab
- To complete this level, simply copy some work from the three branches shown into main. You can see which commits we want by looking at the goal visualization.

```
git cherry-pick C3 C4 C7
```

# Level 2 : Interactive Rebase Intro
- Git cherry-pick is ideal for applying specific commits when you know their hashes. For situations where you don't know which commits to pick, interactive rebasing lets you review and select commits during the rebase process.
- Interactive rebase in Git uses the `rebase -i` command

`git rebase -i HEAD~4`

- To finish this level, do an interactive rebase and achieve the order shown in the goal visualization.

### Goal to reach
![Interactive_rebase](md_git_images/interactive_rebase.png)

### To solve this level

```
git rebase -i HEAD~4
```


## A Mixed Bag
# Level 1 : Grabbing Just 1 Commit
- The only problem is to get ```bugFix``` into ```main``` to get all debug statements into main.

### Goal to reach
![local_stacked_commits](md_git_images/Stacked_commit.png)
**Commands to be used:**<br>
```git rebase -i```<br>
```git cherry-pick```

### To solve this level
```
git checkout main
git cherry-pick c4
```

# Level 2 : Juggling Commits
**Problem:**<br>
- You have some changes (newImage) and another set of changes (caption) that are related, so they are stacked on top of each other in your repository (aka one after another).
- to change the dimensions of newImage slightly, even though that commit is way back in our history.

## Goal to reach
![modification_commit](md_git_images/jugggling_commit.png)

### To solve this lab
```
$ git checkout caption
$ git rebase -i HEAD~2
$ git commit --amend
$ git rebase -i HEAD~2
$ git checkout main
$ git merge caption
```

# Level 3 :Juggling Commits #2

- In the last level, we used `rebase -i` to reorder the commits.
- Once the commit we wanted to change was on **Top**, we could easily `--amend` it and re-order back to our preferred order.
- only issue here is that there is a lot of reordering going on, which can introduce rebase conflicts. 

## Another method with cherry-pick
- git cherry-pick will plop down a commit from anywhere in the tree onto HEAD.

### Goal to reach
1. accomplish the same objective of amending C2 once but avoid using rebase -i.
![juggling2_commit](md_git_images/jugglingcommit#2.png)

### To solve this level
```
git checkout main

$ git cherry-pick C2

$ git commit --amend

$ git cherry-pick C3
```

# Level 4 :Git Tags
- Branches are easily mutated, often temporary, and always changing.
- Tags never move as more commits are created. You can't "check out" a tag and then complete work on that tag -- tags exist as anchors in the commit tree that designate certain spots.

### Goal to reach 
1. For this level just create the tags in the goal visualization and then check v1 out. Notice how you go into detached HEAD state -- this is because you can't commit directly onto the v1 tag.

![juggling2_commit](md_git_images/git_tag.png)

### To solve this lab

```
git tag v0 C1
git tag v1 C2
git checkout HEAD~1
 ```


# Level 5 : Git Describe
Because tags serve as such great "anchors" in the codebase, git has a command to describe where you are relative to the closest "anchor" (aka tag). And that command is called git describe!
Git describe can help you get your bearings after you've moved many commits backwards or forwards in history; this can happen after you've completed a git bisect (a debugging search) or when sitting down at the computer of a coworker who just got back from vacation.
Git describe takes the form of:
`git describe <ref>`
Where `<ref>` is anything git can resolve into a commit. If you don't specify a ref, git just uses where you're checked out right now (HEAD).

The output of the command looks like:
`<tag>_<numCommits>_g<hash>`
Where tag is the closest ancestor tag in history, numCommits is how many commits away that tag is, and `<hash>` is the hash of the commit being described.

## Goal to reach

![Git_describe](md_git_images/git_describe.png)

### To solve this level
```
git commit
```

### **Advanced topic**

## Level 1 : Rebasing over 9000 times

## problem
- to rebase all work from branches onto main
- the commits wants all to be in sequential order

### Goal to reach
![Git_describe](md_git_images/git_describe.png)

### To solve this level
```
git rebase main bugFix

$ git rebase bugFix side

$ git rebase side another

$ git rebase another main
```
**OR**
```
git checkout bugFix
git rebase main
git checkout side
git rebase -i bugFix
git checkout another
git rebase side
git checkout main
git merge another
```
### refer : https://denizsivas.medium.com/learn-git-branching-interactively-9c43d3e26556


## Level 2 : Multiple Parents
1. Like the `~` modifier, the `^` modifier also accepts an optional number after it.
2. Rather than specifying the number of generations to go back (what `~`takes), the modifier on `^` specifies which parent reference to follow from a merge commit.
3. Remember that merge commits have multiple parents, so the path to choose is ambiguous.
4. Git will normally follow the "first" parent upwards from a merge commit, but specifying a number with `^`

### Goal to reach 
![Git_modifiers](md_git_images/modifiers.png)

### To solve this level
1. To complete this level, create a new branch at the specified destination by using modifiers `^` & `~`

```
git branch bugWork HEAD~^2~
```

## Level 3 : Branch Spaghetti
1. Here we have `main` that is a few commits ahead of branches `one` `two` and `three`. For whatever reason, we need to update these three other branches with modified versions of the last few commits on main.
2. Branch one needs a re-ordering of those commits and an exclusion/drop of C5. Branch two just needs a pure reordering of the commits, and three only needs one commit transferred!.

### Goal to Reach 

![Git_modifiers](md_git_images/modifiers.png)


### To solve this level
```
git rebase C2 three

Fast forwarding...

$ git checkout one

$ git cherry-pick C4 C3 C2

$ git checkout two

$ git cherry-pick C5 C4 C3 C2
```