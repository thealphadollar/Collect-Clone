# Collect-Clone
Repo For Task given by @SocialCops for SE Summer Intern


## Caveats


#### Using In-built Sqlite

Since it is convenient to use the in-built database handler,
the project uses sqlite3 from python. This is convenient in case of projects
with long but less number of write requests; once the number of requests
increase, the database slows down since the writes happens sequentially.

#### Less Data In Example 2

Instead of the specified 20 million rows, dummy data for exmaple 2 has 2 million rows because of the limit github imposes on uploaded file's size.

We could use something like Git-Large_File manager but then it adds on unnecessary complexity in the git management.