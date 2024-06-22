# Django Employment Contracts

## Setup

---

## Prerequisites

- Python (3.x recommended)
- Django
- Django REST Framework
- Virtual environment (optional but recommended)

## Installation

1. Clone the repository:

- git clone <repository_url>
- cd employment_contracts

2. Set up a virtual environment (optional but recommended):

- python -m venv venv
- source venv/bin/activate

3. Install dependencies:

- pip install -r requirements.txt

## Database Setup

Using default django SQLite database

---

- python manage.py makemigrations
- python manage.py migrate
- Run python populate_database.py to populate the database with dummy data

## Running the Server

- python manage.py runserver

## API Endpoints

- create a new user in order to get authorization token to access the api endpoints
- access each endpoint by adding Authorization to your header "Token _your_token_"

---

## Access API Endpoints

### Employment Agreements

- List/Create: /api/employment-agreements/
- Retrieve/Update/Delete: /api/employment-agreements/<id>/
- Search: /api/employment-agreements/search/

### Authentication

- Signup: /api/signup/
- Login: /api/login/

## Testing

- python manage.py test

# License

This project is licensed under the MIT License
