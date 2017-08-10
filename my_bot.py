# -*- coding: utf-8 -*-
import requests
import datetime

class Bot:
    ''' Bot class '''

    def __init__(self, token):
        self.token = token
        self.api_url = "https://api.telegram.org/bot{}/".format(token)

    def get_updates(self, offset=None, timeout=30):
        ''' Get All Updates JSON format '''
        method = 'getUpdates'
        params = {'timeout':timeout, 'offset':offset}
        response = requests.get( self.api_url + method, params)
        result_json = response.json()['result']
        return result_json

    def get_last_update(self):
        ''' Get Latest Update '''
        get_result = self.get_updates()

        if len(get_result) > 0:
            last_update = get_result[-1]
        else:
            last_update = get_result[len(get_result)]

        return last_update

    def send_message(self, chat_id, text):
        ''' Send Message '''
        method = 'sendMessage'
        params = {'chat_id':chat_id, 'text':text}
        response = requests.post( self.api_url + method, params)
        return response

''' Help Variables '''
bot = Bot('371331492:AAG0_Ddqkvw-TJr8TxRLig6fNt8mZ1bLXmY')
greetings = (u'здравствуй', u'привет', u'ку', u'здорово')
now = datetime.datetime.now()

''' Main Function '''
def main():
    new_offset = None
    today = now.day
    hour = now.hour

    while True:
        bot.get_updates(new_offset)

        last_update = bot.get_last_update()

        last_update_id = last_update['update_id']
        last_chat_text = last_update['message']['text']
        last_chat_id = last_update['message']['chat']['id']
        last_chat_name = last_update['message']['chat']['first_name']

        if last_chat_text.lower() in greetings and today == now.day and 6 <= hour < 12:
            bot.send_message(last_chat_id, u'Доброе утро, {}'.format(last_chat_name))
            today += 1

        elif last_chat_text.lower() in greetings and today == now.day and 12 <= hour < 17:
            bot.send_message(last_chat_id, u'Добрый день, {}'.format(last_chat_name))
            today += 1

        elif last_chat_text.lower() in greetings and today == now.day and 17 <= hour < 23:
            bot.send_message(last_chat_id, u'Добрый вечер, {}'.format(last_chat_name))
            today += 1

        new_offset = last_update_id + 1

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()
