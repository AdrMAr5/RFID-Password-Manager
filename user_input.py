from enum import Enum
import maskpass


class Actions(Enum):
    ADD = 1
    DISPLAY = 2
    LIST = 3
    CHANGE = 4
    REMOVE = 5
    QUIT = 6


class InputManager:
    def __init__(self):
        pass

    @staticmethod
    def __display_actions():
        print('Wybierz działanie:')
        print('1. Dodaj nowe hasło')
        print('2. Wyświetl hasło dla domeny')
        print('3. Wylistuj domeny')
        print('4. Zmień hasło')
        print('5. Usuń rekord')
        print('6. Wyjdź')

    @staticmethod
    def get_user_action() -> Actions:
        InputManager.__display_actions()
        user_choice = input('Wybierz działanie wpisując odpowiedni numer: ')
        match user_choice:
            case '1':
                return Actions.ADD
            case '2':
                return Actions.DISPLAY
            case '3':
                return Actions.LIST
            case '4':
                return Actions.CHANGE
            case '5':
                return Actions.REMOVE
            case '6':
                return Actions.QUIT

    @staticmethod
    def get_user_domain_and_pswd():
        domain = input('Domena: ')
        pswd = maskpass.askpass("Hasło: ")
        return domain, pswd

    @staticmethod
    def get_domain():
        domain = input('Domena: ')
        return domain
