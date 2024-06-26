# 1. Rebasing over 9000 times!

**Problem:**<br>
- to rebase all work from branches onto main
- the commits wants all to be in sequential order
![alt text](./images/rebasingover9000.png)

**Solution:**

![alt text](./images/rebasingover9000soln.png)


# 2. Multiple Parents
- ~ modifier takes optional number specifying what number of generations to go back
- ^ modifier also specifies which parent reference to follow from merge commit
- git normally follows first parent, but we can specify number with ^ to change default behaviour. 


**Problem:**<br>
To complete this level, create a new branch at the specified destination:
![alt text](./images/multipleparent.png)


**Solution:**<br>
Just create bugWork branch in C2 commit.<br>
```git branch bugWork C2```


# 3. Branch Spaghetti
- ```main``` is few commits ahead of ```one```, ```two```and ```three``` branches.
- to update these 3 branches with modified versions of last few commits on main.
- Branch one needs a re-ordering of those commits and an exclusion/drop of C5. 
- Branch two just needs a pure reordering of the commits. 
- Branch three only needs one commit transferred.
![alt text](./images/branchspagetti.png)


**Solution:**<br>
![alt text](./images/branchspagettisoln.png)
- cherry-pick required commits from main branch 
- continue cherry-picking from two branches
- forcebranch to commit c2 using ```git branch -f three HEAD~3```