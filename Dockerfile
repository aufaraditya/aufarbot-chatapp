#parent image: official python runtime
FROM python:3.8
#workdir: /app
WORKDIR /aufarbot-app
#copy the current directory contents into the container in the path /app
ADD . /aufarbot-app

#install packages contained in the text
RUN pip install -r requirements.txt
##make port 80 available to the world (outside the container)
#EXPOSE 8081
#execute a py app
CMD ["python", "chat.py"]