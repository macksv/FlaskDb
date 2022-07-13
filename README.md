# FlaskDb
Demo on Flask which uses DB, Docker and CI/CD using Github Actions. Container application deploys to Heroku.
The app is a Task Tracker which enables the user to add, edit and delete tasks which gets stored in a Database (sqlite).
Once a push or pull requests happens on Github, the app automatically gets unit tested (pytest). If it passes, then a Docker
image is created and this is automatically pushed to the Heroku repository where the web pages are served.
