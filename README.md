# FlaskDb
The main purpose of this repo is to demonstrate Docker and CI/CD concepts using Github Actions.
The app is a Task Tracker which enables the user to add, edit and delete tasks which gets stored in a Database (sqlite).
Once a push or pull requests happens on Github, the app automatically gets unit tested (pytest). If it passes, then a Docker
image is created and this is automatically pushed to the Heroku repository where the web pages are served.
