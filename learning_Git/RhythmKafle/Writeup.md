## Introduction to Git Commits

A commit in a git repository records a snapshot of all the (tracked) files in your directory. Git maintains a history of all commits. 

Solution:

```bash
git commit
git commit
```

## Branching in Git

Branches are pointers to a specific commit.

Used to logically divide your work.

Branch essentially says “I want to include the work of this commit and all parent commits.”

Commands used in this level:

```bash
git branch branchName
git checkout branchName
```

Shortcut to do both the commands (and solve the level):

```bash
git checkout -b branchName
```

## Branches and Merging

Merge means to include all the works from both the “parents”

Commands to solve this level

```bash
git checkout -b bugFix
git commit
git checkout main
git commit 
git merger bugFix
```

## Git Rebase

Another way of combining work between branches.

Takes a set of commits, “copies” them, and plops them down somewhere else.

Helps to make a nice linear sequence of commits.

Commands to solve this level:

```bash
git checkout -b bugFix
git commit
git checkout main
git commit
git checkout bugFix
git rebase main
```

# Detatch yo’ head

## Head:

Is the symbolic name for the currently checked out commit

It is basically the commit we are working on top of

Head always points to the most recent commit

Detatching a head = attaching head to a commit, instead of a branch

To do this: 

 

```bash
git checkout commit_hash
```

## Relative Refs(^)

Simply typing the first few letters of the hash can help git recognize the commit hash

Eg:`fed2` for `fed2da64c0efc5293610bdd892f82a58e8cbc5d8` 

Relative commits:

- Move upwards one commit at a time (^)
- Moving upwards a number of times(~<num>)

To go one step up ( towards the parent ) of Main branch:

```bash
git checkout main^
```

We can also use HEAD as relative ref

```bash
git checkout C3
git checkout HEAD^
git checkout HEAD^
git checkout HEAD^
# goes 3 parents up
```

To solve this level:

```bash
git checkout bugFix^
```

## Relative refs #2 (~)

- Optional
- Specifies number of parents you wish to ascend


```bash
git checkout HEAD~4
```

- You can directly reassign a branch to a commit with the `-f` option.

```bash
git branch -f main HEAD~3
```

- Commands to solve this level:

```bash
git branch -f bugFix HEAD~2
git branch -f main C6
git checkout HEAD^
```

## Reversing Changes in Git

- Two primary ways to do this: `git reset` and `git revert`

### Git Reset:

- Moves the commit back to a previous commit
- Similar to “Rewriting history”

```bash
git reset HEAD~1
```

### Git Revert

- Reverse changes and *share* those reversed changes with others
- With reverting, you can push out your changes to share with others.

```bash
git revert HEAD
```

To solve this level:

```bash
git reset local^
git checkout pushed
git revert pushed
```

## Cherry-pick

- Copy a series of commits below the current location

```bash
git cherry-pick commit1 commit2 ...
```

This copies the work done in commit1 and commit2 and brings it below the current working branch

- Useful when we know which commits we want and their corresponding hashes

To solve this level:

```bash
git cherry-pick C3 C4 C7
```

## Interactive Rebase

- using git rebase with -i option
- Git will open an interactive window/UI to show which commit messages are to be rebased below the target of the rebase

```bash
git rebase -i HEAD~4
```

To solve this level:

```bash
git rebase -i HEAD~4
```

## Grabbing just 1 commit

To solve this level:

```bash
git checkout main
git cherry-pick C4
```
## Juggling Commit

To solve this level:

```bash
git rebase -i caption~2
-> pick C3
-> pick C2
git --amend
git rebase -i caption~2
-> pick C2''
-> pick C3'
git branch -f main caption
```

## Juggling Commit - 2

To solve this level:

```bash
git checkout main
git cherry-pick C2
git commit --amend
git cherry-pick C3
```

## Git tags

- permanently marks certain commits as milestones that we can then refer like a branch

To solve this level:

```bash
git tag v0 c1
git tag v1 c2
git checkout v1
```

## Git Describe

- Describes where we are closest to the “anchor”(tag)
- Syntax: git describe
- Output: tag_stepsAway_hash

Just git commit after playing for a while


## Rebasing over 9000 times

To solve this level:

```bash
git rebase main bugFix
git rebase bugFix side
git rebase side another
git rebase another main
```

## Multiple parents

To solve this level:

```bash
git branch bugWork main^^2^
```

## Branch Spaghetti
To solve this level:

```bash
git checkout one
git cherry-pick c4 c3 c2
git checkout two 
git cherry-pick c5 c4' c3' c2'
git branch -f three c2
```

## Git Remotes

To create remotes:

```bash
git clone 
```

To solve this level:

```bash
git clone
```

## Remote branches

o/main is a remote branch

o = remote name, main = branch name

To solve this level:

```bash
git commit
git checkout o/main
git commit
```

## Git fetching

fetches data from a remote repository

git fetch does the following:

- downloads the commits the remote has but are missing in our local repo
- updates where our remote branches point

To solve this level:

```bash
git fetch
```

## Git pullin’

fetches remote and merges them

To solve this level

```bash
git pull
```

## Faking Teamwork

To solve this level:

```bash
git fakeTeamwork main 2
git commit
git pull
```

## Git Pushin’

Upload shared work

To solve this level:

```bash
git commit
git commit
git push
```

## Diverged History

When the main branch has commits that your branch does not, git push does not work

In this case: 

1. git fetch → git rebase → git push
2. git fetch → git merge → git push
3. git pull —rebase → git push
4. git pull → git push

To solve this level:

```bash
git clone
git fakeTeamwork main 1
git commit
git fetch
git rebase o/main
git push
```

## Locked Main

To solve this level:

```bash
git checkout -b feature
git branch -f main o/main
git push
```
