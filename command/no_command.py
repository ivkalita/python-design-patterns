from command.command import Command


class NoCommand(Command):
    name = ''
    description = 'No command found'

    def execute(self, **kwargs) -> None:
        print('No command found')
