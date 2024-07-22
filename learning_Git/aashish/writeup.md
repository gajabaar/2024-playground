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

git branch -f main HEAD~3

