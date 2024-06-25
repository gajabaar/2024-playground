# Introduction Sequence

### Level 1: Commits in Git

**Objective:** Learn the basic git commit commands.

**Task:** Just type in `git commit` twice to finish!

<figure><img src=".gitbook/assets/Introduction Sequence Image 1.png" alt=""><figcaption></figcaption></figure>

* **Creating a Commit:**

```bash
git commit
git commit
```

### Level 2: Branching in Git

**Objective:** Understand how to create and switch branches. **Task:** Make a new branch with `git branch` and check it out with `git checkout`.

<figure><img src=".gitbook/assets/Introduction Sequence Image 2.png" alt=""><figcaption></figcaption></figure>

* **Creating and Switching to `bugFix` Branch:**

```bash
git branch bugFix
git checkout bugFix
```

### Level 3: Merging Branches

**Objective:** Learn how to merge branches.&#x20;

**Task:** Merge `bugFix` into `main`.

<figure><img src=".gitbook/assets/Introduction Sequence Image 3.png" alt=""><figcaption></figcaption></figure>

* **Merging `bugFix` into `main`:**

```bash
git branch bugFix
git checkout bugFix
git commit
git checkout main
git commit
git merge bugFix
```

### Level 4: Rebasing in Git

**Objective:** Learn how to rebase branches.&#x20;

**Task:** Rebase `bugFix` branch onto `main`.

<figure><img src=".gitbook/assets/Introduction Sequence Image 4.png" alt=""><figcaption></figcaption></figure>

* **Creating and rebasing `bugFix` to `main` Branch:**

```bash
git branch bugFix
git checkout bugFix
git commit
git checkout main
git commit
git checkout bugFix
git rebase main
```
