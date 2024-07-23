Introduction:
Git is a distributed version control system widely used for tracking changes in source code during software development. Created by Linus Torvalds in 2005, it allows multiple developers to work on a project simultaneously without interfering with each other's contributions. Git enables developers to save snapshots of their projects, called commits, which record the state of the project at specific points in time. These commits form a history, allowing developers to revert to previous versions if needed. Git's branching and merging features facilitate parallel development and integration of new features, making it an essential tool for modern software development workflows. Its popularity is further enhanced by platforms like GitHub and GitLab, which provide cloud-based repositories and collaboration features.

About GitLearning Website:
The website "Learn Git Branching" (https://learngitbranching.js.org/) is an interactive tutorial designed to help users understand and practice Git branching concepts. It provides a visual and hands-on approach to learning Git, making it easier to grasp the complexities of version control operations.
 
Level 1 Introduction Sequence:
Part 1: Introduction to Git commit
Git Commits:
A commit in a git repository records a snapshot of all the (tracked) files in your directory. It's like a giant copy and paste, but even better!

Git wants to keep commits as lightweight as possible though, so it doesn't just blindly copy the entire directory every time you commit. It can (when possible) compress a commit as a set of changes, or a "delta", from one version of the repository to the next.

Git also maintains a history of which commits were made when. That's why most commits have ancestor commits above them -- we designate this with arrows in our visualization. Maintaining history is great for everyone working on the project!

It's a lot to take in, but for now you can think of commits as snapshots of the project. Commits are very lightweight and switching between them is wicked fast!

Commands:
git commit
git commit

Explanation:
This command without any options will open the default text editor for you to enter a commit message. If you want to skip this step, you can use the -m option to provide a commit message directly from the command line.

Part 2: Branching in Git
Git Branches
Branches in Git are incredibly lightweight as well. They are simply pointers to a specific commit -- nothing more. This is why many Git enthusiasts chant the mantra:

branch early, and branch often
Because there is no storage / memory overhead with making many branches, it's easier to logically divide up your work than have big beefy branches.

When we start mixing branches and commits, we will see how these two features combine. For now though, just remember that a branch essentially says "I want to include the work of this commit and all parent commits."Solution:
 
Commands:
git checkout -b bugfix

Explanation:
This command is used to switch branches or restore working tree files. When used with the -b option, it creates a new branch and switches to it.

-b: This option tells Git to create a new branch
 

Part 3: Merging in Git
Branches and Merging
Great! We now know how to commit and branch. Now we need to learn some kind of way of combining the work from two different branches together. This will allow us to branch off, develop a new feature, and then combine it back in.

The first method to combine work that we will examine is git merge. Merging in Git creates a special commit that has two unique parents. A commit with two parents essentially means "I want to include all the work from this parent over here and this one over here, and the set of all their parents."

It's easier with visuals, let's check it out in the next view.

Commands:
git commit
git checkout main
git commit
git merge bugFix

Explanation:
git commit:
This command commits the staged changes to the local repository.
If you run git commit without any options, it will open the default text editor for you to enter a commit message.

git checkout main:
This command switches to the main branch.
If you are currently on a different branch (e.g., bugFix), this command will switch you back to the main branch.
 
git merge bugFix:
This command merges the changes from the bugFix branch into the current branch (main).
It incorporates the changes from the bugFix branch into the main branch

Part 4: Rebase Introduction
Git Rebase
The second way of combining work between branches is rebasing. Rebasing essentially takes a set of commits, "copies" them, and plops them down somewhere else.

While this sounds confusing, the advantage of rebasing is that it can be used to make a nice linear sequence of commits. The commit log / history of the repository will be a lot cleaner if only rebasing is allowed.

Let's see it in action...

Commands:
git commit
git checkout main
git commit
git checkout bugFix
git rebase main

Explanation:
git commit:
This command commits the staged changes to the local repository.
If you run git commit without any options, it will open the default text editor for you to enter a commit message.

git checkout main:
This command switches to the main branch.
If you are currently on a different branch (e.g., bugFix), this command will switch you back to the main branch.

git rebase main:
This command rebases the bugFix branch onto the main branch.
Rebasing takes the changes from your current branch (bugFix) and re-applies them on top of the main branch.
This effectively makes it as if your changes on bugFix were based on the most recent state of main.

Level 2 Ramping Up
Part 1: Detach yo’ Head
Moving around in Git
Before we get to some of the more advanced features of Git, it's important to understand different ways to move through the commit tree that represents your project.

Once you're comfortable moving around, your powers with other git commands will be amplified!

Commands:
git checkout c4

Explanation:
git checkout main:
This command switches to the main branch.
If you are currently on a different branch (e.g., bugFix), this command will switch you back to the main branch.

Part 2: Relative Refs (^)
Relative Refs
Moving around in Git by specifying commit hashes can get a bit tedious. In the real world you won't have a nice commit tree visualization next to your terminal, so you'll have to use git log to see hashes.

Furthermore, hashes are usually a lot longer in the real Git world as well. For instance, the hash of the commit that introduced the previous level is fed2da64c0efc5293610bdd892f82a58e8cbc5d8. Doesn't exactly roll off the tongue...

The upside is that Git is smart about hashes. It only requires you to specify enough characters of the hash until it uniquely identifies the commit. So I can type fed2 instead of the long string above.

Commands:
git checkout bugFix^
Explanation:
git checkout: 
This command is used to switch branches or restore working tree files.
bugFix^: The caret symbol (^) refers to the parent commit. When used after a branch name (e.g., bugFix), it specifies the parent of the latest commit on that branch.

 

Part 3: Relative Refs #2 (~)
The "~" operator
Say you want to move a lot of levels up in the commit tree. It might be tedious to type ^ several times, so Git also has the tilde (~) operator.

The tilde operator (optionally) takes in a trailing number that specifies the number of parents you would like to ascend. Let's see it in action.

Commands:
Git checkout HEAD ~1
Git branch -f bugFix HEAD~1

Explanation:
git checkout HEAD~1
git checkout: This command is used to switch branches or restore working tree files.
HEAD~1: This notation refers to the commit immediately preceding the current commit (the parent commit of HEAD).

Part 4: Reversing Changes in Git
Reversing Changes in Git
There are many ways to reverse changes in Git. And just like committing, reversing changes in Git has both a low-level component (staging individual files or chunks) and a high-level component (how the changes are actually reversed). Our application will focus on the latter.

There are two primary ways to undo changes in Git -- one is using git reset and the other is using git revert. We will look at each of these in the next dialog

Solution:
Commands:
Git checkout pushed
Git revert HEAD

Explanation:
git checkout pushed:
This command switches to the branch named pushed.
If the branch pushed exists, it will change your working directory to match the state of the pushed branch.
 
git revert HEAD:
This command creates a new commit that reverses the changes made by the most recent commit (HEAD).
It is used to undo changes introduced by the last commit while keeping the project's history intact. The new commit will contain the inverse of the changes made by the last commit.


Level 3 Moving Work Around
Part 1: Cherry-pick Intro
Moving Work Around
So far we've covered the basics of git -- committing, branching, and moving around in the source tree. Just these concepts are enough to leverage 90% of the power of git repositories and cover the main needs of developers.

That remaining 10%, however, can be quite useful during complex workflows (or when you've gotten yourself into a bind). The next concept we're going to cover is "moving work around" -- in other words, it's a way for developers to say "I want this work here and that work there" in precise, eloquent, flexible ways.

This may seem like a lot, but it's a simple concept.
Solution:
Commands:
git cherry-pick C3 C4 C7

Explanation:
git cherry-pick: This command applies the changes introduced by the specified commits onto your current branch.
 

Part 2: Interactive Rebase Intro
Git Interactive Rebase
Git cherry-pick is great when you know which commits you want (and you know their corresponding hashes) -- it's hard to beat the simplicity it provides.

But what about the situation where you don't know what commits you want? Thankfully git has you covered there as well! We can use interactive rebasing for this -- it's the best way to review a series of commits you're about to rebase.

Let's dive into the details...
Solution:
Commands:
git rebase -i overHere

Explanation:
git rebase -i: The -i flag stands for "interactive." This option allows you to interactively edit commits, which means you can modify, reorder, squash, or even delete commits as part of the rebase process.

Level 4 A Mixed Bag
Part 1: Grabbing Just 1 Commit
Locally stacked commits
Here's a development situation that often happens: I'm trying to track down a bug but it is quite elusive. In order to aid in my detective work, I put in a few debug commands and a few print statements.

All of these debugging / print statements are in their own commits. Finally I track down the bug, fix it, and rejoice!

Only problem is that I now need to get my bugFix back into the main branch. If I simply fast-forwarded main, then main would get all my debug statements which is undesirable. There has to be another way...
Solution:
 

Commands:
Git rebase -i main
Git rebase bugFix main

Explanation:
git rebase -i main
This command performs an interactive rebase of the current branch onto the main branch.

-i: This flag stands for "interactive," allowing you to edit commits during the rebase process.
main: This is the branch onto which you want to rebase your current branch.
 

Part 2: Juggling Commits
Juggling Commits
Here's another situation that happens quite commonly. You have some changes (newImage) and another set of changes (caption) that are related, so they are stacked on top of each other in your repository (aka one after another).

The tricky thing is that sometimes you need to make a small modification to an earlier commit. In this case, design wants us to change the dimensions of newImage slightly, even though that commit is way back in our history!!

Solution:
Commands:
git rebase -i HEAD~2 
$ git commit --amend
$ git rebase -i HEAD~2 
$ git rebase caption main

Explanation:
1. git rebase -i HEAD~2
This command starts an interactive rebase session for the last two commits before HEAD.
HEAD~2: This refers to the commit that is two steps before the current HEAD.
 

Part 3: Juggling Commits #2	
Juggling Commits #2
If you haven't completed Juggling Commits #1 (the previous level), please do so before continuing

As you saw in the last level, we used rebase -i to reorder the commits. Once the commit we wanted to change was on top, we could easily --amend it and re-order back to our preferred order.

The only issue here is that there is a lot of reordering going on, which can introduce rebase conflicts. Let's look at another method with git cherry-pick.
Solution:
Commands:
git checkout main
git cherry-pick C2
git commit --amend
git cherry-pick C3

Explanation:
git checkout main
This command switches your working directory to the main branch.

git cherry-pick C2
This command applies the changes from commit C2 to the main branch.

Part 4: Git Tags
Git Tags
As you have learned from previous lessons, branches are easy to move around and often refer to different commits as work is completed on them. Branches are easily mutated, often temporary, and always changing.

If that's the case, you may be wondering if there's a way to permanently mark historical points in your project's history. For things like major releases and big merges, is there any way to mark these commits with something more permanent than a branch?
Solution:
Commands:	
git tag v1 side~1
git tag v0 main~2
git checkout v1

Explanation:
git tag v1 side~1
This command creates a tag named v1 at the commit side~1.

git tag: This command is used to create a new tag.
v1: This is the name of the tag being created.
side~1: This specifies the commit where the tag should be placed. side~1 refers to the parent commit of side, meaning one commit before the side branch’s tip.

git tag v0 main~2
This command creates a tag named v0 at the commit main~2.

v0: This is the name of the tag being created.
main~2: This specifies the commit where the tag should be placed. main~2 refers to the commit that is two steps before the current tip of the main branch.  

Part 5: Git Describe
Git Describe
Because tags serve as such great "anchors" in the codebase, git has a command to describe where you are relative to the closest "anchor" (aka tag). And that command is called git describe!

Git describe can help you get your bearings after you've moved many commits backwards or forwards in history; this can happen after you've completed a git bisect (a debugging search) or when sitting down at the computer of a coworker who just got back from vacation.
Solution:
Commands:
git commit

Explanation:
Create a New Commit: When you run git commit, Git takes the changes you have staged (using git add) and creates a new commit in the repository's history. This new commit will have a unique SHA-1 hash and will include a commit message.

Level 5 Advanced Topics
Part 1: Rebasing over 9000 times
Rebasing Multiple Branches
Man, we have a lot of branches going on here! Let's rebase all the work from these branches onto main.

Upper management is making this a bit trickier though -- they want the commits to all be in sequential order. So this means that our final tree should have C7' at the bottom, C6' above that, and so on, all in order.

If you mess up along the way, feel free to use reset to start over again. Be sure to check out our solution and see if you can do it in fewer commands!
Solution:
Commands:
git rebase main bugFix
git rebase bugFix side
git rebase side another
git rebase another main

Explanation:
Rebase bugFix onto main: Git will take all the commits from the bugFix branch and reapply them on top of the main branch. This updates the bugFix branch with changes from main.

git rebase bugFix side
This command rebases the side branch onto the bugFix branch.

git rebase side another
This command rebases the another branch onto the side branch.

git rebase another main
This command rebases the main branch onto the another branch.

 

Part 2: Multiple parents
Specifying Parents
Like the ~ modifier, the ^ modifier also accepts an optional number after it.

Rather than specifying the number of generations to go back (what ~ takes), the modifier on ^ specifies which parent reference to follow from a merge commit. Remember that merge commits have multiple parents, so the path to choose is ambiguous.

Git will normally follow the "first" parent upwards from a merge commit, but specifying a number with ^ changes this default behavior.

Enough talking, let's see it in action.
Solution:


Commands:
git branch bugWork main^^2^

Explanation:
git branch: This is the Git command used to create, list, or delete branches.

bugWork: This is the name of the new branch you want to create.

main^^2^: This specifies the commit where the new branch should be created. It's a relative reference to the commit in the main branch.
 

Part 3: Branch Spaghetti
Branch Spaghetti
WOAHHHhhh Nelly! We have quite the goal to reach in this level.

Here we have main that is a few commits ahead of branches one two and three. For whatever reason, we need to update these three other branches with modified versions of the last few commits on main.

Branch one needs a re-ordering of those commits and an exclusion/drop of C5. Branch two just needs a pure reordering of the commits, and three only needs one commit transferred!

We will let you figure out how to solve this one -- make sure to check out our solution afterwards with show solution.
Solution:


Commands:
git checkout one
git cherry-pick C4 C3 C2
git checkout two
git cherry-pick C5 C4 C3 C2
git branch -f three C2

Explanation:
git checkout one
This command switches your working directory to the one branch.

git cherry-pick C4 C3 C2
This command applies the changes from commits C4, C3, and C2 onto the one branch.

git checkout two
This command switches your working directory to the two branch.

git cherry-pick C5 C4 C3 C2
This command applies the changes from commits C5, C4, C3, and C2 onto the two branch.

git branch -f three C2
This command forcefully moves the three branch to point to the commit C2




