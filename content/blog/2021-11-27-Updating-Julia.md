---
title: "Updating Julia in 2021"
date: 2021-11-27
tags: [julia]
categories: [workflow]
summary: "What it takes to update from a previous install of Julia on Mac/Linux"
aliases:
    - /updating-julia
---

Had the hassle of trying to update Julia from 1.6.2 to 1.6.4 this weekend and I gotta say, *every* time there's always something I forget, so here's my best tips on what it takes to update your installation of Julia in Mac/Linux:

## Step 1: Use `jill`/`pyjill` to Download & Install Julia

I used to try to mess with downloading the binaries and install files directly from the [julialang site](https://julialang.org/downloads/) and also tried homebrew, but both of these options were really clunky when it came to updating your existing installation. Instead, I just use `pyjill` (https://github.com/johnnychen94/jill.py)

```bash
# Install or update the latest version of jill (requires python>=3.6)
pip install jill --user -U
# export the jill PATH somewhere
echo 'export PATH=$PATH:/home/$USERNAME/.local/bin' >> ~/.personal_macros
source ~/.zshrc
# Install the latest stable release
jill install
```

## Step 2: Remove the Old `.julia` Folder *(optional)*

Another time sink I had was realizing that with a fresh update, I couldn't add packages anymore to julia because I didn't have root access to a folder hidden deep within the `.julia` folder in my user directory. I had to delete it and then julia worked fine after that after rebuilding the registry.

```bash
# Go to your home directory
cd
# Delete that sucker with prejudice
sudo rm -rf .julia
```

## Step 3: Update Jupyter Kernels

Next we'll need to remove the old julia kernel:

```bash
# See the list of existing jupyter kernels and find your old install
jupyter kernelspec list
# My previous one was called julia-1.6, let's remove it
jupyter kernelspec remove julia-1.6
```

Then use IJulia to add a new one. Whenever you change the Julia binary you need to have IJulia rebuild in order to register the new kernel to jupyter, so go back to Julia and go to the Pkg prompt:

```julia
(@v1.6) pkg> build IJulia
```

## Update Your Libraries

From here on out you'll need to probably build and update your other libraries too, and if you use stuff like `PyCall`([link](https://github.com/JuliaPy/PyCall.jl)) where it downloads a distribution of python and hides it in your julia folder, have fun managing all of that! I'll do a writeup later when I figure this out a little more.