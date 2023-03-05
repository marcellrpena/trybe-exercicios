from abc import ABC, abstractmethod


# --------------ABSTRAÇÃO------------------
# CLASSES ABSTRATAS NÃO PODEM GERAR INSTANCIAS OU OBJETOS DE SÍ
# classe abstrata: python não tem classes abstratas nativas
# para isso faz-se o uso da biblioteca ABC
# a classe com metodos abstratos obriga suas filhas a herdarem
# esse metodo ou seja se caso eu herdar a classe definida abaixo
# eu devo obrigatoriamente usar todos os metodos abstratos que ela
# compõe caso contrário meu código quebra
class PersonagemInterface(ABC):
    # meus herdeiros obrigatoriamente devem usar essa classe
    @abstractmethod
    def speak():
        # levanta um erro quando é chamado direto da classe abstrata
        raise NotImplementedError()
        # passa pela função e a executa ainda que não faça nada
        # pass ou ...
