# FlaskDb
The main purpose of this repo is to demonstrate Docker and CI/CD concepts using Github Actions.
The app is a Task Tracker which enables the user to add, edit and delete tasks which gets stored in a Database (sqlite).
Github actions perform the following once a push or pull requests happen:
* sets up the environment to run on (ie OS and the particular Python version)
* installs the Python libraries the app requires as specified in requirements.txt
* runs the unit test using pytest
* if test pass, it pushes the code plus Dockerfile to Heroku repository where the image is built and then web pages are served

