import requests
from time import sleep

url = "https://api.telegram.org/bot371331492:AAG0_Ddqkvw-TJr8TxRLig6fNt8mZ1bLXmY//"     # Bot url with bot token

''' Get All Updates JSON format '''
def get_updates_json(request):
    params = {'timeout': 100, 'offset': None}
    response = requests.get(request + 'getUpdates', data=params)
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
    params = {'chat_id':chat,'text':text}
    response = requests.post(url + 'sendMessage', data=params)
    return response

''' Main method using short polling '''
def main():
    update_id = last_update(get_updates_json(url))['update_id']
    while True:
        if update_id == last_update(get_updates_json(url))['update_id']:
           send_mess(get_chat_id(last_update(get_updates_json(url))), 'test')
           update_id += 1
    sleep(1)

if __name__ == '__main__':
    main()
