import requests

url = "https://api.telegram.org/bot...token..."     # Bot url woth bot token

''' Get All Updates JSON format '''
def get_updates_json(reqeust):
    response = requests.get(requests + 'getUpdates')
    return response.json()

''' Get Latest Update '''
def last_update(data):
    results = data['result']
    last_update = len(results) - 1
    return results[last_update]
