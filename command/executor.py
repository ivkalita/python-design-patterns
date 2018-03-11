import inspect
from typing import List, Type, Dict

import sys

from command.command import Command
from command.no_command import NoCommand


class CommandExecutor:
    _commands: Dict[str, Type[Command]] = {}

    def __init__(self, commands: List[Type[Command]]) -> None:
        """ Creates an executor with registered commands. """
        self._commands = {}
        for command in commands:
            self._commands[command.name] = command

    def execute(self, *cli_args) -> None:
        """ Executes command based on cli-args. """
        name = cli_args[0] if len(cli_args) > 0 else ''
        cls = self._commands.get(name, NoCommand)
        instance = cls(*cli_args)
        instance.execute()

    @classmethod
    def create_from_module(cls, module_name: str) -> 'CommandExecutor':
        """ Creates an executor with commands, that are registered in module_name module. """
        __import__(module_name)
        commands_module = sys.modules[module_name]
        members = inspect.getmembers(commands_module, lambda x: inspect.isclass(x) and issubclass(x, Command))
        commands = list(map(lambda member: member[1], members))
        return cls(commands)
