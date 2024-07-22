Learning Git command from the site 
learninggitbranching.org


The first task was to learn the command git commit
commit basically creates the checkout of current work

command - git commit -m "your message"

------------------------------------------------------------------------------------

Level Introduction to Git Commit

command - git commit

git commit create a snapshot of the staged changes along a timeline of a Git projects history.

---------------------------------------------------------------------------------

Level Learn Git Branching

Braches in Git are  are simply pointers to a specific commit --

Branch Early, and Branch Often

git branch bugFix
git checkout bugFix (inorder to change branch checkout command is used)

also
git checkout -b [branch name] (creates a new branch and change to that branch)

-------------------------------------------------------------------------------------

Level Merging in Git

We can merge two branches using git merge command, we have to make sure that the commits are updated.


git branch bugFix
git checkout bugFix
git commit
git checkout main
git commit
git merge bugFix   (merge bugFix to main as we were on main branch)

-------------------------------------------------------------------------------------

Level Rebasing


Rebasing essentially takes a set of commits, "copies" them, and plops them down somewhere else.


git checkout -b bugFix; git commit
git checkout main; git commit
git checkout bugFix
git rebase main

-------------------------------------------------------------------------------------

Level Detach yo' Head

Head is hidden under recent commit, which helps understand the commit tree, we can detach it 


git checkout c4 (to show head in commit C4)

-------------------------------------------------------------------------------------

Level Relative Refs (^)

We can see our commit history using git command
Every commit are in hashes which is a lot longer and bit tedious to specify

The upside is that Git is smart about hashes. It only requires you to specify enough characters of the hash until it uniquely identifies the commit. So I can type fed2 instead of the long string above.

Specifying commits by their hashes isnt convenient so, git has relative refs

^ is used to move upwards one commit
~<num> to move upwards a number of times

git checkout bugFix
git checkout HEAD^

Level Relative Refs (~)

~<num> to move upwards a number of times

-f forcefully moves head

solution :

git checkout HEAD^
git branch -f main C6
git branch -f bugFix HEAD^

-------------------------------------------------------------------------------------

Level : reversing changes in Git

git revert
and git reset

reset moves to one branch up and acts like rewriting history

whereas
revert creates a new commit, below the commit we wanted to reverse
it just happens to introduce changes that exactly reverses the commit of prev one

With reverting, you can push out your changes to share with others.

git checkout pushed
git revert pushed
git checkout local
git reset c1


-------------------------------------------------------------------------------------


Learn Cherry pick

The first command in this series is called git cherry-pick. It takes on the following form:

git cherry-pick <Commit1> <Commit2> <...>

It's a very straightforward way of saying that you would like to copy a series of commits below your current location (HEAD).

git cherry-pick c3 c4 c7

the copy of three commits are kept below current head

-------------------------------------------------------------------------------------

Interactive rebase intro

git rebase -i HEAD~4



this opens a text editor in vim 
in which we can omit commits, pick or rearrange them


-------------------------------------------------------------------------------------

Level grabbing just one commit

solution using cherry-pick

git checkout main
git cherry-pick c4


-------------------------------------------------------------------------------------

Juggling Commits

