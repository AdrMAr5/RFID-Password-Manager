from enum import Enum
from getpass import getpass


class Actions(Enum):
    ADD = 1
    LIST = 2
    CHANGE = 3
    REMOVE = 4
    QUIT = 5


class InputManager:
    def __init__(self):
        pass

    @staticmethod
    def __display_actions():
        print('Wybierz działanie:')
        print('1. Dodaj nowe hasło')
        print('2. Wylistuj domeny')
        print('3. Zmień hasło')
        print('4. Usuń rekord')
        print('5. Wyjdź')

    @staticmethod
    def get_user_action() -> Actions:
        InputManager.__display_actions()
        user_choice = input('Wybierz działanie wpisując odpowiedni numer: ')
        match user_choice:
            case '1':
                return Actions.ADD
            case '2':
                return Actions.LIST
            case '3':
                return Actions.CHANGE
            case '4':
                return Actions.REMOVE
            case '5':
                return Actions.QUIT

    @staticmethod
    def get_user_domain_and_pswd():
        domain = input('Domena: ')
        pswd = getpass('Hasło: ')
        return domain, pswd
