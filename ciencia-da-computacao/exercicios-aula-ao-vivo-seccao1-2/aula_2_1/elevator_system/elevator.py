from elevator_system.elevator_status import ElevatorStatus


class Elevator():
    def __init__(self):
        # codigo abaixo = <nome da instancia>.current_floor
        self.current_floor = 0
        self.door_is_open = False
        # COMPOSIÇÃO:
        self._status = ElevatorStatus.STOPPED

    def move(self, floor):
        if self.current_floor == floor:
            self._status = ElevatorStatus.STOPPED
            self.door_is_open = True
            return
        self.door_is_open = False
        if self.current_floor < floor:
            self._status = ElevatorStatus.GOING_UP
            self.current_floor = floor
        if self.current_floor > floor:
            self._status = ElevatorStatus.GOING_DOWN
            self.current_floor = floor
