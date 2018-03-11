from factory.cars.car import Car


class Van(Car):
    def stop(self) -> None:
        print('Van is stopped.')

    def start(self) -> None:
        print('Van is started.')
