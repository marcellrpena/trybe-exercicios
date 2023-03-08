from navigation.navigator import Navigator
from strategy.strategy_types import WalkStrategy


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