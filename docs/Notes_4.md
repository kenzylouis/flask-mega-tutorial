## Module 4

#### 0. Pre-requisites
Module-3

#### 1. Install `flask-sqlalchemy` 
it that provides a wrapping mechanism around SQL called ORM. Write high level entities such as classes, methods, function to create systematically low level sql object like schemas, tables regardless of the database of choice.
```shell
pip install flask-sqlalchemy
```

####  2. Install `flask-migrate` 

It that help migrate database seemlessly even when the datastructure change
```shell
pip install flask-migrate
```

####  3. Update configuration
Update config.py and add 2 additionals configuration elements for database. if development use sqllite if prod use the URL provided in the environment variable.

#### 4. Update the init function
update`app/__init__.py` to initialise the database for the app.
- create an DB instance of SQLALchemy
- add an object for the migration engine

#### 5. Database models
what are database models:
- data stored in the database will be represented by a collections of classes called database models
- The ORM layer will do the translation from python/flask into into the database

<table>
<tr><th>users </th></tr>
<tr><td>

||||
|--|--|--|
|id|integer|primary key|
|username|varchar(64)||        
|email|varchar(120)||        
|password_hash|varchar(128)||

</td></tr></table>

create the app/models.py
```bash
touch app/models.py
```
verify
```pyhon
>>> from app.models import User
>>> u = User(username='kenzy', email='kenzy@example.com')
>>> u
<User kenzy>
```

create the migration repository
```shell
flask db init

  Creating directory /Users/klouis/projects/python-projects/flask-mega-tutorial/migrations ...  done
  Creating directory /Users/klouis/projects/python-projects/flask-mega-tutorial/migrations/versions ...  done
  Generating /Users/klouis/projects/python-projects/flask-mega-tutorial/migrations/script.py.mako ...  done
  Generating /Users/klouis/projects/python-projects/flask-mega-tutorial/migrations/env.py ...  done
  Generating /Users/klouis/projects/python-projects/flask-mega-tutorial/migrations/README ...  done
  Generating /Users/klouis/projects/python-projects/flask-mega-tutorial/migrations/alembic.ini ...  done
  Please edit configuration/connection/logging settings in '/Users/klouis/projects/python-projects/flask-mega-tutorial/migrations/alembic.ini' before proceeding.
```
- the perform the first database migration. You can use -m to add comments to the migration
```shell
flask db migrate -m "users table"

INFO  [alembic.runtime.migration] Context impl SQLiteImpl.
INFO  [alembic.runtime.migration] Will assume non-transactional DDL.
INFO  [alembic.autogenerate.compare] Detected added table 'user'
INFO  [alembic.autogenerate.compare] Detected added index 'ix_user_email' on '['email']'
INFO  [alembic.autogenerate.compare] Detected added index 'ix_user_username' on '['username']'
  Generating /Users/klouis/projects/python-projects/flask-mega-tutorial/migrations/versions/8dbf09d5c896_users_table.py ...  done
```

- The `flask db migrate` command does not make any changes to the database, it generates the migration script. To apply the changes to the database, use `flask db upgrade`.

```shell
flask db upgrade

INFO  [alembic.runtime.migration] Context impl SQLiteImpl.
INFO  [alembic.runtime.migration] Will assume non-transactional DDL.
INFO  [alembic.runtime.migration] Running upgrade  -> 8dbf09d5c896, users table
```

- With database servers like MySQL and PostgreSQL, must create the database in the database server before running `upgrade`.
- by default Flask-SQLAlchemy uses a snake case naming convention for db tables. So if a class is `User` the corresponding table will be `user`. if a class is FamilyAndFriend, the corresponding table is family_and_friend. To specify our own custom name for table, we can use the dunder __tablename__ attribute in the model class.
- use `flask db upgrade` and `flask db downgrade` to apply new schema changes and rollback to previous version of db respectively. downgrade is mostly use in a dev environment.

#### 6. Define database relationships
the 1st table relationship we will define is:
- one-to-many relationship between users and post: one user can write many posts.
<table>
<tr><th>users </th><th>posts</th></tr>
<tr><td>

||||
|--|--|--|
|id|integer|primary key|
|username|varchar(64)||        
|email|varchar(120)||        
|password_hash|varchar(128)||

</td><td>

||||
|---|---|---|
|id|integer|primary key|
|body|varchar(140)||
|timestamp|datetime||
|user_id|integer|foreign key to id in user table|

</td></tr> </table>

#### 7. Create the Post table
Update `models.py` and add a Post class

Next: [module 05](Notes_5.md)