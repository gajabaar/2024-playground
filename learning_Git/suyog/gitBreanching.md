# Learning Git Branching (Main)

## 1.1 Introduction to Git Commits      
```bash  
git commit;
```

## 1.2 Branching in Git
```bash  
git branch bugFix;  
git checkout bugFix;
```

## 1.3 Merging in Git
```bash  
git branch bugFix;  
git checkout bugFix;  
git commit;  
git checkout main;  
git commit;
git merge bugFix;
```

## 1.4 Rebase Introduction
```bash 
git checkout -b bugFix;  
git commit;  
git checkout main;  
git commit;  
git checkout bugFix;  
git rebase main;
```

## 2.1 Detach HEAD
```bash 
git checkout c4;
```

## 2.2 Relative Refs (^)
```bash 
git checkout bugFix^;
```

## 2.3 Relative Refs #2 (~)
```bash 
git branch -f bugFix HEAD~2;  
git branch -f main c6;  
git checkout c1;
```

## 2.4 Reversing Changes in Git
```bash 
git reset HEAD^;
git checkout pushed;  
git revert HEAD;
```

## 3.1 Cherry-pick Intro
```bash 
git cherry-pick c3 c4 c7;
```

## 3.2 Interactive Rebase Intro
```bash 
git rebase -i HEAD~4;
```

## 4.1 Grabbing Just 1 Commit
```bash
git checkout main;
git cherry-pick bugFix;
```

## 4.2 Juggeling Commits
```bash
git rebase -i c1 c3;
git commit --amend;
git rebase -i HEAD~2;
git branch caption -f;
git branch -f main;
```

## 4.3 Juggeling Commits #2
```bash
git checkout newImage;
git commit --amend;
git checkout main;
git cherry-pick newImage c3;
```

## 4.4 Git Tags
```bash
git tag v0 c1;
git checkout c2;
git tag v1;
```

## 4.5 Git Describe
```bash
git describe c4;
git describe bugFix;
git describe c3;
git side main;
git describe main;
```

## 5.1 Rebasing over 9000 times
```bash
git rebase main bugFix;
git rebase bugFix side;
git rebase side another;
git branch -f main;
```

## 5.2 Multiple Parents
```bash
git branch bugWork HEAD~^2~;
```

## 5.3 Branch Spaghetti
```bash
git checkout c1;
git cherry-pick c4 c3 c2;
git branch -f one;
git cherry-pick c5;
git checkout c2;
git branch -f three;
git rebase -i HEAD~4;
git branch -f two;
```

# Learning Git Branching (Remote)

## 1.1 Clone Intro
```bash
git clone;
```

## 1.2 Remote Branches
```bash
git checkout o/main;
git commit;
git commit;
git checkout c3;
git branch -f main;
git checkout c4;
```

## 1.3 Git Fetchin'
```bash
git fetch;
```

## 1.4 Git Pullin'
```bash
git fetch;
git merge o/main;
```

## 1.5 Faking Teamwork
```bash
git clone;
git fakeTeamwork main 2;
git commit;
git pull;
```

## 1.6 Git pushin'
```bash
git commit;
git commit;
git push;
```

## 1.7 Diverged History
```bash
git clone;
git fakeTeamwork 1;
git commit;
git fetch;
git rebase o/main main;
git push;
```

## 1.8 Locked Main
```bash
git reset o/main;
git checkout -b feature c2;
git push;
```

## 2.1 Push Main!
```bash
git fetch;
git rebase o/main side1;
git checkout c2';
git cherry-pick c3 c4 c5 c6 c7;
git branch -f main;
git branch -f side3;
git checkout c4';
git branch -f side2;
git checkout main;
git push;
```

## 2.2 Merging with remotes
```bash
git fetch;
git checkout c8;
git merge c2;
git merge c4;
git merge c7;
git branch -f main;
git checkout main;
git push;
```