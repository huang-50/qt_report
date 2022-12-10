import getpass
from db import encrypt

def generate_token():
    # enter username
    username = input("Enter username: ")
    # password = input("Enter password: ")
    # password invisible when typing
    password = getpass.getpass("Enter password: ")
    # generate token
    token = encrypt(username + "/" + password)
    # print(_key)
    print('token:', token)

generate_token()
