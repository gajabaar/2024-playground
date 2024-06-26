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

# Ramping Up

## Level 1: Moving around in Git

**Description**

HEAD in Git refers to the currently checked-out commit, indicating what you're working on. It usually points to a branch name, like bugFix, and reflects the most recent commit in the working tree. When you make a commit, HEAD updates to show this change.

**Steps:**

- Analyze the goal

![Untitled](learninggitbranching%20js%20org%20lab%20Writeup%203bfa01ecd12a4cd2be2264988ab50b25/c2791a48-ab03-466f-973e-bdc7c86edfc5.png)

- Solve

![Untitled](learninggitbranching%20js%20org%20lab%20Writeup%203bfa01ecd12a4cd2be2264988ab50b25/99336515-a710-4e2f-8567-474deaca57c6.png)

## Level 2: Relative Refs

**Description**

Using commit hashes to navigate in Git can be tedious, especially since hashes are long and not easy to remember. While git log helps you see these hashes, Git only needs enough characters to uniquely identify a commit. For example, you can use fed2 instead of the full fed2da64c0efc5293610bdd892f82a58e8cbc5d8. Similarly, Specifying commits by their hash is inconvenient, so Git provides relative refs. These allow you to start from a memorable point (like a branch or HEAD) and move from there. Two simple relative refs are:

`^` to move up one commit
`~<num>` to move up a specified number of commits

**Steps:**

- Analyze the goal

![Untitled](learninggitbranching%20js%20org%20lab%20Writeup%203bfa01ecd12a4cd2be2264988ab50b25/Untitled%207.png)

- Solve

![Untitled](learninggitbranching%20js%20org%20lab%20Writeup%203bfa01ecd12a4cd2be2264988ab50b25/Untitled%208.png)

## Level 3: **The "~" operator**

**Description**

To move up multiple levels in the commit tree without repeatedly typing `^`, use the tilde `~` operator. The tilde can take a number to specify how many commits to ascend. For example, `~3` moves up three commits. Relative refs can be used to move branches. The `-f` option with git branch allows you to reassign a branch to a specific commit. For example, `git branch -f main HEAD~3` moves the main branch three commits behind HEAD. Note: This command can't be used on the currently checked-out branch.

**Steps:**

- Analyze the goal

![Untitled](learninggitbranching%20js%20org%20lab%20Writeup%203bfa01ecd12a4cd2be2264988ab50b25/Untitled%209.png)

- Solve

![Untitled](learninggitbranching%20js%20org%20lab%20Writeup%203bfa01ecd12a4cd2be2264988ab50b25/Untitled%2010.png)

## Level 4: **Reversing Changes in Git**

**Description**

Reversing changes in Git can be done at both low and high levels. The two primary methods are `git reset` and `git revert`.

- **Git Reset**

![Untitled](learninggitbranching%20js%20org%20lab%20Writeup%203bfa01ecd12a4cd2be2264988ab50b25/Untitled%2011.png)

- **Git Revert**

![Untitled](learninggitbranching%20js%20org%20lab%20Writeup%203bfa01ecd12a4cd2be2264988ab50b25/Untitled%2012.png)

**Steps:**

- Analyze the goal

![Untitled](learninggitbranching%20js%20org%20lab%20Writeup%203bfa01ecd12a4cd2be2264988ab50b25/Untitled%2013.png)

- Solve

![Untitled](learninggitbranching%20js%20org%20lab%20Writeup%203bfa01ecd12a4cd2be2264988ab50b25/Untitled%2014.png)

# Moving Work Around

## Level 1: Git Cherry-pick

**Description**

The `git cherry-pick` command copies specified commits to the current branch. It's straightforward and involves minimal complexity, making it easy to understand and use.

**Steps:**

- Analyze the goal

![Untitled](learninggitbranching%20js%20org%20lab%20Writeup%203bfa01ecd12a4cd2be2264988ab50b25/Untitled%2015.png)

- Solve

![Untitled](learninggitbranching%20js%20org%20lab%20Writeup%203bfa01ecd12a4cd2be2264988ab50b25/Untitled%2016.png)

## Level 2: **Git Interactive Rebase**

**Description**

`git cherry-pick` is ideal when you know the specific commits you want. For situations where you're unsure, interactive rebasing `git rebase -i` allows you to review and select commits in a UI. This method shows commit hashes and messages, helping you decide which commits to include.

**Steps:**

- Analyze the goal

![Untitled](learninggitbranching%20js%20org%20lab%20Writeup%203bfa01ecd12a4cd2be2264988ab50b25/Untitled%2017.png)

- Solve

![Untitled](learninggitbranching%20js%20org%20lab%20Writeup%203bfa01ecd12a4cd2be2264988ab50b25/Untitled%2018.png)

# A Mixed Bag

## Level 1:  Locally Stacked Commits

**Steps:**

- Analyze the goal

![Untitled](learninggitbranching%20js%20org%20lab%20Writeup%203bfa01ecd12a4cd2be2264988ab50b25/Untitled%2019.png)

- Solve

![Untitled](learninggitbranching%20js%20org%20lab%20Writeup%203bfa01ecd12a4cd2be2264988ab50b25/Untitled%2020.png)

## Level 2: **Juggling Commits**

**Steps:**

- Analyze the goal

![Untitled](learninggitbranching%20js%20org%20lab%20Writeup%203bfa01ecd12a4cd2be2264988ab50b25/Untitled%2021.png)

- Solve

![Untitled](learninggitbranching%20js%20org%20lab%20Writeup%203bfa01ecd12a4cd2be2264988ab50b25/Untitled%2022.png)

## Level 3: **Juggling Commits #2**

**Steps:**

- Analyze the goal

![Untitled](learninggitbranching%20js%20org%20lab%20Writeup%203bfa01ecd12a4cd2be2264988ab50b25/Untitled%2023.png)

- Solve

![Untitled](learninggitbranching%20js%20org%20lab%20Writeup%203bfa01ecd12a4cd2be2264988ab50b25/Untitled%2024.png)

## Level 4:  Git Tags

**Description**

Branches in Git are flexible and change often, but tags provide a way to permanently mark significant commits, like major releases. Unlike branches, tags don't move and act as fixed anchors in the commit history.

**Steps:**

- Analyze the goal

![Untitled](learninggitbranching%20js%20org%20lab%20Writeup%203bfa01ecd12a4cd2be2264988ab50b25/Untitled%2025.png)

- Solve

![Untitled](learninggitbranching%20js%20org%20lab%20Writeup%203bfa01ecd12a4cd2be2264988ab50b25/Untitled%2026.png)

## Level 5:  Git Describe

**Description**

Git tags act as anchors in the codebase, and `git describe` helps you identify your position relative to the nearest tag. The command `git describe <ref>` shows the closest tag, number of commits since that tag, and the current commit hash.

**Steps:**

- Analyze the goal

![Untitled](learninggitbranching%20js%20org%20lab%20Writeup%203bfa01ecd12a4cd2be2264988ab50b25/Untitled%2027.png)

- Solve

![Untitled](learninggitbranching%20js%20org%20lab%20Writeup%203bfa01ecd12a4cd2be2264988ab50b25/Untitled%2028.png)
