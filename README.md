# About
A simple web chatbot app about the Author :)

## Tools
This web app using Flask of python but the Bot only using pure python with simple comparison algorithm

## Library
Additional Library can be found in requirements.txt

## How it Works
Users send message and by using Flask Socket IO it return the user message and Bot message.
Bot Messages are generated with simple comparison algorithm from the source file intents.json

## Docker Command
1. `docker image build -t aufarbot-app .`
2. `docker run -p 5000:5000 -d aufarbot-app`

## What to Improve
Algorithm of the Bot can be improved with NLTK or other Machine Learning Algorithm to obtain more accurate response.

![Screenshot 2022-01-22 191815](https://user-images.githubusercontent.com/5984684/151359161-e4fa4982-dcb9-409e-af2f-4ba73345d881.jpg)



