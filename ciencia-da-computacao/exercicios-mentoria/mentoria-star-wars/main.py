# arquivo principal onde vamos rodar os códigos do projeto
# abaixo temos a importação da classe personagem
from jedi_sit import Jedi, Sits
from personagem import Personagem
from sabre import Sabre

personagem1 = Personagem('Genérico', 'Humano', 150)
print(f'local e espaço de memória: {personagem1}')
# retorno: <personagem.Personagem object at 0x7f19c7b07c10>
#                 |__> local                 |_> espaço de memória ocupado>

# abaixo tanta imprimir um atributo privado do objeto:
# print(personagem1.__hp)
# retorno: AttributeError: 'Personagem' object has no attribute '__hp'


# abaixo tenta imprimir um atributo pelo metodo:
print(personagem1.get_hp())
# retorno: 150 |=> agora funciona pois é meu método público contido dentro
# da classe que acessa o atributo privado "__hp"

# gera dano no personagem:
personagem1.set_hp(73)

# abaixo chamamos a propriedade hp:
# mesmo sendo um metodo eu posso usar o hp
# da mesma forma que eu uso o acesso a um stributo ou seja sem parenteses
print(personagem1.hp)
# retorno: 150 |=> agora funciona pois é meu método público contido dentro
# da classe que acessa o atributo privado "__hp"

# o metodo vars transforma os atributos e valores passados para o objeto
# em um dicionário contém chave e valores:
print(vars(personagem1))
# retorno: {'nome': 'Genérico', 'especie': 'Humano', 'hp': 150}

# parametros da instancia da classe Jedi e Sabre:
# Jedi()=> (nome, especie=String, hp=number, sabre=Obj da classe Sabre)
# Sabre()=> (cor=String, potencia=Number)
anakin_skywalker = Jedi("Anakin", "Humano", 250, Sabre("Azul", 90))
darth_vader = Sits("Darth Vader", "Ciborg", 200, Sabre("Vermelho", 100))

print("-----------------------")
print("BATALHA MORTAL")
print(f"{anakin_skywalker.nome}: {anakin_skywalker.speak()}")
print(f"{darth_vader.nome}: {darth_vader.speak()}")

while darth_vader.hp > 0:
    print(
        f"{darth_vader.nome} (HP {darth_vader.hp})" +
        f"ataca {anakin_skywalker.nome} (HP {anakin_skywalker.hp})"
    )
    print(darth_vader.atack(anakin_skywalker))
    # personagem2.falar()
    if anakin_skywalker.hp > 0:
        print(
            f"{anakin_skywalker.nome} (HP {anakin_skywalker.hp})"
            + f" contra-ataca {darth_vader.nome} (HP {darth_vader.hp})"
        )
        print(anakin_skywalker.backfire(darth_vader))
        # personagem3.falar()
    else:
        break
