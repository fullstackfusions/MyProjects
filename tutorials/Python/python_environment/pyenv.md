Sure! Here's a detailed guide on how to use `pyenv` to manage different Python versions and how to create virtual environments using these versions:

### Step 1: Install pyenv

First, you'll need to install `pyenv`. The installation process can vary depending on your operating system. Here's how you can install it on Unix-like systems:

```bash
# Install prerequisites (Ubuntu example)
sudo apt-get update
sudo apt-get install -y make build-essential libssl-dev zlib1g-dev \
libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev \
libncursesw5-dev xz-utils tk-dev libffi-dev liblzma-dev python-openssl git

# Install pyenv using the Pyenv-installer
curl -L https://github.com/pyenv/pyenv-installer/raw/master/bin/pyenv-installer | bash

# Add pyenv to the shell by adding the following lines to your shell's
# configuration file (.bashrc, .bash_profile, .zshrc, etc.)
export PATH="$HOME/.pyenv/bin:$PATH"
eval "$(pyenv init --path)"
eval "$(pyenv virtualenv-init -)"
```

### Step 2: Install Python Versions

Once `pyenv` is installed, you can install multiple versions of Python. Here’s how you can install Python 3.8.5 and 3.9.1, for example:

```bash
pyenv install 3.8.5
pyenv install 3.9.1
```

### Step 3: Create Virtual Environments

With the Python versions installed, you can create virtual environments for each version. Here’s how to create a virtual environment for Python 3.8.5:

```bash
# Set the global Python version to 3.8.5
pyenv global 3.8.5

# Create a virtual environment named 'env385' using Python 3.8.5
pyenv virtualenv 3.8.5 env385
```

And similarly for Python 3.9.1:

```bash
# Set the global Python version to 3.9.1
pyenv global 3.9.1

# Create a virtual environment named 'env391' using Python 3.9.1
pyenv virtualenv 3.9.1 env391
```

### Step 4: Activate and Use Virtual Environments

To activate the virtual environment, use:

```bash
pyenv activate env385
```

When you are done working in the virtual environment, you can deactivate it:

```bash
pyenv deactivate
```

### Step 5: Switching Between Environments

You can switch between environments by simply activating the desired one. Each time you activate a different environment, you switch to that environment's Python version and its installed packages.

### Additional Tips

- You can list all installed Python versions with `pyenv versions`.
- You can see all virtual environments with `pyenv virtualenvs`.

This setup allows you to have distinct Python installations and virtual environments, managing them efficiently for different projects.
