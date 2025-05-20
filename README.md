# Employer Management System (DRF)

## Features
- Custom User model with JWT Auth
- User registration, login, and profile
- CRUD for Employers

## Setup
```bash
# 1. Clone the repository
git clone https://github.com/sayedulabrar/Django-assessment.git
cd Django-assessment

# 2. Create and activate virtual environment
python -m venv env
env\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Apply migrations
cd employer_project
python manage.py makemigrations
python manage.py migrate

# 5. (Optional) Create superuser for admin panel
python manage.py createsuperuser

# 6. Run the development server
python manage.py runserver
````

## Endpoints

* `POST /api/auth/signup/`
* `POST /api/auth/login/`
* `GET /api/auth/profile/`
* `POST /api/employers/`
* `GET /api/employers/`
* `GET /api/employers/<id>/`
* `PUT /api/employers/<id>/`
* `DELETE /api/employers/<id>/`
* `POST /api/auth/logout/`

```
