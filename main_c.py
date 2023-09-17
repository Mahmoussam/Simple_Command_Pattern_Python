import time
from abc import ABC, abstractmethod


class Command(ABC):
    """
    The Command interface declares a method for executing a command.
    """

    @abstractmethod
    def execute(self) -> None:
        pass
class Light:
    def __init__(self):
        self.__state=False
    def turn_on(self):
        self.__state=True
    def turn_off(self):
        self.__state=False
    def print_state(self):
        if self.__state:
            print('Light is ON!')
        else:
            print('Light is OFF!')

class turnOnCommand(Command):

    def __init__(self, light: Light) -> None:
        self.__light = light

    def execute(self) -> None:
        self.__light.turn_on()
class turnOffCommand(Command):

    def __init__(self, light: Light) -> None:
        self.__light = light

    def execute(self) -> None:
        self.__light.turn_off()
class printStateCommand(Command):

    def __init__(self, light: Light) -> None:
        self.__light = light

    def execute(self) -> None:
        self.__light.print_state()

class Remote:
    __turn_on_command = None
    __turn_off_command = None
    __print_state_command = None
    

    def set_turn_on(self, command: Command):
        self.__turn_on_command = command

    def set_turn_off(self, command: Command):
        self.__turn_off_command = command
    def set_print_state(self, command: Command):
        self.__print_state_command = command
    def auto_light(self):
        print('Starting lighting system..')
        time.sleep(1)
        print('Turning lights on for 5 seconds')
        self.__turn_on_command.execute()
        self.__print_state_command.execute()
        time.sleep(5)
        print('turning off')
        self.__turn_off_command.execute()
        self.__print_state_command.execute()

if __name__ == "__main__":
    remote=Remote()
    light=Light()
    remote.set_turn_on(turnOnCommand(light))
    remote.set_turn_off(turnOffCommand(light))
    remote.set_print_state(printStateCommand(light))
    #remote is ready to start!    
    remote.auto_light()
