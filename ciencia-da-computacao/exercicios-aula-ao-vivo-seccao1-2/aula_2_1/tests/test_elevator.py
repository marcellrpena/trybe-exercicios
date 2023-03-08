# começando por TDD => os testes direcionam:
from elevator_system.elevator_status import ElevatorStatus
from elevator_system.elevator import Elevator


def test_create_elevator():
    # cria meu objeto(instancia) da classe Elevator
    elevator = Elevator()
    # testa se o atributo current_floor do objeto elevator começa = a 0
    assert elevator.current_floor == 0
    # testa se o atributo door_is_open do meu objeto elevator começa = true
    assert elevator.door_is_open is False
    # status é uma variável
    assert elevator._status == ElevatorStatus.STOPPED


def test_move_up():
    # preparo de teste
    elevator = Elevator()
    destination_floor = 5
    elevator.move(destination_floor)

    # teste de resultados
    assert elevator.door_is_open is False
    assert elevator.current_floor == 5
    assert elevator._status == ElevatorStatus.GOING_UP


def test_move_down():
    # preparo de teste
    elevator = Elevator()
    elevator.current_floor = 5
    destination_floor = 1
    elevator.move(destination_floor)

    # teste de resultados
    assert elevator.door_is_open is False
    assert elevator.current_floor == 1
    assert elevator._status == ElevatorStatus.GOING_DOWN


def test_move_same_floor():
    # preparo de teste
    elevator = Elevator()
    elevator.current_floor = 5
    destination_floor = 5
    elevator.move(destination_floor)

    # teste de resultados
    assert elevator.door_is_open is True
    assert elevator.current_floor == destination_floor
    assert elevator._status == ElevatorStatus.STOPPED
