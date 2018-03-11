from factory.cars.car import Car


class Jeep(Car):
    def stop(self) -> None:
        print('Jeep stopped.')

    def start(self) -> None:
        print('Jeep is running.')
