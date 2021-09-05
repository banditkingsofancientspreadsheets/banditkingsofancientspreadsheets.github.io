---
title: "Quick Bash Script for Complete Newbies"
date: 2020-11-13
tags: [workflow]
summary: "Basic shell scripting for everyday productivity."
---

At work or grad school, I have to juggle a lot of projects and it always takes me a while to remember which directory I was in and what I named the project environment. I wanted 'shortcuts' in the terminal that would automate the things I was typing out manually each time. To do this, I saved these custom functions and `source` them into `.zshrc`.

## 1. Create a file for your custom scripts
I store a file for these personal macros, let's create one here:
```bash
cd /usr/local/bin/
touch personal_macros.
vi personal_macros
```
This navigates to your `/usr/local/bin/` directory, creates the `personal_macros` file with `touch` and uses vim to open it with `vi`. 

## 2. Write functions
Once your blank file is created you need to add in your functions. The first line that starts with the `#!` (shebang) tells bash that this is a zshell script. I don't remember if this is absolutely necessary but I had it here.

```bash
#!/usr/bin/env zsh

function explore() {
  cd ~/Documents/Analysis
  conda activate explore
  code .
}

function workmode() {
  cd ~/Documents/Analysis/GT/ISYE6501
  open .
  open ISYE6501.Rproj
}
```
These are examples of basic functions. The first one, `explore()` navigates to a folder and activates a conda environment called `explore`. Then it opens up a vscode window in the folder.

The second function `workmode()` navigates to another folder, opens an explorer window there, and then will open my `ISYE6501.Rproj` project in RStudio. 

Remember, when you're done with vim, type `:wq` to save your changes and exit.
```vim
:wq
```

## 3. Add these functions to your `.zshrc` file
After you're done creating the functions it's time to add them to the `.zshrc` file so you can call these functions from the terminal.
```console
cd
vi .zshrc
```
Then you want to add a line to `source` your `personal_macros` file by adding in this line to the `.zshrc` file:
```bash
source /usr/local/bin/personal_macros
```
Go ahead and save and exit vim:
```vim
:wq
```
Now you can reload your terminal and the functions will be available to you! Just type `explore` or `workmode` and it'll run through the steps in your script.

I like to create functions that follow a particular taxonomy. For work projects, I'll make a function for each project I'm working on, starting with `work-` so it's easy to remember and I can utilize tab completion. For example, I'll have a `work-unicorn` function when I'm working on the unicorn project and a `work-phoenix` function when I want to resume work on the phoenix project. 

Happy scripting!