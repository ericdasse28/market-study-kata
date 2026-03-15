# market-study-kata

## Iteration 1: adding Poetry to an existing project

1. Install [Poetry](https://python-poetry.org/docs/1.8#installing-with-pipx)
   > **/!\ IMPORTANT:** Deactivate any activated virtual environment before you install Poetry
2. Use poetry to generate a `pyproject.toml`
   ```
   poetry init
   ```
3. Configure poetry so that it generates the virtual environment inside the project
   ```
   poetry config virtualenvs.in-project true
   ```
   You're all set!

## Iteration 2: introduce linting and formatting

### Formatting with Black & isort

1. Specify and install `black` and `isort` as dev dependencies as follows:
   ```
   poetry add -G dev black isort
   ```
2. Is the codebase currently formatted according to Black style? If not, apply Black formatting on it
3. Are the imports sorted currently sorted correctly?
4. Configure your VS Code so that Black automatically formats Python files on save
   > **Tip:** Search the _Black Formatter_ extension in VS Code extensions tab
5. Likewise, configure your VS Code so it uses isort.

### Linting with Flake8

1. Specify and install `flake8` as a dev dependency
2. Run linting on the entire codebase. Notice anything weird?
3. Create a file named `setup.cfg` at the root of the project and add the following:
   ```Properties
   [flake8]
   exclude =
      .venv,
      __pycache__
   ```
   This configuration tells Flake8 to ignore any file that's within your virtual environment
   or in `__pycache__`.
4. Run linting again. Did it detect any problem?
5. Add the Flake8 extension to your VS Code

#### Bonus: sharing recommended VS Code extensions across team

It is possible to make it so VS Code prompts users to install the exact
extensions we are using in the project within their workspace. It can be done
by creating a file named `extensions.json`. Let's make one and add it to version
control.
