# Collect-Clone
Repo For Task given by @SocialCops for SE Summer Intern

## TechStack

The following tech-stack has been used in the process:

- Python 3.7
- Flask
- Gunicorn
- Sqlite 3
- HTML
- Heroku [https://collect-demo.herokuapp.com/]

There are other libraries used for minor purposes. For e.g. pylint has been used for linting and code sanitization purposes.

## Documentation

The code is aptly documented with python doc-strings that are the best way to provide documentation in a python project. They can be used to create a web documentation using Sphinx or any similar service.

### To Run

#### Without Docker

Follow the below steps to run the REST API:

- Install Python 3.7 and pip
- `pip install pipenv`
- `cd /path/to/project`
- `pipenv install --dev`
- `gunicorn collect-demo.wsgi:app`
- Access the endpoints on 127.0.0.1:8000

NOTE: The above instructions were tested on Debian Stretch with Python 3.7.2

#### With Docker

The program has been dockerised for ease of deployment. This is the easier of the two methods in which the program can be accessed.

- Install docker and docker-compose
- `cd /path/to/project/`
- `docker-compose up`  # this will build only the first time, to rebuild add `--build`
- Access the endpoints on 127.0.0.1:5000

## Caveats

#### Deployment on Heroku is non-functional

I had planned to make a separate version of the application for Heroku which would take remote database and hence would be able to work on heroku server but was not able to find time for the same.

#### Incomplete Work

Due to academic activities and campus involvements, I devoted as much as time possible and completed the backend of the application but was not able to work on the
frontend and finishing of the task.


#### Using In-built Sqlite

Since it is convenient to use the in-built database handler,
the project uses sqlite3 from python. This is convenient in case of projects
with long but less number of write requests; once the number of requests
increase, the database slows down since the writes happens sequentially.

#### Less Data In Example 2

Instead of the specified 20 million rows, dummy data for exmaple 2 has 2 million rows because of the limit github imposes on uploaded file's size.

We could use something like Git-Large_File manager but then it adds on unnecessary complexity in the git management.