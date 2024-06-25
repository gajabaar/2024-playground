# Introduction Sequence

### Level 1: Commits in Git

**Objective:** Learn the basic git commit commands.

**Task:** Just type in `git commit` twice to finish!

* **Creating a Commit:**

```bash
git commit
git commit
```

<figure><img src=".gitbook/assets/Introduction Sequence Level 1.png" alt=""><figcaption></figcaption></figure>

### Level 2: Branching in Git

**Objective:** Understand how to create and switch branches. **Task:** Make a new branch with `git branch` and check it out with `git checkout`.

* **Creating and Switching to `bugFix` Branch:**

```bash
git branch bugFix
git checkout bugFix
```

<figure><img src=".gitbook/assets/Introduction Sequence Level 2.png" alt=""><figcaption></figcaption></figure>

### Level 3: Merging Branches

**Objective:** Learn how to merge branches. **Task:** Merge `bugFix` into `main`.

* **Merging `bugFix` into `main`:**

```bash
git branch bugFix
git checkout bugFix
git commit
git checkout main
git commit
git merge bugFix
```

<figure><img src=".gitbook/assets/Introduction Sequence Level 3.png" alt=""><figcaption></figcaption></figure>

### Level 4: Rebasing in Git

**Objective:** Learn how to rebase branches. **Task:** Rebase `bugFix` branch onto `main`.

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

<figure><img src=".gitbook/assets/Introduction Sequence Level 4.png" alt=""><figcaption></figcaption></figure>
