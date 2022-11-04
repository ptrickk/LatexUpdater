#Latex und Git Updater

## Information
This project contains scripts to automatically update compile your latex project (.tex) into a pdf and to automatically push changes of your project to an existing remote repository.

### Installation and usage
After cloning the project, copy or move the scripts into your local repository (you probably want to add them to your .gitignore).

### Auto LaTeX compiler
To start the automatic LaTeX comiler just run the upTex.py script and enter the name of the LaTeX file (.tex) you want to compile. The scipt is going to create and update a PDF file every few seconds.

### Auto Git Updater
For the auto Git-Updater just run the upGit.py script and enter pass the name of the remote-connection you want to push your changes to (if you dont pass anything it will use "origin"). After that every 30 seconds a new commit and push will take place.
