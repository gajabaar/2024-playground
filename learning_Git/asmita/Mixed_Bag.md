# A Mixed Bag

The commands to be used here are
- `git rebase -i`
- `git cherry-pick`


## LEVEL 1: GRABBING JUST ONE COMMIT
In order to complete the level, make sure `main` receives the commit that `bugFix` references.<br />
The commands are:
```sh
    git checkout main
    git cherry-pick C4
```
    

## LEVEL 2: JUGGLING COMMITS
Here's another situation that happens quite commonly. You have some changes (`newImage`) and another set of changes (`caption`) that are related, so they are stacked on top of each other in your repository (aka one after another).<br />
The tricky thing is that sometimes you need to make a small modification to an earlier commit. In this case, design wants us to change the dimensions of `newImage` slightly, even though that commit is way back in our history!! <br />
We will overcome this difficulty by doing the following:
    - We will re-order the commits so the one we want to change is on top with `git rebase -i`
    - We will `git commit --amend` to make the slight modification
    - Then we will re-order the commits back to how they were previously with `git rebase -i`
    - Finally, we will move main to this updated part of the tree to finish the level (via the method of your choosing)
    
The commands are: 
```sh
    git rebase -i HEAD~2 
    git commit —amend
    git rebase -i HEAD~2
    git branch -f main C3’’
```
Note: Here, both times when, git rebase -i HEAD~2 is done, the sequence of commits is changed between the two, ultimately going for two consecutive changes.
    

## LEVEL 3: JUGGLING COMMITS #2
So in this level, let's accomplish the same objective of amending `C2` once but avoid using `rebase -i`. <br />
The commands are:
```sh
    git checkout HEAD~2
    git cherry-pick C2
    git checkout HEAD~1
    git cherry-pick C2' C3
    git branch -f main C3’
```
    

## LEVEL 4: GIT TAGS
Git tags (somewhat) permanently mark certain commits as "milestones" that can then be referenced like a branch. More importantly though, they never move as more commits are created. <br />
To create a tag:<br />
`git tag v1 C1`<br />
The commands for solving this level are:
```sh
    git tag v0 C1
    git tag v1 C2
    git checkout HEAD~1
```
    

## LEVEL 5: GIT DESCRIBE
Because tags serve as such great "anchors" in the codebase, git has a command to *describe* where you are relative to the closest "anchor" (aka tag). And that command is called `git describe`!<br />
Git describe can help you get your bearings after you've moved many commits backwards or forwards in history; this can happen after you've completed a git bisect (a debugging search) or when sitting down at the computer of a coworker who just got back from vacation.<br />
Git describe takes the form of:<br />
    `git describe <ref>` <br />
Where `<ref>` is anything git can resolve into a commit. If you don't specify a ref, git just uses where you're checked out right now (`HEAD`).<br />
    
The output of the command looks like:<br />
    `<tag>_<numCommits>_g<hash>` <br />
Where `tag` is the closest ancestor tag in history, `numCommits` is how many commits away that tag is, and `<hash>` is the hash of the commit being described.<br />
The command is 
```sh
    git commit
```