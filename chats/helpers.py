import os
import requests
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
import json

key = os.environ.get('YANDEX_API_KEY')

def get_translation(text, language):
    response = requests.get(f'https://translate.yandex.net/api/v1.5/tr.json/translate?key={key}&text={text}& poop&lang=lt-en').json()
    print('resp1', response)
    resp = response['text'][0]

    print(resp)
    return resp

    # json.dumps({
    #         'message': message
    #     })