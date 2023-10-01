from AbstractCarta import *
from Personagem import *


class Carta(AbstractCarta):

    def __init__(self, personagem: Personagem):
        self.__personagem = (None, personagem)[
            isinstance(personagem, Personagem)]

    '''
    Soma e retorna todos os valores dos atributos do personagem da Carta
    @return Retorna o somatorio de todos os atributos do personagem da Carta
    '''

    def valor_total_carta(self) -> int:
        if (
            isinstance(self.personagem.energia, int),
            isinstance(self.personagem.habilidade, int),
            isinstance(self.personagem.resistencia, int),
            isinstance(self.personagem.velocidade, int),
        ):
            return sum([
                self.personagem.energia,
                self.personagem.habilidade,
                self.personagem.resistencia,
                self.personagem.velocidade
            ])

    @property
    def personagem(self) -> Personagem:
        return self.__personagem
