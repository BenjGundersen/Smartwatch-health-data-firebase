# Overview

For this project, I decided to look into Firestore databases using Google Firebase. This was tricky for me, becuase I am unfamiliar with both cloud things and database things.
I wanted to learn what kinds of things are possible though, so I decided to make a simple database that contains health information from my smart watch.

Below is a video demonstration that shows the program in action. 

[Software Demo Video](https://youtu.be/MGURxpHkDCM)

# Cloud Database

I used Google Firestore which is a part of Google Firebase.

The structure of the database is very simple. There is a "collection" of "documents". The "collection," in this case, is a given calendar week; and the "documents" are individual days.
Within the "documents," there are variables that store data. Things like calorie count, steps taken for the day, and heart beat information. 

# Development Environment

I used the JetBrains PyCharm Professional program to code the Python segments of the program. 

I also used the ```firebase-admin``` package so that I could import firebase things in the main Python file. 

# Useful Websites

Below are a couple of websites that were very helpful in doing this.

- [Google Firebase](https://firebase.google.com/docs/firestore)
- [Google Cloud](https://cloud.google.com/docs/authentication/client-libraries)

# Future Work

Below are a couple of things that I would like to change or improve upon for the future. 

- Proper user input for putting information in.
- Maybe a menu within the python code that lets the user choose what to do from a couple of options.
- Better password system. 
