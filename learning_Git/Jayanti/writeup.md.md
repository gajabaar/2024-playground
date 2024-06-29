# learninggitbranching.js.org lab Writeup

# Section 1: Introduction Sequence

## Level 1: Introduction to git commits

**Description:**

A commit in a Git repository records a snapshot of all tracked files in your directory. Instead of copying the entire directory each time, Git efficiently compresses changes (deltas) from one version to the next.

**Steps:** 

- Analyze the goal

![level1_goal.png](learninggitbranching%20js%20org%20lab%20Writeup%203bfa01ecd12a4cd2be2264988ab50b25/level1_goal.png)

- Solve

![Untitled](learninggitbranching%20js%20org%20lab%20Writeup%203bfa01ecd12a4cd2be2264988ab50b25/Untitled.png)

## Level 2: Git Branches

**Description:**

Branches in Git are lightweight pointers to specific commits, allowing you to easily create and manage many branches without significant overhead. This makes it practical to branch early and often, facilitating organized and logical work division.

**Steps:** 

- Analyze the goal

![Untitled](learninggitbranching%20js%20org%20lab%20Writeup%203bfa01ecd12a4cd2be2264988ab50b25/Untitled%201.png)

- Solve

![Untitled](learninggitbranching%20js%20org%20lab%20Writeup%203bfa01ecd12a4cd2be2264988ab50b25/Untitled%202.png)

## Level 3: Branches and Merging

**Description:**

Now that we know how to commit and branch, we need to combine work from different branches. The first method we'll explore is git merge. Merging creates a commit with two parents, indicating it includes work from both branches and their histories. Let's see how this works visually next.

**Steps:** 

- Analyze the goal

![Untitled](learninggitbranching%20js%20org%20lab%20Writeup%203bfa01ecd12a4cd2be2264988ab50b25/Untitled%203.png)

- Solve

![Untitled](learninggitbranching%20js%20org%20lab%20Writeup%203bfa01ecd12a4cd2be2264988ab50b25/Untitled%204.png)

## Level 4: Git Rebase

**Description**

The second way to combine work between branches is rebasing. Rebasing copies commits and places them onto another branch, creating a linear commit history. This results in a cleaner and more readable commit log.

**Steps:**

- Analyze the goal

![Untitled](learninggitbranching%20js%20org%20lab%20Writeup%203bfa01ecd12a4cd2be2264988ab50b25/Untitled%205.png)

- Solve

![Untitled](learninggitbranching%20js%20org%20lab%20Writeup%203bfa01ecd12a4cd2be2264988ab50b25/Untitled%206.png)