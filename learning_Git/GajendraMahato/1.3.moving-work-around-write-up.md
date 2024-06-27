# &#x20;Moving Work Around&#x20;

### Level 1: Cherry-pick Intro

**Objective:** Learn how to cherry-pick specific commits.

**Task:** Cherry-pick commits `C3`, `C4`, and `C7`.

<figure><img src=".gitbook/assets/ Moving Work Around  image 1.png" alt=""><figcaption></figcaption></figure>

* **Cherry-picking Commits:**

```bash
git cherry-pick C3 C4 C7
```

### Level 2: Interactive Rebase Intro

**Objective:** Understand how to use interactive rebase.

**Task:** Rebase interactively, remove `C2`, and move `C5` up.

<figure><img src=".gitbook/assets/ Moving Work Around  image 2.png" alt=""><figcaption></figcaption></figure>

* **Interactive Rebase:**

```bash
git rebase -i HEAD~4
#Interactive work: Remove/Omit C2, move C5 up in between C2 and c4
```
