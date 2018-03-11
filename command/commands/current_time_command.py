from datetime import datetime

from command.command import Command


class CurrentTimeCommand(Command):
    name = 'time'
    description = 'Displays current local time'

    def execute(self, **kwargs) -> None:
        print(datetime.now())
