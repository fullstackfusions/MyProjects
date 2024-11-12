## Check if the Interpreter is matching

### check the interpreter location:

First, check whether the pip has the same version of the interpreter as that on the system and where the Python environment currently resides: To check where the Python currently resides type the below command in the terminal.

**Windows**

- where python
- where pip

**Linux** / **Mac**

- which -a python python2 python3
- which python
- which pip

**Output should be matching**:

- C:\Users\SomeFolder\AppData\Local\Programs\Python\Python37\python.exe
- C:\Users\SomeFolder\AppData\Local\Programs\Python\Python37\Scripts\pip.exe

---

## change/ manage python versions (manually):

to change the python versions on mac you first have to download the python versions.

For example I have downloaded 3.11.1 and 3.13.1. Now when I run `python3` in terminal that will select one of the python as default version to handle the task.

In that process suppose the 3.11.1 version chosen as default one, and I want to set 3.13.1 as default python version.

Run `alias python=python3.13.1`

> **If you don't want to manage manually you can take a look into pyenv and conda options.**

---

## Specify the Interpreter of your choice

### Specify interpreter manually if you are using virtualenv

- virtualenv -p 'interpreter path' 'virtual environment name'
- example: virtualenv -p /usr/bin/python3 virtualenv_name
