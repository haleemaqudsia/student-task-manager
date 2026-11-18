# Lab Report

## 1. Git, GitHub, and basic commands

Git tracks changes in my local repository. GitHub hosts the repository online
for collaboration. `git add` stages changes, `git commit` records them locally,
and `git push` uploads commits to GitHub.

## 2. Branches, pull requests, and merge conflicts

Branches let me work on features separately from `main`. Pull requests let me
inspect changes and leave comments before merging. My README conflict happened
because both branches replaced `Project status: Planning` with different text.
I kept both meanings in one line and removed the leftover conflict markers
in a follow-up commit.

## 3. Fetch vs. pull and merge vs. rebase

`git fetch` downloads remote updates without integrating them into my branch.
`git pull` fetches and then integrates the updates. A merge combines histories
without rewriting existing commits. A rebase replays commits on a new base,
giving the replayed commits new IDs.

## 4. Issues and Actions

Issues track bugs, features, and documentation work. Linking an issue to a pull
request shows which changes address it. Actions runs tests automatically so
problems can be caught before merging.

## 5. One difficulty and how I solved it

The app would not start because the body of `complete_task` was not indented
under its definition. I fixed the indentation and ran the app again. The final
local test run passed all three tests for adding, completing, and deleting tasks.
