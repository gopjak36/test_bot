import requests

url = "https://api.telegram.org/bot...token..."     # Bot url with bot token

''' Get All Updates JSON format '''
def get_updates_json(reqeust):
    response = requests.get(requests + 'getUpdates')
    return response.json()

''' Get Latest Update '''
def last_update(data):
    results = data['result']
    last_update = len(results) - 1
    return results[last_update]

''' Get Chat id from Last Update '''
def get_chat_id(update):
    chat_id = update['message']['chat']['id']
    return chat_id

''' Send Message '''
def send_mess(chat, text):
    param = {'chat_id':chat,'text':text}
    response = requests.post(url + 'sendMessage', data=params)
    return response

chat_id = get_chat_id(last_update(get_updates_json(url))) # Chat id
send_mess = send_mess(chat_id, 'Message text here!') # Send Message            
