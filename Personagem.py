from AbstractPersonagem import *


class Personagem(AbstractPersonagem):
    # Construtor fornecido, nao deve ser alterado
    def __init__(
            self,
            energia: int,
            habilidade: int,
            velocidade: int,
            resistencia: int,
            tipo: Tipo
    ):
        self.__energia = (None, energia)[isinstance(energia, int)]
        self.__habilidade = (None, habilidade)[isinstance(habilidade, int)]
        self.__velocidade = (None, velocidade)[isinstance(velocidade, int)]
        self.__resistencia = (None, resistencia)[isinstance(resistencia, int)]
        self.__tipo = (None, tipo)[isinstance(tipo, int)]

    @property
    def tipo(self) -> Tipo:
        return self.__tipo

    @property
    def energia(self) -> int:
        return self.__energia

    @property
    def habilidade(self) -> int:
        return self.__habilidade

    @property
    def velocidade(self) -> int:
        return self.__velocidade

    @property
    def resistencia(self) -> int:
        return self.__resistencia
