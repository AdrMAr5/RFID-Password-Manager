import sys

import serial
from cryptography.fernet import Fernet
from user_input import Actions, InputManager


from PasswordManager import PasswordManager

# arduino = serial.Serial(port='COM5', baudrate=9600, timeout=.1)
#
# while True:
#     print(arduino.readline())




def main():
    manager = PasswordManager()
    manager.authenticate()
    while True:
        user_input = InputManager.get_user_action()
        match user_input:
            case Actions.ADD:
                d, ps = InputManager.get_user_domain_and_pswd()
                manager.save_new_password(d, ps)
            case Actions.LIST:
                pass
            case Actions.CHANGE:
                pass
            case Actions.REMOVE:
                pass
            case Actions.QUIT:
                sys.exit()


if __name__ == '__main__':
    main()
