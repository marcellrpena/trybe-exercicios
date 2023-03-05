# Molde => um personagem pode ser de varios tipos
# e esses pesonagens compartilham caracteristicas
# semelhantes como exemplo:
# possuem braço , perna , mãos mas tem cores e nomes
# diferentes

from interface import PersonagemInterface


# abaixo estou herdando os atributos e metodos da classe
# PersonagemInterface que é a superclasse, agora minha classe
# Personagem passa a ser uma SUBCLASSE da minha SUPERCLASSE PersonagemInterface
class Personagem(PersonagemInterface):
    # Metodo __init__ é um construtor usado apenas em classes
    # que criam objetos(instancias de classe)
    # self => referencia ao objeto criado a partir da classe
    # lida com os elementos de cada objeto em especifico
    # cls => referencia a classe lida com a classe e todos os
    # objetos criados a partir dessa classe

    # abaixo temos um método de instancia ou objeto, manipula
    # informações apenas do meu objeto criado vem acompanhado
    # do self
    # O SELF GUARDA O LUGAR DA INSTANCIA CRIADA, OU SEJA SELF
    # ASSUME O NOME DO OBJETO CRIADO
    def __init__(self, nome, especie, hp):
        self.nome = nome  # self.nome =  personagem1.nome
        self.especie = especie
        # __ =  dunder =  atributo ou método privado ou seja
        # só pode ser usado na classe ou objeto próprio
        # ------ENCAPSULAMENTO------
        # encapsulamento é a segmentação de atributos e metodos
        # definindo onde cada um vai atuar, se em um contexto geral ou
        # apenas dentro do contexto da classe
        self.__hp = hp

    # decorador property: é como criar uma propriedade/atributo novo
    @property
    def hp(self):
        return self.__hp

    def get_hp(self):
        return self.__hp  # self.__hp = personagem1.__hp

    # metodo de instancia: quero alterar o hp apenas do objeto criado
    def set_hp(self, dano):
        # self.__hp = personagem1.__hp -= dano(parametro externo)
        self.__hp -= dano

    def speak(self):
        return "é uma armadilha"

    # abaixo temos um método de classe, ou seja manipula a classe
    # portanto todos os objetos gerados a partir dessa classe sofrem
    # alteração de algo atraves desse método, vem acompanhado de cls
    # O CLS GUARDA O LUGAR DA CLASSE OU SEJA, CLS ASSUME O NOME DA CLASSE
    # ENTÃO SE A CLASSE É INSTANCIADA E EU USO ESSE MÉTODO OS PARAMETROS 
    # PASSADOS VÃO ALTERAR TODAS AS INSTANCIAS JÁ CRIADAS DA CLASSE
    @classmethod
    def class_method(cls):
        pass  # cls.nome = Personagem.nome

    # abaixo temos um método estático, ou seja não altera nada ele só
    # é executado, tal qual uma função, não altera atributos mas pode
    # ler atributos de uma instancia ou objetos e usa-los em uma lógica
    # dentro dele
    @staticmethod
    def static_method():
        pass
