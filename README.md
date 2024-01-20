# FullThrottle Labs Django App

**The API might return empty dictionary for the example id becasue I am using in-built SQLLite database and hence the data is lost after each commit to the repository.**

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
- User is the main table having id (Primary Key), real_name and tz as columns.
- ActivityPeriods the table having user (Foreign Key with User.id as Reference, on_delete.CASCADE), start_time and end_time as columns.
- I assumed the relation between two tables is one-to-many where one record from User is related to many records from ActivityPeriod since a user can have more then one session.
- I believe this is the best way to store data by preserving the relationship between models.
- The id field in User is Foreign Key to user field in ActivityPeriod.

## App
- The project consists of 2 apps `fullthrottle_labs` & `myapi`.

## API ENDPOINTS

![POST/sendjson](https://fullthorottle-labs.herokuapp.com/sendjson/)

POST request to get JSON data
<br>*Requires Authentication*

#### Request Body
| Feild        | Description                             | Required |
| :----------- | :-------------------------------------- | :------- |
| id_list          | The of id for which JSON data is required                 | True     |

Example of JSON to be included in post body

`{"id_list" : ["W012A3CDE", "W07QCRPA4"]}`

#### Response
| Status Code | Message                      | Reason                                                         |
| :--         | :--------------------------- | :------------------------------------------------------------- |
| 200         | Data send        | User JSON data send successfully                                    |

Example of JSON data recieved 
`{
    "ok": true,
    "members": [
        {
            "id": "W012A3CDE",
            "real_name": "Egon Spengler",
            "tz": "America/Los_Angeles",
            "activity_periods": [
                {
                    "start_time": "Feb 1 2020  1:33PM",
                    "end_time": "Feb 1 2020 1:54PM"
                },
                {
                    "start_time": "Mar 1 2020  11:11AM",
                    "end_time": "Mar 1 2020 2:00PM"
                },
                {
                    "start_time": "Mar 16 2020  5:33PM",
                    "end_time": "Mar 16 2020 8:02PM"
                }
            ]
        },
        {
            "id": "W07QCRPA4",
            "real_name": "Glinda Southgood",
            "tz": "Asia/Kolkata",
            "activity_periods": [
                {
                    "start_time": "Feb 1 2020  1:33PM",
                    "end_time": "Feb 1 2020 1:54PM"
                },
                {
                    "start_time": "Mar 1 2020  11:11AM",
                    "end_time": "Mar 1 2020 2:00PM"
                },
                {
                    "start_time": "Mar 16 2020  5:33PM",
                    "end_time": "Mar 16 2020 8:02PM"
                }
            ]
        }
    ]
}`


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

