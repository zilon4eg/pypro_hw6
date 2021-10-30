import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


def auth_ya_disk(my_login, my_pass):
    driver = webdriver.Chrome(executable_path='chromedriver_win32\chromedriver.exe')
    url = 'https://passport.yandex.ru/auth/'
    driver.get(url)
    login = driver.find_element_by_name('login')
    login.send_keys(my_login)
    login.send_keys(Keys.RETURN)
    time.sleep(1)
    pswd = driver.find_element_by_name('passwd')
    pswd.send_keys(my_pass)
    pswd.send_keys(Keys.RETURN)
    time.sleep(1)
    errors = []
    errors.append(driver.find_elements_by_class_name('captcha__reload'))
    errors.append(driver.find_elements_by_class_name('Textinput-Hint_state_error'))
    if errors[1]:
        print('Неверный пароль.')
    elif errors[0]:
        print('Увы, нужно ввести капчу.')
    assert 'No results found.' not in driver.page_source
    driver.close()
    driver.quit()
    return errors


def create_ya_folder(folder_name):
    with open('ya_api_token.txt', 'r') as file:
        for line in file:
            token = line

    base_url = 'https://cloud-api.yandex.net:443/'
    ya_headers = {
        'accept': 'application/json',
        'authorization': f'OAuth {token}'
    }
    result = requests.put(base_url + 'v1/disk/resources', headers=ya_headers, params={'path': folder_name}).json()
    return result


if __name__ == '__main__':
    create_ya_folder('test')
    auth_ya_disk('test2', 'test2')
