# Ramping Up

### Level 1: Detach yo’ HEAD

**Objective:** Understand how to detach HEAD and move it to a specific commit.

**Task:** Move HEAD to the commit `C4`.

<figure><img src=".gitbook/assets/ Ramping Up image 1.png" alt=""><figcaption></figcaption></figure>

* **Detaching HEAD to `C4`:**

```bash
git checkout C4
```

### Level 2: Relative Refs (^)

**Objective:** Use caret (^) to navigate to the parent commit.

**Task:** Move HEAD to the parent of `C4` using `^`.

<figure><img src=".gitbook/assets/ Ramping Up image 2.png" alt=""><figcaption></figcaption></figure>

* **Moving HEAD to Parent of `C4`:**

```bash
git checkout C4^
```

### Level 3: Relative Refs #2 (\~)

**Objective:** Use tilde (\~) to navigate multiple commits back.

**Task:** Update branches and move HEAD to commit `C1`.

<figure><img src=".gitbook/assets/ Ramping Up image 3.png" alt=""><figcaption></figcaption></figure>

* **Updating Branches and Moving HEAD:**

```bash
git branch -f main C6
git branch -f bugFix C0
git checkout C1
```

### Level 4: Reversing Changes in Git

**Objective:** Learn how to reverse changes using `git reset` and `git revert`.

**Task:** Reset to a previous commit and revert changes on a branch.

<figure><img src=".gitbook/assets/ Ramping Up image 4.png" alt=""><figcaption></figcaption></figure>

* **Resetting and Reverting Changes:**

```bash
git reset local~1
git checkout pushed
git revert pushed
```
