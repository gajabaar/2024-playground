# Advanced Topics

## LEVEL 1 : REBASING OVER 9000 TIMES
Rebasing is the process of moving or combining a sequence of commits to a new base commit. Rebasing is most useful and easily visualized in the context of a feature branching workflow. <br />
The commands to complete this level are:
```sh
git checkout bugFix
git rebase main
git checkout side 
git rebase bugFix
git checkout another
git rebase side
git branch -f main HEAD
```


## LEVEL 2 : MULTIPLE PARENTS
Like the `~` modifier, the `^` modifier also accepts an optional number after it.<br />
Rather than specifying the number of generations to go back (what `~` takes), the modifier on `^` specifies which parent reference to follow from a merge commit.<br />
Git will normally follow the "first" parent upwards from a merge commit, but specifying a number with ^ changes this default behavior.<br />
THe commands to complete this level are:
```sh
git branch bugWork
git branch -f bugWork HEAD~^2~
```

## LEVEL 3 : BRANCH SPAGHETTI
Here we have `main` that is a few commits ahead of branches `one` `two` and `three`. For whatever reason, we need to update these three other branches with modified versions of the last few commits on main.<br />
Branch `one` needs a re-ordering of those commits and an exclusion/drop of `C5`. Branch `two` just needs a pure reordering of the commits, and `three` only needs one commit transferred!<br />
The commands are:
```sh
git checkout C1
git cherry-pick C4  C3  C2
git branch -f  one
git checkout C1
git cherry-pick C5  C4’  C3’  C2’
git branch -f two
git checkout C2
git branch -f  three
```

