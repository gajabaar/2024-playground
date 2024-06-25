# &#x20;A Mixed Bag&#x20;

### Level 1: Grabbing Just 1 Commit

**Objective:** Learn how to cherry-pick a single commit.

**Task:** Cherry-pick commit `C4` onto `main`.

<figure><img src=".gitbook/assets/ A Mixed Bag image 1.0.png" alt=""><figcaption></figcaption></figure>

* **Cherry-picking a Single Commit:**

```bash
git checkout main
git cherry-pick C4
```

### Level 2: Juggling Commits

**Objective:** Learn advanced commit manipulation techniques.

**Task:** Use interactive rebase and amend commits.

<figure><img src=".gitbook/assets/ A Mixed Bag image 2.0.png" alt=""><figcaption></figcaption></figure>

#### **Rebasing caption branch:**

```bash
git rebase -i caption~2
```

When we run the above command, Git will open the interactive rebase interface. Here, we need to arrange the commits. Arrange `C3` before `C2` by changing the order of the commits in the list.

Before:  &#x20;

```
pick C2
pick C3
```

<figure><img src=".gitbook/assets/ A Mixed Bag image 2.1.png" alt=""><figcaption></figcaption></figure>

After:

```
pick C3
pick C2
```

<figure><img src=".gitbook/assets/ A Mixed Bag image 2.2.png" alt=""><figcaption></figcaption></figure>

Save and close the interactive interface by clicking on Confirm button.

#### Amending the Commit:

```bash
git commit --amend
```

#### Starting Another Interactive Rebase:

Now, perform another interactive rebase to finalize the changes.

```bash
git rebase -i caption~2
```

The above command will again open interactive rebase interface, we need to arrange the commits again. This time, we have to ensure that the reordered commits from the previous steps are correctly positioned.

Before:

```
pick C3'
pick C2''
```

<figure><img src=".gitbook/assets/ A Mixed Bag image 2.3.png" alt=""><figcaption></figcaption></figure>

After:

```
pick C2''
pick C3'
```

<figure><img src=".gitbook/assets/ A Mixed Bag image 2.4.png" alt=""><figcaption></figcaption></figure>

Save and close the interactive interface by clicking on Confirm button.

#### Updating the `main` Branch:

Finally, force-update the `main` branch to point to the new commit structure.

```bash
git branch -f main caption
```

<figure><img src=".gitbook/assets/ A Mixed Bag image 2.5.png" alt=""><figcaption></figcaption></figure>

### Level 3: Juggling Commits #2

**Objective:** More advanced commit juggling.

**Task:** Cherry-pick and amend commits on `main`.

<figure><img src=".gitbook/assets/ A Mixed Bag image 3.0.png" alt=""><figcaption></figcaption></figure>

* **Cherry-picking and Amending:**

```bash
git checkout main
git cherry-pick C2
git commit --amend
git cherry-pick C3
```

### Level 4: Git Tags

**Objective:** Learn how to use Git tags.

**Task:** Tag commits `C1` and `C2`, and check out `C2`.

<figure><img src=".gitbook/assets/ A Mixed Bag image 4.png" alt=""><figcaption></figcaption></figure>

* **Creating and Using Tags:**

```bash
git tag v0 C1
git tag v1 C2
git checkout C2
```

### Level 5: Git Describe

**Objective:** Understand how to use `git describe`.

**Task:** Create a commit and use `git describe`.

<figure><img src=".gitbook/assets/ A Mixed Bag image 5.png" alt=""><figcaption></figcaption></figure>

* **Using `git describe`:**

```bash
git describe
git commit
```
