# Learning Git Branching

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
