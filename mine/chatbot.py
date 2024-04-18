res = {
'hi': 'hello how can i help you?',
'how are you': 'i am fine ',
'who are you': 'i am simple chatbot'
}


def get_response(que):
	if que in res:
		print('bot : '+res[que])
	else:
		print('bot: I could not understand your question')

print('bot : hello how can i help you today')
while(1):
	que = input('you : ')
	if que != 'by':
		get_response(que)	
	else:
		print('bot : By see you.')
		break;