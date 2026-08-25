# Small Wins

Small Wins is a tiny task list built with Django. It is intentionally small so
the GitHub Actions workflow is easy to follow.

## Run locally

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Open <http://127.0.0.1:8000/> in a browser.

## Checks

The same commands used by GitHub Actions can be run locally:

```bash
python manage.py check
python manage.py collectstatic --noinput
python manage.py test
ruff check .
```

The workflow runs the build, test, and lint jobs for every branch push and for
pull request activity.