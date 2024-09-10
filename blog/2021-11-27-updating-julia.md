---
title: 'Updating Your Julia Installation (Feb 2023)'
date: 2021-11-27
categories: [julia, workflow]
description: 'What it takes to update from a previous install of Julia on Mac/Linux'
aliases:
  - /updating-julia
canonicalUrl: https://www.nelsontang.com/blog/2021-11-27-updating-julia
date-modified: "2023-02-15"
---

# Updating and managing multiple Julia versions

Out of the box, Julia has a great package manager but it's missing something like `conda` or `pyenv` to manage different versions of Julia, or to update your current installation of Julia to the latest release. See below for what I use on my Mac:

---

**Feb 2023 Update:**

_I recently switched out of `conda` and into `pyenv` and `poetry` on my mac, which ended up breaking my previous method of using `pyjill` to manage my julia installation (which requires python)._

_This was a great opportunity to switch to `juliaup`, which is written in Rust and offers much of the same functionality without the dependence on python. However, it's not perfect ([particularly to users in PRC, as the author of `pyjill` notes here](https://github.com/johnnychen94/jill.py#why-i-make-the-python-fork-of-jill)) and I'll be keeping the old instructions of using `pyjill` for now:_

<details>
<summary>Click here for the old `pyjill` instructions (Python required)</summary>

## Step 1: Use `jill`/`pyjill` to Download & Install Julia

I used to mess with downloading the binaries and install files directly from the [julialang site](https://julialang.org/downloads/) and also tried homebrew, but both of these options were really clunky when it came to updating your existing installation. Instead, I just use `pyjill` ([Github](https://github.com/johnnychen94/jill.py)), which works perfectly on _both_ OSX, Windows, and Linux (note: requires python >=3.6).

```bash
# Install or update the latest version of jill (requires python>=3.6)
pip install jill --user -U
# export the jill PATH somewhere, if this is your first time installing jill
echo 'export PATH=$PATH:/home/$USERNAME/.local/bin' >> ~/.zshrc
source ~/.zshrc
# Install the latest stable release
jill install
```

Then the next time you need to update Julia, you only need to do `jill install` to get the latest.

</details>

---

## Step 0: First-time Install with `juliaup`

The instructions on the [juliaup repo](https://github.com/JuliaLang/juliaup) are extensive, but I'll share a few key commands here:

<details open>
<summary> On a Mac, it's advised (as of Feb'23) to use the following `curl` command instead of `brew`</summary>

```bash
curl -fsSL https://install.julialang.org | sh
```

</details>

This will run an interactive install script and for convenience it will update your `PATH` and install the latest release and set it as your default if you don't have Julia already installed.

Then `juliaup status` will show you the list of versions you have installed, and show you which is the default version of julia that's symlinked to `julia`.

```bash
juliaup status
```

### Switching environments

You can always install an older release, let's say you want `1.8.4`:

```bash
# Add an older version of Julia, let's say 1.8.4
juliaup add 1.8.4
# Then to run that version of julia, all you would need to do is add `+1.8.4` when you launch julia, i.e.:
julia +1.8.4
```

You can also set it as the default channel with `juliaup default`:

```bash
juliaup default 1.8.4
```

## Step 1: Updating to the latest release with `juliaup`

`juliaup` will automatically check for the latest release every so often when you launch `julia`, but you can manually update with:

```bash
juliaup update
```

## Step 2: Remove the Old `.julia` Folder _(optional, linux/OSX instructions)_

Another time sink I had was realizing that with a fresh update, I couldn't add packages anymore to julia because I didn't have root access to a folder hidden deep within the `.julia` folder in my user directory. I had to delete it and then julia worked fine after that after rebuilding the registry. This might not be as much of an issue after Julia 1.7, where they [changed the manifest and how the package registry handles different Julia versions](https://julialang.org/blog/2021/11/julia-1.7-highlights/#new_manifest_format).

```bash
# Go to your home directory
cd
# Delete that sucker with prejudice
sudo rm -rf .julia
```

## Step 3: Update Jupyter Kernels

Next we'll need to remove the old julia kernel from Jupyter with `jupyter kernelspec remove {{ kernel name }}`:

```bash
# See the list of existing jupyter kernels and find your old install
jupyter kernelspec list
# My previous one was called julia-1.6, let's remove it
jupyter kernelspec remove julia-1.6
```

Then use IJulia to add a new one. Whenever you change the Julia binary you need to have IJulia rebuild in order to register the new kernel to jupyter, so go back to Julia and go to the `Pkg` prompt:

```julia
# In the Julia REPL, press the ] key to bring up the Pkg prompt
(@v1.8) pkg> add IJulia
(@v1.8) pkg> build IJulia
```

At this point, if you're upgrading from Julia 1.7+ and it's a minor update (i.e. 1.7.2 to 1.7.3), your base package manifest should still be there and Julia will precompile and build those other packages so they'll be ready to go - no need to re-add them.

## Step 4. Update Your Libraries (if upgrading from Julia < 1.7)

From here on out you'll need to probably `build` and update your other libraries too, and if you use stuff like `PyCall`([link](https://github.com/JuliaPy/PyCall.jl)) where it downloads a distribution of python and hides it in your julia folder, have fun managing all of that! I'll do a writeup later when I figure this out a little more.

```julia
# A few common libraries that I install for data exploration and analysis
(@v1.8) pkg> add Revise Plots Gadfly DataFrames DataFramesMeta XLSX CSV RDatasets Parquet
```
