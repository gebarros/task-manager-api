### API Task Manager 

**Stack**
- Python3
- Django e Django Rest Framework
- SQLite3

**Step by Step**

- Clone the repo

*Running local*

- Create a virtual env: $ python3 -m venv venv
-  Activate the virtual env: $ source activate venv/bin/activate
- Install dependencies: $ pip install -r requirements.txt
- Run app: python manage.py runserver
- App running on: http://127.0.0.1:8000/

*Running in docker-compose*

- Install docker
- Build the image: $ docker-compose build
- Run app: $ docker-compose up
- App running on: http://127.0.0.1:8000/
- Stop: $ docker-compose down

*Running tests*

$ coverage run manage.py test

- Show coverage console: app $ coverage report  taskList/views.py taskList/models.py taskList/serializer.py taskList/urls.py

- Get report in html (folder: htmlcov): app $ coverage html  taskList/views.py taskList/models.py taskList/serializer.py taskList/urls.py

*Running coverage without point out specific files, will generate a full report including files from packages we are not interested

*Accessing Logs*

- All the logs are displayed on console, according level defined on .env file 
- Logs from level 'WARNING' will be available in the file: app.logs
- Logs in tests files are disable
- The logs behavior are totally customized: https://docs.djangoproject.com/en/3.1/topics/logging/

**Resourses**

The API has the following endpoints, as requested:

- **/taskList**
- **/taskList/uuid**
- **/tasks**
- **/tasks/uuid**
- **/tags**
- **/tags/uuid**

*They can be easily accessed loading the file TaskManager.postman_collection.json in POSTMAN: https://www.postman.com/

**Data history**

There are tables to control the history of data for each model:

*Accessing tables:* 

$ sqlite3 db.sqlite3 

$ .tables

- taskList_historicaltag     
- taskList_historicaltask    
- taskList_historicaltasklist

...

**Other configs**

- .editorconfig: file that defines indent_style, among other things to standardize the code
- .env: enviroment variables file
- .gitignore: defines what will be load on version control tool

**Observations**

- The project was developed using SQLite3, but a pre configuration is available to use PostgresSQL
- Database file (db.sqlite3) will be kept to be analyzed

**For more information**

gebarrosbio@gmail.com
