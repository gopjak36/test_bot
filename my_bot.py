# -*- coding: utf-8 -*-
import requests
import datetime

class Bot:
    ''' Bot class '''

    def __init__(self, token):
        self.token = token
        self.api_url = "https://api.telegram.org/bot{}".format(token)

    def get_updates(self, offset=None, timeout=30):
        ''' Get All Updates JSON format '''
        method = 'getUpdates'
        params = {'timeout':timeout, 'offset':offset}
        response = reqeusts.get( self.api_url + method, params)
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


''' Main method using long polling '''
def main():
    pass

if __name__ == '__main__':
    main()
