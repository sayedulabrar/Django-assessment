# Employer Management System (DRF)

## Features
- Custom User model with JWT Auth
- User registration, login, and profile
- CRUD for Employers

## Setup
```bash
git clone <repo>
cd employer_project
pip install -r requirements.txt
python manage.py migrate
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

```
