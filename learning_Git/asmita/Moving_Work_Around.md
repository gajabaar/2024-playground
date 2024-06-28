# MOVING WORK AROUND

## LEVEL 1: CHERRY-PICK INTRO

The first command in this series is called `git cherry-pick`. It takes on the following form:<br />
- `git cherry-pick <Commit1> <Commit2> <...>`<br />

It's a very straightforward way of saying that you would like to copy a series of commits below your current location (`HEAD`).<br />
To complete this level, simply copy some work from the three branches shown into main. <br />
The command is :
```sh
    git cherry-pick C3 C4 C7
```


## LEVEL 2: INTERACTIVE REBASE INTRO
When the interactive rebase dialog opens, 
    - You can reorder commits simply by changing their order in the UI (via dragging and dropping with the mouse).
    - You can choose to keep all commits or drop specific ones. When the dialog opens, each commit is set to be included by the `pick` button next to it being active. To drop a commit, toggle off its `pick` button.
    `git rebase -i HEAD~number`<br />
The command is :
```sh
    git rebase -i HEAD~4
```
Then as per the requirement, C4 is ommitted and reordering is done