import requests
import const
import json

URL = "https://api.telegram.org/bot"+const.token


def get_updates_json():
    response = requests.get(URL + '/getUpdates')
    return response.json()

def get_userdata():
    data = {'': 0}
    userdata = get_updates_json()
    user_id = userdata['result'][-1]['message']['from']['id']
    user_text = userdata['result'][-1]['message']['text']
    data = {user_text: user_id}
    return data

def send_message(chat_id, text):
    url = URL + '/sendMessage?chat_id='+chat_id+'&text='+text
    requests.get(url)

if __name__ == '__main__':
    main()
