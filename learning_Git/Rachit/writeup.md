1.	Introduction to Git Commits
Task: The task is to make commits. 
Solution: 
Git Commit
Git Commit
Explanation: This command  creates a commit, which is like a snapshot of repository.  

2.	Branching in Git
Task: The task is to make a new branch named bugfix and switch to the branch. 

Solution:
git checkout -b bugfix

Explanation: This command lets user navigate between the branches created by git branch.

3.	Merging in Git
Task: The task is to make a new branch named bugFix and merge the branch bugFix into main.
 
Solution:
git checkout – b bugfix ; git commit 
git checkout main ; git commit 
git merge bugfix

Examination: This command creates s branch bugFix and commits any changes in the branch. then, it switches to main branch and commits any changes made in main. The git merge bugFix merges the bugFix branch to main branch. -


4.	Rebase Introduction
Task: The task is to create a branch named bugFix, commit once, go back to main, commit once, checkout to bugFix and rebase to main.
 
Solution:
git checkout – b bugfix ;git commit 
git checkout main ; git commit 
git checkout bugFix
git rebase main

Examination: This command creates a new branch bugFix, commits changes in both the bugFix branch and the main branch and then rebases the bug fix branch onto the main branch making it as if the changes in bugFix were made on top of the current state of main.

