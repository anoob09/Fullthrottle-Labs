# FullThrottle Labs Django App

**Since there wasn't a lot of information available about the assignment, I have made a few assumptions.** 

## Custom Management Command
### Insert into User
- The command takes 1 argument i.e. the number of users that needs to be generated.
- The command prints a message stating the `user with following userid has been successfully generated`.
- The command uses `get_random_string()` to create userid, name and timezone.
### Insert into ActivityPeriod
- The command takes 2 arguments, 1st is the userid of the user for which the dummy data has to be generated and the 2nd argument is the number of dummy records that has to be generated.
- It prints a message for every successful record generated along with the userid.
- The command prints and error message if the userid is not already present in the user table because the `userid` field is a `Foreign Key` field referencing `id` field of `User` model.

## View & Request
- The request will a post request.
- The request will be containing a json which will contain a list of id for which the data is to be returned.
- I date-time value in ActivityPeriods is string (I had little time so I used string to store them).

## Models
- User is the main table having 3 id (Primary Key), real_name and tz as columns.
- ActivityPeriods the table having 3 user (Foreign Key with User.id as Reference, on_delete.CASCADE), start_time and end_time as columns.
- I assumed the relation between two tables is one-to-many where one record from User is related to many records from ActivityPeriod since a user can have more then one session.
- I believe this is the best way to store data by preserving the relationship between models.
- The id field in User is Foreign Key to user field in ActivityPeriod.

## App
- The project consists of only 1 app i.e `myapi`.

## Building

It is best to use the python `virtualenv` tool to build locally:

```sh
$ virtualenv-2.7 venv
$ source venv/bin/activate
$ pip install -r requirements.txt
$ DEVELOPMENT=1 python manage.py runserver
```

Then visit `http://localhost:8000` to view the app.

## Deploy to Heroku

Run the following commands to deploy the app to Heroku:

```sh
$ git clone https://github.com/anoob09/Fullthrottle-Labs.git
$ cd Fullthrottle-Labs
$ heroku create
$ heroku addons:add fullthrottle:dev
$ git push heroku master:master
$ heroku open
```

