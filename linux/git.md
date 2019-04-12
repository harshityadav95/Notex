# Git Commands  
#### [<--Back to Home](../Readme.md)

Setting up Git  Identity

```
$ git config --global user.name "John Doe"

$ git config --global user.email johndoe@example.com
```

Checking Settings
```
git config --list
```

Create a new branch with git and manage branches

Before creating a new branch, pull the changes from upstream. Your master needs to be up to date.

```
$ git pull
```
Create the branch on your local machine and switch in this branch :
```
$ git checkout -b [name_of_your_new_branch]

```
Push the branch on github :

```
$ git push origin [name_of_your_new_branch]
```