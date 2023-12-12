from task2 import posts, create_post
import pytest
import yaml
import requests

with open('./task2/config.yaml') as f:
    data = yaml.safe_load(f)

def test_id_post(token):
    assert data['check_id'] in posts(token)

def test_create_post(token):
    assert 'testtt' in create_post(token, 'title', 'testtt', 'content')


if __name__ == '__main__':
    pytest.main(['-vv'])