from abc_usage.runnable import Runnable


class GoodClass(Runnable):
    def __init__(self) -> None:
        self.__is_running = False

    @property
    def is_running(self) -> bool:
        return self.__is_running

    def run(self) -> None:
        if self.is_running:
            print('Already running')
        else:
            self.__is_running = True

    def stop(self) -> None:
        if not self.is_running:
            print('Already stopped')
        else:
            self.__is_running = False
