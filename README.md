# All-In-One-Predictor
Collections of predictor

## Project Setup

virtualenv is a tool to create isolated Python environments. Since Python 3.3, a subset of it has been integrated into the standard library under the venv module. The venv module does not offer all features of this library, to name just a few more prominent:

- is slower (by not having the app-data seed method),
- is not as extendable,
- cannot create virtual environments for arbitrarily installed python versions (and automatically discover these),
- is not upgrade-able via pip,
- does not have as rich programmatic API (describe virtual environments without creating them).

**1. Create a Virtual Environment**

- *On macOS and Linux:*
  ```bash
    python3 -m venv env
  ```
- *Windows*
  ```bash
    py -m venv env
  ````

**2. Activate the Virtual Environment**
  - *On Windows*
    ```bash
    
    ```
  - *On macOS and Linux:*
    ```bash
    source env/bin/activate
    ```
**3. Install dependencies using**
```bash
pip install -r requirements.txt
```

**4. Make Migrations**

```bash
  python manage.py makemigrations
  python manage.py migrate
```
**5. Run Server**

```bash
  python manage.py runserver
```
**6. Create admin**

```bash
  python manage.py createsuperuser
```

Congratulations! You've created your virtual environment.
