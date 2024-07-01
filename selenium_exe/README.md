# Overview
This repository contains a Python script using Selenium WebDriver to automate testing of a login functionality for a web application. The script tests various scenarios, including successful login and logout, and handling invalid credentials with appropriate error messages.

## Features:
* Automated login using valid and invalid credentials.
* Error handling for incorrect username and password.
* Automated logout after a successful login.
* URL verification to ensure correct navigation.

## Usage
### 1. Clone the repository
```
git clone <git path>
```

### 2. Activate venv
```
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt
```

### 3. Run the test
```
python app.py
```

