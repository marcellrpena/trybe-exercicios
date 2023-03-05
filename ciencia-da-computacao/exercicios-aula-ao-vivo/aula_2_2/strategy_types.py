from aula_2_2.navigator import NavigationStrategy, Navigator

# herda de NavigationStrategy o metodo construtor build
class WalkStrategy(NavigationStrategy):
    #--------STRATEGY------------
    # cls => busca a classe de destino em NavigatorStrategy
    @classmethod
    def build_route(cls, departure, arrrival):
        print(f"Rota a pé saindo de {departure} para {arrrival}")


class BikeStrategy():
    def build_route(cls, departure, arrrival):
        print(f"Rota de bicicleta saindo de {departure} para {arrrival}")


class BusStrategy():
    def build_route(cls, departure, arrrival):
        print(f"Rota de onibus saindo de {departure} para {arrrival}")


class CarStrategy():
    def build_route(cls, departure, arrrival):
        print(f"Rota de carro saindo de {departure} para {arrrival}")


rota1 = Navigator(WalkStrategy)
rota1.build_route("centro", "Morada do Sol")
# O que acontece aqui?
# 1º Navigator recebe a classe WalkStrategy como parametro

# 2º rota1 recebe como atributo uma instancia de Navigator

# 3º o método build_route de Navigator é ativado recebendo 
# dois parâmetros

# 4º o método build_route de Navigator repassa os parâmetros
# dela para o build_route de WalkStrategy, 
# a linha 11 do arquivo navigator lê-se da seguinte forma:

# rota1.WalkStrategy.build_route("centro", "Morada do Sol").

# 5º a classe abstrata NavigatorStrategy faz a ponte entre
# Navigator e WalkStrategy essa ponte é permitida porque
# WalkStrategy é herdeira de NavigatorStrategy que por sua vez
# tem o mesmo metodo que Navigator