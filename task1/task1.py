from zeep import Client, Settings
import yaml

with open('./task1/config.yaml') as f:
    data = yaml.safe_load(f)

def check_word(word):
    url = data['url']
    settings = Settings(strict=False)
    client = Client(wsdl=url, settings=settings)
    print('test')
    print(client.service.checkText(word)[0]['s'])
    return client.service.checkText(word)[0]['s']
