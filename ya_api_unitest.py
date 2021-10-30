import requests
import unittest
import ya_api


def metainfo(folder_name):
    with open('ya_api_token.txt', 'r') as file:
        for line in file:
            token = line
    base_url = 'https://cloud-api.yandex.net:443/'
    ya_headers = {
        'accept': 'application/json',
        'authorization': f'OAuth {token}'
    }
    response = requests.get(base_url + 'v1/disk/resources', headers=ya_headers, params={'path': folder_name})
    return response


class TestSomething(unittest.TestCase):
    def setUp(self):
        print("method setUp")


    def tearDown(self):
        print("method tearDown")


    def test_create_ya_folder(self):
        ya_api.create_ya_folder('test')
        response = metainfo('test')
        self.assertEqual(response.status_code, 200)


    def test_auth_ya_disk(self):
        self.assertFalse(ya_api.auth_ya_disk('test', 'test'))