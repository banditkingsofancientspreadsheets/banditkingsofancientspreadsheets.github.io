# banditkings

A project package generated using the [cookiecutter](https://cookiecutter.readthedocs.io/en/stable/) library and the https://github.com/banditkings/ds_cookie template.

# Usage: with`poetry` + `pyenv`

## Set local `pyenv` environment

Let's say you want to create an environment using python version 3.10.12 (default: 3.10.6)

```bash
pyenv install 3.10.12
```
Then navigate to the root directory and make it your local version:

```bash
pyenv local 3.10.12
```

This creates a `.python-version` file. During cookie creation this should have prompted you for this for convenience

## Install dependencies and create the virtual env in `poetry`

```bash
# Install with optional dev and plotly dependencies
poetry install --with dev,plotly
```

This will install the required dependencies and the banditkings package and create a virtual environment and virtual shell. You can exit the virtual shell with crtl+d or `exit` in terminal.

## Resuming work

Next time you enter into the directory, `pyenv` will detect and activate local python version and then you can restart the shell:

```bash
poetry shell
```
# Testing

To use `pytest` to run all tests in the `src\tests\` folder:


```bash
poetry run pytest
```

This will use `pytest` to search for files that start with test_*.py or *_test.py,
and within those files run `test` prefixed functions and methods. 

* See [pytest docs](https://docs.pytest.org/en/7.2.x/explanation/goodpractices.html)


# Git

See this [gist](https://gist.github.com/mindplace/b4b094157d7a3be6afd2c96370d39fad) for a reminder on the steps to initialize this as a git repo and push to a remote, empty repo.


# From the old site: 

## Custom CSS
Followed instructions for custom CSS and downloaded the table class from bootstrap 4 in order to get tables to look better. But, dark mode sucks with it

## Tables
Adding CSS to Markdown Tables
Fixes issue with this blog post