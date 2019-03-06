# Collect-Clone
Repo For Task given by @SocialCops for SE Summer Intern

## TechStack

The following tech-stack has been used in the process:

- Python 3.7
- Flask
- Gunicorn
- Sqlite 3
- 


## Caveats

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