# Push & Pull -- Git Remotes! 

Time to share your 1's and 0's kids; coding just got social 

## 1: Clone Intro

![101.1](./ss/101.1.png)

```sh
git clone
```

## 2: Remote Branches

![101.2](./ss/101.2.png)

```sh
git commit
git checkout o/main
git commit
```

## 3: Git Fetchin'

![101.3](./ss/101.3.png)

```sh
git fetch
```

## 4: Git Pullin'

![101.4](./ss/101.4.png)

```sh
git pull
```

## 5: Faking Teamwork

![101.5](./ss/101.5.png)

```sh
git clone
git fakeTeamwork main 2
git fetch
git commit
git merge o/main
```

## 6: Git Pushin'

![101.6](./ss/101.6.png)

```sh
git commit
git commit
git push
```

## 7: Diverged History

![101.7](./ss/101.7.png)

```sh
git clone
git fakeTeamwork
git commit
git pull --rebase
git push
```

## 8: Locked Main

![101.8](./ss/101.8.png)

```sh
git branch feature
git reset HEAD^
git checkout feature
git push
```

# To Origin And Beyond -- Advanced Git Remotes! 

And you thought being a benevolent dictator would be fun... 

## 1: Push Main!

![102.1](./ss/102.1.png)

```sh
git fetch 
git rebase o/main side1
git rebase side1 side2
git rebase side2 side3
git rebase side3 main
git push
```

## 2: Merging with remotes

![102.2](./ss/102.2.png)

```sh
git fetch
git checkout side1
git merge o/main
git merge side2
git merge side3
git rebase side1 main
git push
```
OR,
```sh
git checkout main
git pull
git merge side1
git merge side2
git merge side3
git push
```

## 3: Remote Tracking

![102.3](./ss/102.3.png)

```sh
git checkout -b side o/main
git commit
git pull --rebase
git push
```

## 4: Git push arguments

![102.4](./ss/102.4.png)

```sh
git push origin main
git push origin foo
```

## 5: Git push arguments -- Expanded!

![102.5](./ss/102.5.png)

```sh
git checkout foo
git push origin foo:main
git push origin main^:foo
git checkout main
```
OR,
```sh
git push origin main^:foo
git push origin foo:main
```

## 6: Fetch arguments

![102.6](./ss/102.6.png)

```sh
git fetch origin C6:main
git fetch origin C3:foo
git checkout foo
git merge main
```

## 7: Source of nothing

![102.7](./ss/102.7.png)

```sh
git push origin :foo
git fetch origin :bar
```

## 8: Pull arguments

![102.8](./ss/102.8.png)

- My solution:
```sh
git fetch origin C2:side
git pull origin C3:foo
git merge side
```

- Their Solution:
```sh
git pull origin c3:foo
git pull origin c2:side
```
