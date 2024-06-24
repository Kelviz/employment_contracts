#!/bin/bash

# Install dependencies
pip install -r requirements.txt

# Run Django migrations
python manage.py makemigrations
python manage.py migrate

# Run custom script to populate the database
python populate_database.py
