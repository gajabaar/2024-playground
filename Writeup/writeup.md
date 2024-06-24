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
