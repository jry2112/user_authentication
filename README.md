curl https://raw.githubusercontent.com/jehna/readme-best-practices/master/README-default.md > README.md

# user_authentification
PPAB: SQL + Python, allows user to authenticate users saved to the database and add users to database. Users have the option to use YAML config file or SQL database

This project was made using Robert Heaton's Programming Projects for Advanced Beginners. You can find it here: https://robertheaton.com/2019/08/12/programming-projects-for-advanced-beginners-user-logins/

## Breakdown of Files

1) login.py: When run, the program will request the user to enter their username and password. If the user exists, they will see an "Access Granted" message. If not, they will get an "Access Denied" message. 
By default, the program uses "ppab6.db" as its database. However, the "users.yaml" file can be used by uncommenting lines 14-18 to import, open, and load a yaml file and lines 71-94. 

2) setup_db.py: Creates db "ppab6.db". If the database already exists, users have the option to overwrite and recreate. 

3) add_user.py: Creates a new user and adds to "ppab6.db". If username is taken, user will be prompted to choose another name. 

The database and yaml files are included for samples. Users can create their own db and yaml files, but should be named "ppab6.db" or "users.yaml"

Note: Passwords are hashed and stored with sha256 hexadecimal.
