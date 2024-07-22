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

 

Part 2: Branching in Git
Git Branches
Branches in Git are incredibly lightweight as well. They are simply pointers to a specific commit -- nothing more. This is why many Git enthusiasts chant the mantra:

branch early, and branch often
Because there is no storage / memory overhead with making many branches, it's easier to logically divide up your work than have big beefy branches.

When we start mixing branches and commits, we will see how these two features combine. For now though, just remember that a branch essentially says "I want to include the work of this commit and all parent commits."Solution:
 

Commands:
git checkout -b bugfix

Explanation:

 

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

 

Part 4: Rebase Introduction
Git Rebase
The second way of combining work between branches is rebasing. Rebasing essentially takes a set of commits, "copies" them, and plops them down somewhere else.

While this sounds confusing, the advantage of rebasing is that it can be used to make a nice linear sequence of commits. The commit log / history of the repository will be a lot cleaner if only rebasing is allowed.

Let's see it in action...

Solution:
 

Commands:
git commit
git checkout main
git commit
git checkout bugFix
git rebase main

Explanation:


 


Level 2 Ramping Up
Part 1: Detach yo’ Head
Moving around in Git
Before we get to some of the more advanced features of Git, it's important to understand different ways to move through the commit tree that represents your project.

Once you're comfortable moving around, your powers with other git commands will be amplified!
Solution:
 

Commands:
git checkout c4
Explanation:


 

Part 2: Relative Refs (^)
Relative Refs
Moving around in Git by specifying commit hashes can get a bit tedious. In the real world you won't have a nice commit tree visualization next to your terminal, so you'll have to use git log to see hashes.

Furthermore, hashes are usually a lot longer in the real Git world as well. For instance, the hash of the commit that introduced the previous level is fed2da64c0efc5293610bdd892f82a58e8cbc5d8. Doesn't exactly roll off the tongue...

The upside is that Git is smart about hashes. It only requires you to specify enough characters of the hash until it uniquely identifies the commit. So I can type fed2 instead of the long string above.

Solution:
 

Commands:
git checkout bugFix^
Explanation:


 

Part 3: Relative Refs #2 (~)
The "~" operator
Say you want to move a lot of levels up in the commit tree. It might be tedious to type ^ several times, so Git also has the tilde (~) operator.

The tilde operator (optionally) takes in a trailing number that specifies the number of parents you would like to ascend. Let's see it in action.

Solution:

 

Commands:
Git checkout HEAD ~1
Git branch -f bugFix HEAD~1
Explanation:

 

Part 4: Reversing Changes in Git

