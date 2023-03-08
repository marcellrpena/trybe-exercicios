from enum import Enum


# a Classe abaixo HERDA da classe Enum o
# status de enumerador(semelhante a typescript)
class ElevatorStatus(Enum):
    STOPPED = 0
    GOING_UP = 1
    GOING_DOWN = 2
    LOCKED = 3
