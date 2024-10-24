Popular tool for generating documentation in Python is **pdoc**. pdoc is simpler and more lightweight compared to Sphinx, and it's especially good for auto-generating API documentation directly from your Python source code's docstrings. Here’s how you can use pdoc to generate documentation:

1. **Install pdoc**:
   You can install pdoc via pip:

   ```
   pip install pdoc3
   ```

2. **Generate Documentation**:
   To generate HTML documentation for a module or package, run pdoc from the command line, specifying the package or module:

   ```
   pdoc --html your_module_name --output-dir docs
   ```

   This command will generate HTML documentation for `your_module_name` and place it in the `docs` folder. If `your_module_name` is a package, pdoc will recursively generate documentation for all its submodules.

3. **View Documentation**:
   The generated HTML files will be in the `docs` directory, and you can open them in any web browser to view the documentation.

pdoc provides a very straightforward and clean output, making it excellent for smaller projects or when you need something set up quickly without much configuration.
