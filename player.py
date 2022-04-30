'''
Classe correspondente a um jogador.
'''
class Player:
    def __init__(self, name:str ,symbol:str):
        self.__name = name
        self.__symbol = symbol

    def __str__(self):
        return self.__symbol

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_value):
        self.__name = new_value

    @property
    def symbol(self):
        return self.__symbol

    @symbol.setter
    def symbol(self, new_value):
        self.__symbol = new_value