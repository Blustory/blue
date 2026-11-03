# Flask Learning

A hands-on starter guide for learning Flask, Python's lightweight web framework.

## Overview

Use this project to explore the core building blocks of a Flask web application.
Start small, experiment with each concept, and build features incrementally.

## Learning goals

- Create routes and return HTTP responses.
- Render pages with Jinja templates.
- Handle and validate form input.
- Organize related functionality with blueprints.
- Configure an app for different environments.
- Write tests for routes and application behavior.

## Requirements

- Python 3.9 or newer.
- pip, the Python package installer.
- A terminal or command prompt.
- Git is optional but useful for version control.

## Setup

1. Open this repository's directory in a terminal.
2. Create a virtual environment for project dependencies.
3. Activate the environment for your operating system.
4. Install Flask and any project requirements.

### Create an environment

```bash
python -m venv .venv
```

On Windows, activate the environment with PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

On macOS or Linux, activate it with:

```bash
source .venv/bin/activate
```

### Install dependencies

If the repository has a `requirements.txt` file, install its packages:

```bash
python -m pip install -r requirements.txt
```

For a minimal setup, install Flask directly:

```bash
python -m pip install Flask
```

## Run the application

If the project entry point is named `app.py`, run:

```bash
python app.py
```

Alternatively, start it with Flask's command-line interface:

```bash
flask --app app run --debug
```

Open the local address shown in the terminal, usually http://127.0.0.1:5000.
Debug mode is intended for local development, not production deployments.

## Minimal example

```python
from flask import Flask

app = Flask(__name__)

@app.get("/")
def home():
    return "Hello, Flask!"

if __name__ == "__main__":
	app.run(debug=True)
```

## Suggested next steps

1. Add routes for a home page and a detail page.
2. Create a `templates/` directory and render a Jinja template.
3. Add shared page layout and static CSS files.
4. Build a form and validate submitted input.
5. Add tests using Flask's test client and `pytest`.
6. Refactor related routes into a blueprint as the app grows.

## Security notes

Keep secrets in environment variables rather than committed source code.
Never use Flask's development server or debug mode in production.
