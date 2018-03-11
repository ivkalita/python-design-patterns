import psutil

from command.command import Command


class CPUUsageCommand(Command):
    name = 'cpu_usage'
    description = 'Shows current CPU usage'

    def execute(self, **kwargs) -> None:
        print(psutil.cpu_times_percent(interval=1, percpu=True))
