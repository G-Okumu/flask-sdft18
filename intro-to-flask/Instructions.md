# Introduction to Flask

- This README documents what we covered today while getting started with Flask, Python virtual environments, routes, and returning response from a simple Flask API.

## What We Learned
Today we covered:
1. What Flask is and why it is useful for building web applications and APIs.
2. How to create a minimal Flask application.
3. How to create and use a Python virtual environment with venv.
4. How to install Flask inside an isolated environment.
5. How Flask routes URLs to Python functions.
6. How to create a basic / route.
7. How to create a /todos API endpoint.
8. How Flask can automatically convert a Python dictionary/list response into a JSON response.
9. How to run a Flask application in debug mode.
10. The difference between venv and Pipenv and when each is appropriate.


# Setting Up the Virtual Environment

A virtual environment isolates the packages for one Python project from the rest of the computer.

This is important because different projects may require different versions of the same package.

For example:

- Project A → Flask 3.x
- Project B → Flask 2.x

Without isolated environments, packages installed globally can interfere with one another.

---

## Option 1: Using `venv`

This is the approach we used today.

Python includes `venv`, so no additional environment-management tool is required.

### 1. Create the project

```bash
mkdir flask-project
cd flask-project
```

### 2. Create the virtual environment

```bash
python -m venv .venv
```

On some systems, you may need:

```bash
python3 -m venv .venv
```

This creates a `.venv` directory containing the isolated Python environment.

### 3. Activate the environment

#### Linux/macOS

```bash
source .venv/bin/activate
```

#### Windows Command Prompt

```cmd
.venv\Scripts\activate
```

#### Windows PowerShell

```powershell
.venv\Scripts\Activate.ps1
```

Once activated, your terminal will usually show something similar to:

```text
(.venv) $
```

### 4. Install Flask

```bash
pip install Flask
```

### 5. Verify Flask

```bash
pip show Flask
```

You can also check the Python interpreter.

#### Linux/macOS

```bash
which python
```

#### Windows

```cmd
where python
```

The Python executable should point to the virtual environment.

### 6. Save dependencies

Once the project dependencies are installed:

```bash
pip freeze > requirements.txt
```

This creates a `requirements.txt` file containing the installed dependencies.

Another developer can recreate the environment with:

```bash
pip install -r requirements.txt
```

---

## Option 2: Using Pipenv

[Pipenv](https://pipenv.pypa.io/) is another tool for managing Python dependencies and virtual environments.

Unlike plain `venv`, Pipenv combines environment management with dependency management through:

- `Pipfile`
- `Pipfile.lock`

Pipenv can automatically create a virtual environment when you run `pipenv install` in a project that does not already have one.

### Install Pipenv

Once Pipenv is available, check that it is installed:

```bash
pipenv --version
```

### Create a Pipenv environment

From the project directory:

```bash
pipenv install Flask
```

This will:

- Create a virtual environment if one does not exist.
- Install Flask.
- Create or update `Pipfile`.
- Create or update `Pipfile.lock`.

### Activate the environment

```bash
pipenv shell
```

Alternatively, commands can be executed without activating the shell:

```bash
pipenv run python app.py
```

### Check the environment

```bash
pipenv --venv
```

This shows where Pipenv created the virtual environment.

---

## venv vs Pipenv

| Feature | `venv` | Pipenv |
|---|---|---|
| Built into Python | Yes | No |
| Creates virtual environments | Yes | Yes |
| Dependency management | Basic | Built in |
| Dependency file | `requirements.txt` | `Pipfile` |
| Locked dependencies | Not built in | `Pipfile.lock` |
| Simplicity | Very simple | More features |
| Good for learning Python | Excellent | Good |
| Good for small projects | Excellent | Good |
| Useful for larger dependency-managed projects | Good | Good |

---

## When Should I Use `venv`?

Use `venv` when:

- You are learning Python or Flask.
- You want the simplest possible setup.
- The project has relatively few dependencies.
- You are comfortable maintaining `requirements.txt`.
- You want to use Python's built-in tooling without adding another dependency-management tool.

**This is what we used today.**

For this introductory Flask project, `venv` is enough.

---

## When Should I Use Pipenv?

Pipenv becomes useful when you want dependency management and virtual-environment management to work together.

It can be particularly useful when:

- A project has many dependencies.
- You want a `Pipfile` describing the project's direct dependencies.
- You want a `Pipfile.lock` recording resolved dependency versions and hashes.
- You want a more structured dependency workflow across development and deployment.
- Reproducibility of dependencies is important.

Pipenv projects typically commit both `Pipfile` and `Pipfile.lock` to version control.

---

## Important

You do **not** need to use both `venv` and Pipenv for the same project.

Choose one environment-management approach for the project.

For this introductory Flask project, we are using:

```text
Python
   ↓
venv
   ↓
Flask
   ↓
requirements.txt
```
