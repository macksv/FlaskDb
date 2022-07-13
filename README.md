# FlaskDb
The main purpose of this repo is to demonstrate Docker and CI/CD concepts using Github Actions.
The app is a Task Tracker which enables the user to add, edit and delete tasks which gets stored in a Database (sqlite).
Github actions perform the following once a push or pull requests happen:
     1. sets up the environment to run on (ie OS and the particular Python version)
     2. installs the Python modules the app requires as specified in requirements.txt
     3. runs the unit test using pytest
     4. if test pass, it pushes the Docker image to Heroku repository where the web pages are served

