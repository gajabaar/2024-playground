Git commit:
A commit in git repository record a snapshot of all tracked files  in your dir
Keeps commits lightweight as possible
Compress changes as a set of changes
Maintain history of what changes were made
Commit -> Snapshot or projects
Lightweight and switching bet'n them is wicked fast


Level 1 -> Intro to Git commit
	There are two commit in small repository C0 & C1
	git commit then we add again one commit
	C0 C1 C2
Objective: 
Make two commits

git commit
git commit


![[Pasted image 20240623225817.png]]

---

Level 2 -> Branching in git
Branch are simply pointer to commits
Git Sutra 
```
branch early, and branch often
```
Git branch help in development of specific feature & part of projects

	When we start mixing branches and commits, we will see how these two features combine. For now though, just remember that a branch essentially says "I want to include the work of this commit and all parent commits."
To create new branch we use
git branch branch_name
-> git branch headline
next commit will include branch changes


If we commit directly then branch image will not move
we need to tell git to checkout so
git checkout branch_name

```
git checkout headline;
git commit
```

Then our changes were recorded into new branches

_Note: In Git version 2.23, a new command called `git switch` was introduced to eventually replace `git checkout`, which is somewhat overloaded (it does a bunch of different things depending on the arguments). The lessons here will still use `checkout` instead of `switch` because the `switch` command is still considered experimental and the syntax may change in the future. However you can still try out the new `switch` command in this application, and also [learn more here](https://git-scm.com/docs/git-switch)._

To create a branch and check it out at same time
 `git checkout -b [yourbranchname]`


Objective : Create a branch bugFix and checkout branch

git branch bugFix
git checkout bugFix
git commit

![[Pasted image 20240623225938.png]]

---

Level 3 ->  Git Merge
Objective 

To complete this level, do the following steps:

- Make a new branch called `bugFix`
- Checkout the `bugFix` branch with `git checkout bugFix`
- Commit once
- Go back to `main` with `git checkout`
- Commit another time
- Merge the branch `bugFix` into `main` with `git merge`

_Remember, you can always re-display this dialog with "objective"!_

So comamnds would be

git checkout -b bugFIx / git branch bugFix; git checkout bugFix
git commit
git checkout main
git commit
git merge bugFix

![[Pasted image 20240623230349.png]]


---

Level 4 -> Git Rebase

Git Rebase
Combining work between branches is rebasing. takes set of commit copies them and plops them somewhere else
the advantage of rebasing is that it can be used to make a nice linear sequence of commits. The commit log / history of the repository will be a lot cleaner if only rebasing is allowed.

Objective:
To complete this level, do the following

- Checkout a new branch named `bugFix`
- Commit once
- Go back to main and commit again
- Check out bugFix again and rebase onto main

Good luck!

To solve this challenge:
git checkout -b bugFix
Git commit
git checkout main
git commit
git checkout bugFix
git rebase main



![[Pasted image 20240623232213.png]]

---

Head
 HEAD is the symbolic name for the currently checked out commit -- it's essentially what commit you're working on top of.

HEAD always points to the most recent commit which is reflected in the working tree. Most git commands which make changes to the working tree will start by changing HEAD.

Normally HEAD points to a branch name (like bugFix). When you commit, the status of bugFix is altered and this change is visible through HEAD.


Detaching HEAD

Detaching HEAD just means attaching it to a commit instead of a branch. This is what it looks like beforehand:

HEAD -> main -> C1

git checkout C1



And now it's

HEAD -> C1

To complete this level we just have to detach the head
we can do that by git checkout C4



---

Relative Refs

Git logs -> To find the commit hashes
		Need to specify enough character in hash until it uniquely identify the commit
		To identify fed2da64c0efc5293610bdd892f82a58e8cbc5d8
		we can just type fed2 instead of long string abole

With relative refs, you can start somewhere memorable (like the branch `bugFix` or `HEAD`) and work from there.

Relative commits are powerful, but we will introduce two simple ones here:

- Moving upwards one commit at a time with `^`
- Moving upwards a number of times with `~<num>`


To complete this level we can use commands

git checkout bugFix^

^ to go to above head
if we want to go above it then we can use git checkout bugFix^ ; git checkout bugFix^;git checkout bugFix^;git checkout bugFix^;


## Relative Refs 2

The "~" operator

Say you want to move a lot of levels up in the commit tree. It might be tedious to type `^` several times, so Git also has the tilde (~) operator.

The tilde operator (optionally) takes in a trailing number that specifies the number of parents you would like to ascend. Let's see it in action.

 git checkout bugFix^ ; git checkout bugFix^; git checkout bugFix^; git checkout bugFix^;

EQUIVALENT to 

git checkout HEAD~4

One of the most common ways I use relative refs is to move branches around. You can directly reassign a branch to a commit with the `-f` option. So something like:

`git branch -f main HEAD~3`

moves (by force) the main branch to three parents behind HEAD.

_Note: In a real git environment `git branch -f command` is not allowed for your current branch._

`git branch -f main HEAD~3`  -> moves to 3 way above head
-f to forcibly move the head or another parts


SOLUTION: 
git checkout head~1 for head to transfer head on C1
git branch -f main C6
git branch -f bugFix C0




---

## Reversing Changes in Git

Two ways to reverse change in Git
- git reset
- git revert


## Git Reset

`git reset` reverses changes by moving a branch reference backwards in time to an older commit. In this sense you can think of it as "rewriting history;" `git reset` will move a branch backwards as if the commit had never been made in the first place.

## Git Revert

While resetting works great for local branches on your own machine, its method of "rewriting history" doesn't work for remote branches that others are using.

In order to reverse changes and _share_ those reversed changes with others, we need to use `git revert`.

To complete level:

Git checkout pushed
git revert head
git checkout local
git reset HEAD~1


---

# Moving work around

Level 1 -> Cherry Pick Intro

Cherry Pick
`git cherry-pick`.

- `git cherry-pick <Commit1> <Commit2> <...>`

it is used to pick copy certain commit into main. If we select commits and added into main then we can get it plopped down into our main.

To complete this level
We use command 

git cherry-pick C3 C4 C7 to copy all commits into main



---

Level 2 ->  Interactive rebase intro

Git cherry-pick is great when you know which commits you want (and you know their corresponding hashes) -- it's hard to beat the simplicity it provides.

But what about the situation where you don't know what commits you want? Thankfully git has you covered there as well! We can use interactive rebasing for this -- it's the best way to review a series of commits you're about to rebase.

Interactive rebase
All interactive rebase means Git is using the `rebase` command with the `-i` option.

If you include this option, git will open up a UI to show you which commits are about to be copied below the target of the rebase. It also shows their commit hashes and messages, which is great for getting a bearing on what's what.

When the interactive rebase dialog opens, you have the ability to do two things in our educational application:

You can reorder commits simply by changing their order in the UI (via dragging and dropping with the mouse).
You can choose to keep all commits or drop specific ones. When the dialog opens, each commit is set to be included by the pick button next to it being active. To drop a commit, toggle off its pick button.


To complete this level 
git rebase -i C1
drop C2 while arranging all other commit on order.


---

# A mixed Bag

Level 1 -> Grabbing just one commit

What if we want to copy one of our commit to our main. Grabbing only one commit is the way to solve this problem 

To solve this problem
we can use 
-git cherry-pick
-git rebase -i 

To solve this level 
git switch main
git cherry-pick C4

boom** solved


---

Level 2 -> Juggling Commits

To solve this level

	git rebase -i main  [switch order bet'n C2 and C3]
	git commit --amend
	git rebase -i main
	git switch main
	git merge caption
Level completed.





---

