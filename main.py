import sys
from cryptography.fernet import Fernet
from user_input import Actions, InputManager


from PasswordManager import PasswordManager


def main():

    manager = PasswordManager()
    if not manager.authenticate():
        print('Nie udało się uwierzytelnić, spróbuj ponownie')
    while manager.authenticated:
        user_input = InputManager.get_user_action()
        match user_input:
            case Actions.ADD:
                d, ps = InputManager.get_user_domain_and_pswd()
                manager.save_new_password(d, ps)
            case Actions.DISPLAY:
                domain = input('Domena: ')
                manager.display_password_for_domain(domain)
            case Actions.LIST:
                manager.list_domains()
            case Actions.CHANGE:
                pass
            case Actions.REMOVE:
                pass
            case Actions.QUIT:
                sys.exit()


if __name__ == '__main__':
    main()
