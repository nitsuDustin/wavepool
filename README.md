# Wavepool
Industry Dive's django code exercise for software engineer candidates

## Requirements
* Python 3* 
* Pipenv or similar

## Install & run
Using pipenv:

Install an environment using python 3
`pipenv install --python your-path-to-python3`

SSH into your environment
`pipenv shell`

Install environment requirements
`pip install -r requirements.txt`

Run migrations for the app
`python manage.py migrate`

Serve the app locally
`python manage.py runserver`

## Use
Navigate in your browser to the wavepool homepage at `http://127.0.0.1:8000/`

Click on the "Instructions" link to view the coding exercises.

## CMS
Navigate to `http://127.0.0.1:8000/admin` and use the username `divecandidate` and password `divecandidatetest` to log in.