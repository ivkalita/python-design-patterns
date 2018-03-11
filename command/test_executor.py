from unittest import mock

from command.executor import CommandExecutor


class TestExecutor:
    @mock.patch('command.commands.CPUUsageCommand.execute')
    def test_discovery(self, cpu_usage_execute: mock.MagicMock) -> None:
        executor = CommandExecutor.create_from_module('command.commands')
        executor.execute('cpu_usage')

        cpu_usage_execute.assert_called_once()

    @mock.patch('command.no_command.NoCommand.execute')
    def test_no_command_executed_if_no_command_found(self, no_command_execute: mock.MagicMock) -> None:
        executor = CommandExecutor([])

        executor.execute('cpu_usage')

        no_command_execute.assert_called_once()
