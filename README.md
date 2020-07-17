# Django-RPS
Live demo [here](https://django-rps.herokuapp.com/).

A user-based application where the results of playing "Rock, Paper, Scissors" against the computer are automatically tallied and stored to the database. Each user also has a profile page that only they can view and edit.

Possible TODO
- venv instructions

# Usage

```
pip3 install -r requirements.txt
cd website
gunicorn --bind 0.0.0.0:80 website.wsgi
```
