from collections.abc import Iterable, Iterator


class Carta:
    def __init__(self, valor, naipe):
        self.valor = valor
        self.naipe = naipe

    def __repr__(self):
        return '<%s de %s>' % (self.valor, self.naipe)


# classe iteradora, essa classe trata o meu elemento
# iteravel e retorna o objeto
class iteratorBaralho(Iterator):
    def __init__(self, cartas):
        # recebe um array de coisas
        self.__cartas = cartas
        self.__index = 0

    def __next__(self):
        try:
            # dentro do try tenta iterar sobre uma coisa
            print('try')
            carta_atual = self.__cartas[self.__index]
        # Caso chegue a um index inexistente para a operação
        except IndexError:
            raise StopIteration()
        else:
            # executa outras rotinas de codigo e retorna
            # a primeira iteração
            print(f'else {carta_atual}')
            self.__index += 1
        return carta_atual


# contém o elemento a ser iterado ou seja elemento iteravel
class Baralho(Iterable):
    naipes = 'copas ouros espadas paus'.split()
    valores = 'A 2 3 4 5 6 7 8 9 10 J Q K'.split()

    def __init__(self):
        # atributo privado que recebe uma list customizada
        # que itera sobre meus atributos naipes e valores e
        #  instancía a class Carta que por sua vez cria um 
        # objeto Carta único de acordo com os valores de naipe e valores
        self._cartas = [
            Carta(valor, naipe)
            for naipe in self.naipes
            for valor in self.valores
        ]

    def __len__(self):
        # retorna o tamanho do objeto semelhante ao .length do javascript
        return len(self._cartas)

    def __iter__(self):
        # Aqui eu retorno uma instancia ou objeto da classe
        # que iterou sobre meu elemento
        # iteravel tratado ou seja iterado
        return iteratorBaralho(self._cartas)


if __name__ == "__main__":

    teste = Baralho()
    for test in teste:
        print(test)


""" naipes = 'copas ouros espadas paus'.split()
valores = 'A 2 3 4 5 6 7 8 9 10 J Q K'.split()
cartas = [
            Carta(valor, naipe)
            for naipe in naipes
            for valor in valores
        ]

print(cartas) """
