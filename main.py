import vk_api
import pyperclip
import os
from random import randint
# from playsound import playsound
import globals


def auth_handler():
    key = input("2FA code: ")
    remember_device = True
    return key, remember_device


def api_vk():
    login, password = '+########', '######'  # Change for current profile
    vk_session = vk_api.VkApi(login, password, auth_handler=auth_handler)
    try:
        vk_session.auth(token_only=True)
    except vk_api.AuthError as error_msg:
        print(error_msg)
        return
    vk = vk_session.get_api()
    tools = vk_api.VkTools(vk_session)
    return vk, tools


def main():
    response = tools.get_all('photos.get', 50, {'owner_id': ######, 'album_id': "saved"}) # Change # for current profile ID
    vk, tools = api_vk()
    globals.init()
    answer = ''
    counter = 1
    print("Type 0 for exit:")
    while answer == '':
        rnd = randint(0, len(response['items']))
        itemresponselength = len(response['items'][rnd]['sizes'])
        item = response['items'][rnd]['sizes'][itemresponselength - 1]['url']

        pyperclip.copy(item)
        # playsound("fx.mp3")
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Done:", counter)
        counter += 1
        os.startfile(item)
        answer = input()
    return 0
    //TODO create DB to not overwhelm vk server


if __name__ == '__main__':
    main()
