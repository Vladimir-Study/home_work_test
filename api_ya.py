import requests

with open('tocken_ya.txt', 'r', encoding='utf-8') as file:
    token = file.readline()


class ApiYandexDisk():
    '''
    Данный класс создает новую папку с указанным именем на вашем Яндекс.Диск
    класс принимает ваш Апи токен яндекс и имя новой папки
    '''
    def __init__(self, token, name_folder):
        self.token = token
        self.name_folder = name_folder

    def create_new_folder(self):
        url = 'https://cloud-api.yandex.net/v1/disk/resources'

        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': self.token
        }

        params = {
            'path': self.name_folder,
        }

        response = requests.put(url, headers=headers, params=params)

        if response.status_code == 201:
            return 'Folder created'
        elif response.status_code == 409:
            return 'A folder with the same name exists'
        elif response.status_code == 400:
            return 'Incorrect data'
        elif response.status_code == 401:
            return 'Not authorized'
        else:
            return 'Another mistake'

# r = ApiYandexDisk(token, 'q')
# print(r.create_new_folder())