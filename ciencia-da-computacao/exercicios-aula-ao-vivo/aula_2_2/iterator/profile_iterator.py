from collections.abc import Iterable, Iterator


# HERANÇA
class ProfileIterator(Iterator):
    def __init__(self, friends):
        # ENCAPSULAMENTO
        self.__friends = friends
        # ponto de partida do meu next
        self.__index = 0

    def __next__(self):
        try:
            current_value = self.__friends[self.__index]
        except IndexError:
            raise StopIteration()
        else:
            self.__index += 1
            return current_value


# Elemento a ser Iterado aqui vou criar um elemento que
# seja iteravel e envia-lo como parâmetro para uma instancia
# ou Objeto da minha classe ITERADORA
# que fará a iteração(ITERADOR) dessa minha variável usando
# cada elemento de forma individual
class SocialNetwork(Iterable):
    def __init__(self, friends):
        self.friends = friends

    def __iter__(self):
        # COMPOSIÇÃO
        return ProfileIterator(self.friends)


if __name__ == "__main__":
    redesocial = SocialNetwork(['teste1', 'teste2', 'teste3', 'teste4', 'teste5'])
    for name in redesocial:
        print(name)
