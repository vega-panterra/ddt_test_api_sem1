import pytest
import requests
import yaml

with open('./task2/config.yaml') as f:
    data = yaml.safe_load(f)


def posts(token):
    res_get = requests.get(url=data['url'], headers={'X-Auth-Token': token}, params={'owner': 'notMe'})
    list_id = [i['id'] for i in res_get.json()['data']]
    print(list_id)
    return list_id

def create_post(token, title, description, content):
    result = requests.post(url=data['url_create_post'], headers={'X-Auth-Token': token}, params={'title': title, 'description': description, 'content': content})
    res_get = requests.get(url=data['url'], headers={'X-Auth-Token': token})
    list_description = [i['description'] for i in res_get.json()['data']]
    print(list_description)
    return list_description
