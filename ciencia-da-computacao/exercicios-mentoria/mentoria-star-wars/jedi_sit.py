from personagem import Personagem
from sabre import Sabre
# metodo abaixo gera aleatoriedade a partir de uma lista
from random import choice


""" OBS: se a classe possui pelo menos um método abstrato essa classe não pode
         ser mais instanciada, ou seja não será possível gerar novos objetos
         a partir dessa classe """


""" -------HERANÇA------ PILAR DE P.O.O
  - Classe pai ou SuperClasse: Personagem
  - Classe filha ou SubClasse: Sits |=> HERDA ATRIBUTOS E MÉTODOS DE PERSONAGEM
  - Classe neta de PersonagemInterface: |=> aqui não há obrigatoriedade no uso
    de metodos abstratos da SUPERCLASSE PersonagemInterface pois não é uma
    herança de primeiro grau """


class Sits(Personagem):
    # Sits contém um construtor porque eu quero criar objetos
    # a partir dessa Classe
    def __init__(self, nome, especie, hp, sabre):
        # o construtor da minha classe pai é chamada atraves do metodo super()
        # super().__init__ = Personagem.__init__
        super().__init__(nome, especie, hp)
        # nesse caso estou setando o atributo sabre de forma estática
        # ou seja o valor não será passo como parametro
        # -------COMPOSIÇÃO----- PILAR DE P.O.O
        # estou compondo a minha classe com uma instância de outra classe
        # recebo essa instancia por parametro ou staticamente como padrão:
        self.sabre = sabre
        # self.sabre = Sabre('Vermelho', 90)  # self.sabre = personagem1.sabre
        # sabre contém um Objeto criado a partir da Classe Sabre
        # retorno: <self.sabre.Sabre object at 0x7f19c7b07c10>
        #                  |__> local          |_> espaço de memória ocupado>

    """ ---------POLIMORFISMO---------
     As classes Mãe e Filha possuem metodos com nomes iguais porém com
    conteúdos diferentes, ou seja a classe filha 'jedi_sit' possui o mesmo
    metodo que a classe mãe 'Personagem' e eu posso personalizar esse metodo
    para o uso na classe filha sem influência da classe mãe
     """
    def speak(self):
        # self.hp = metodo do tipo propriedade publica da classe mãe personagem
        # self.__hp = atributo privado da classe mãe, não pode ser acessado por
        # suas sub-classes herdeiras
        if self.hp <= 0:
            return f"{self.nome}: i will back"
        return f"{self.nome} say: i'm not go dead"

    """" QUERO ATACAR OUTRO PERSONAGEM, PARA ISSO QUERO MANIPULAR O HP DESSE
      OUTRO PERSONAGEM, PARA ISSO PASSO O PERSONAGEM ALVO COMO PARAMETRO
      MANIPULANDO ASSIM O HP DELE ATRAVES DO METODO set_hp HERDADO DA CLASSE
      Personagem: """
    def atack(self, personagem):
        """ set_hp recebe o parâmetro DANO e o valor desse dano vem do seu
      sabre, portanto self.sabre.potencia codigo abaixo é igual a:
    personagem.set_hp(<nome do obj instanciado da classe Sits>.sabre.potencia)
         """
        # o Personagem alvo tem um metodo defense que retorna true ou false
        # se o valor for true ele não recebe o dano
        if not personagem.defense():
            personagem.set_hp(self.sabre.potencia)
            return personagem.speak()
        return f"{personagem.nome} defendeu o ataque \n {personagem.speak()}"


class Jedi(Personagem):
    # o atributo sabre é do tipo objeto de classe ou seja, a classe Jedi
    # recebe como parâmetro uma instancia ou objeto da classe Sabre
    # e essa instancia gerada terá seus próprios atributos, ou seja
    # o objeto gerado para a classe jedi será diferente do objeto gerado
    # para a classe sit.
    # nome, especie = string,  hp = number, sabre = instancia de classe
    def __init__(self, nome, especie, hp, sabre):
        super().__init__(nome, especie, hp)  # herda de Personagem
        # sabre = Sabre(cor=string, potencia=number)
        self.sabre = Sabre('Azul', 40)

    def speak(self):
        if self.hp <= 0:
            return f"{self.nome} say: now i'm go to my antecessors"
        return f"{self.nome} say: the light be with me i'm not dead"

    def defense(self):
        # retorna aleatoriamente ou True ou False
        return choice([False, True])

    # contra ataque
    def backfire(self, personagem):
        personagem.set_hp(self.sabre.potencia)
        return personagem.speak()
