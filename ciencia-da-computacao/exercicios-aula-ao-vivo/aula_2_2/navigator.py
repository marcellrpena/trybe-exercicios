from abc import ABC, abstractmethod


class Navigator:
    def __init__(self, navigation_strategy):
        # atributo privado somente Navigator pode acessa-lo
        # ele recebe o objeto criado a partir de uma classe
        self.__navigation_strategy = navigation_strategy

    def build_route(self, departure, arrival):
        self.__navigation_strategy.build_route(departure, arrival)
        # self:
        # nome do objeto gerado a partir da Classe Navigator

        # __navigation_strategy:
        # é a instancia ou objeto de Classe enviada como
        # parâmetro para Navigator

        # build_route:
        # é o método do objeto contido em
        # __navigation_strategy ou seja são as caracteristicas
        # da construção desse metodo na classe enviada por
        # parâmetro para navigator
        # basicamente o que estou fazendo é usando isso:
        # Navigator(WalkStrategy).build_route("Centro", "Pampulha")
        # no lugar disso:
        # WalkStrategy.build_route("Centro", "Pampulha")


class NavigationStrategy(ABC):
    @classmethod
    @abstractmethod
    def build_route(self):
        raise NotImplementedError
