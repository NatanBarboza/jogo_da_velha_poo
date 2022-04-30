'''
Esta é uma refatoração do código feito em programação procedural e transcrito em Orientação a Objetos.
'''
class Hash:
    def __init__(self):
        #definindo o tamanho do jogo da velha
        self.__array = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        #definindo estado de vitória do jogo
        self.__state = False

    #definindo visualização do array em jogo da velha
    @property
    def array(self):
        print(f'{self.__array[0]}', f'{self.__array[1]}', f'{self.__array[2]}', sep=(' | '))
        print('-' * 10)
        print(f'{self.__array[3]}', f'{self.__array[4]}', f'{self.__array[5]}', sep=(' | '))
        print('-' * 10)
        print(f'{self.__array[6]}', f'{self.__array[7]}', f'{self.__array[8]}', sep=(' | '))

    #definindo as possibilidades de ganho
    def win(self, player):
        if self.__array[0:3] == [player, player, player]:
            self.__state = True
            return print(f"O jogador '{player.name}' ganhou.")
             
        elif self.__array[3:6] == [player, player, player]:
            self.__state = True
            return print(f"O jogador '{player.name}' ganhou.")

        elif self.__array[6:9] == [player, player, player]:
            self.__state = True
            return print(f"O jogador '{player.name}' ganhou.")

        elif self.__array[0:7:3] == [player, player, player]:
            self.__state = True
            return print(f"O jogador '{player.name}' ganhou.")

        elif self.__array[1:8:3] == [player, player, player]:
            self.__state = True
            return print(f"O jogador '{player.name}' ganhou.")

        elif self.__array[2:9:3] == [player, player, player]:
            self.__state = True
            return print(f"O jogador '{player.name}' ganhou.")

        elif self.__array[2:7:2] == [player, player, player]:
            self.__state = True
            return print(f"O jogador '{player.name}' ganhou.")

        elif self.__array[0:9:4] == [player, player, player]:
            self.__state = True
            return print(f"O jogador '{player.name}' ganhou.")

        else:
            pass

    #definindo a vez de cada jogador
    def turn(self, symbol):
        while True:
            self.array
            value = int(input(f"Digite um valor para ser trocado por {symbol}: "))

            if(value >= 0 and value < 9):
                if (self.__array[value] == value):
                    self.__array[value] = symbol
                    break
                
                else: 
                    print("Digite um valor que não esteja sendo usado.")
                    continue

            else:
                return print("Digite um valor entre 0 e 8.")

    #definindo a lógica de rodadas e turnos
    def all_game(self, player1, player2):
        for turn in range(0, 5):
            turn += 1
            self.turn(player1)
            self.win(player1)

            #verificação de estado do jogo e verificação do término do jogo
            if(self.__state == True):
                break
            elif(turn == 5):
                print("O jogo deu velha e não houve ganhadores.")
                break
            else:
                pass

            self.turn(player2)
            self.win(player2)

            if(self.__state == True):
                break

            else:
                pass