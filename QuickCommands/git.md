Here’s a list of the most commonly used Git commands, categorized by their functionality. These commands are useful for managing your Git repositories, branches, commits, and more.

### **Basic Git Commands**

1. **Clone a Repository**

```bash
git clone <repository-url> # Creates a local copy of a remote repository.
```

2. **Initialize a Git Repository**

```bash
git init # Initializes a new Git repository in the current directory.
```

3. **Check the Status of the Repository**

```bash
git status # Shows the current state of the working directory, including staged, unstaged, and untracked files.
```

4. **Add Files to Staging Area**

```bash
git add <file>
git add .        # Adds all changes
# Moves changes from the working directory to the staging area.
```

5. **Commit Changes**

```bash
git commit -m "Your commit message" # Commits the staged changes to the repository with a message describing the changes.
```

6. **View Commit History**

```bash
git log # Displays the commit history.
```

---

### **Branching and Merging**

1. **Create a New Branch**

```bash
git branch <branch-name> # Creates a new branch.
```

2. **Switch to a Branch**

```bash
git checkout <branch-name> # Switches to the specified branch.
```

3. **Create and Switch to a New Branch**

```bash
git checkout -b <branch-name> # Creates a new branch and switches to it in one step.
```

4. **Merge a Branch**

```bash
git merge <branch-name> # Merges the specified branch into the current branch.
```

5. **Delete a Branch**

```bash
git branch -d <branch-name> # Deletes a branch (only if it has been merged).
```

---

### **Remote Repository Management**

1. **Add a Remote Repository**

```bash
git remote add origin <repository-url> # Adds a remote repository named `origin`.
```

2. **View Remote Repositories**

```bash
git remote -v # Lists the remote repositories and their URLs.
```

3. **Fetch Changes from Remote**

```bash
git fetch origin # Downloads changes from the remote repository without merging them.
```

4. **Pull Changes from Remote**

```bash
git pull # Fetches changes from the remote repository and merges them into the current branch.
```

5. **Push Changes to Remote**

```bash
git push origin <branch-name> # Pushes local changes to the specified branch on the remote repository.
```

6. **Force Push Changes**

```bash
git push --force # Forces a push, overwriting remote changes (use with caution).
```

---

### **Undoing Changes**

1. **Unstage Changes (Undo `git add`)**

```bash
git reset <file>
git reset .     # remove all files from staging
# Removes files from the staging area without deleting the changes.
```

2. **Discard Local Changes**

```bash
git checkout -- <file> # Discards local changes in the working directory (use carefully).
```

3. **Amend the Last Commit**

```bash
git commit --amend -m "Updated commit message" # Modifies the last commit (message or staged files).
```

4. **Revert a Commit**

```bash
git revert <commit-hash> # Creates a new commit that reverses the changes from a specified commit.
```

---

### **Stashing Changes**

1. **Stash Changes**

```bash
git stash # Temporarily stores changes that are not ready to be committed.
```

2. **Apply Stashed Changes**

```bash
git stash apply # Applies the most recently stashed changes.
```

3. **List Stashes**

```bash
git stash list # Lists all stashed changes.
```

4. **Pop and Apply Stashed Changes**

```bash
git stash pop # Applies the most recent stash and removes it from the stash list.
```

---

### **Tagging**

1. **Create a Tag**

```bash
git tag <tag-name> # Creates a new tag.
```

2. **List Tags**

```bash
git tag # Lists all tags in the repository.
```

3. **Push Tags to Remote**

```bash
git push origin <tag-name> # Pushes a specific tag to the remote repository.
```

4. **Delete a Tag**

```bash
git tag -d <tag-name> # Deletes a tag locally.
```

5. **Delete a Tag from Remote**

```bash
git push origin --delete <tag-name> # Deletes a tag from the remote repository.
```

---

### **Advanced Commands**

1. **Rebase**

```bash
git rebase <branch-name> # Reapplies commits from one branch on top of another (useful for linear history).
```

2. **Squash Commits**

```bash
git rebase -i HEAD~<number-of-commits> # Squashes multiple commits into one interactive rebase.
```

3. **Cherry-Pick a Commit**

```bash
git cherry-pick <commit-hash> # Applies the changes from a specific commit to the current branch.
```

4. **Reset to a Specific Commit**

```bash
git reset --hard <commit-hash> # Resets the working directory and index to a specific commit, discarding all changes (use with caution).
```

---

### **Viewing Changes**

1. **Show Changes Between Commits**

```bash
git diff <commit1> <commit2> # Shows the differences between two commits.
```

2. **Show Unstaged Changes**

```bash
git diff # Displays changes that haven't been staged yet.
```

3. **Show Staged Changes**

```bash
git diff --staged # Displays changes that are staged for the next commit.
```

4. **Show Changes in a Commit**

```bash
git show <commit-hash> # Shows the changes made in a specific commit.
```

---

### **Other Useful Commands**

1. **View Commit History with Graph**

```bash
git log --oneline --graph --all # Displays a graphical commit history in one line per commit.
```

2. **Clean Untracked Files**

```bash
git clean -f # Removes untracked files from the working directory.
```

3. **Get Remote URL**

```bash
git remote get-url origin # Displays the URL of the remote repository.
```

4. **Show Commit Author**

```bash
git shortlog # Displays commit history grouped by author.
```
