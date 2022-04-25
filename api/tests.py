import random

import requests
from django.test import TestCase


# POST客户端上传客户端号和分数
def test_upload_score():
    base_url = 'http://127.0.0.1:8000/api'
    for i in range(1, 11):
        score = random.randint(1, 10000000)
        json_data = {'client_no': i, 'score': score}
        response = requests.post(base_url + '/upload/score', json=json_data)
        print(response.status_code)
        result = response.json()
        print(result)


def test_ranking_list():
    base_url = 'http://127.0.0.1:8000/api'
    json_data = {'client_no': 5, 'start': 1, 'end': 5}
    response = requests.post(base_url + '/ranking/list', json=json_data)
    print(response.status_code)
    result = response.json()
    print(result)


if __name__ == '__main__':
    test_upload_score()
    test_ranking_list()