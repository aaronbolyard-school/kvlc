# Kvlc, a faux-Russian calculator
Allows you to perform simple arithmetic.

## Install
Run these commands (assuming Windows 10 & PowerShell):

```
python -m venv venv
cmd
venv\Scripts\activate.bat
pip install flask flask_bootstrap
```

## Running
Run these commands:

```
cmd
venv\Scripts\activate.bat
set FLASK_APP=photomanager
set FLASK_ENV=development
python -m flask run # pytest to run unit tests
```

## Unit Tests
The project comes with unit tests for the model.