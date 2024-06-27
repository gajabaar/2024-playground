# Moving Work Around

In this document, we will explore more features of Git such as cherry-picking and interactive rebase. Each section will include commands and explanations for what each command does.

## 1: Cherry-Pick intro
Cherry-picking allows specific commits to be applied to a branch, useful for selectively integrating changes.
```sh
git cherry-pick C3 C4 C7
```

## 2: Interactive Rebase intro
Interactive rebasing lets you modify commit history by rearranging or deleting commits interactively.

```sh
git rebase -i HEAD~4
```
Then Remove C2 and order as C3, C5 and C4.

This section helps us organize our git tree and interactively choose and pick the order of commits we want applied.