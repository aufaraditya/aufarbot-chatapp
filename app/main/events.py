from flask_socketio import emit
from .similarities import get_response
from .. import socketio

@socketio.on('userchat')
def handleMessage(usermessage, methods=['POST']):
	botmessage = get_response(usermessage['message']) #Get message for Bot from similarities.py file
	usermessage.update({'bot':botmessage}) #Add Bot message/response
	emit('botchat', usermessage) #Return with addition Bot message/response








