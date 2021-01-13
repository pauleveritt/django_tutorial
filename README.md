# django_tutorial
The end of the Django official tutorial, setup for PyCharm Professional demos

## Installation

1. Clone this repo, open in PyCharm Professional, which should:
   - Make a virtual environment
   - Prompt to install dependencies from `requirements.txt`
   - Configure the settings that recognize this as a Django project
   - Make a Django run configuration
2. Open PyCharm's `manage.py` console via `Tools | Run manage..py task`
3. `makemigrations` and press enter
3. `migrate` and press enter
4. `createsuperuser` (and answer the questions)
5. Run the created run config (probably named `django_tutorial`)
6. Visit `http://127.0.0.1:8000/admin/` and add a question
7. Visit `http://127.0.0.1:8000/polls/`
