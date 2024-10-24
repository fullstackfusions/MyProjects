## Setup.py file

first you will require `setup.py` file.

in which setuptools has been setup.

```python
from setuptools import setup

if __name__ == "__main__":
    setup()
```

## create binary distribution wheel

using `bdist_wheel` along with setup.py

for example: `python setup.py bdist_wheel`

## install `wheel` package

`pip install wheel`

## create source distribution file

using `sdist` along with setup.py

for example: `python setup.py sdist`

## you can setup requirements.txt file for additional settings like I mentioned in requirements.txt

now to host package on pypi

you must use `twine` module which will verify all necessary things require for packages.

`twine upload dist/*`

this command will upload distribution on pypi
will ask for pypi credentials username and password
