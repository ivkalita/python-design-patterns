from factory.cars.car import Car


class NullCar(Car):
    def start(self) -> None:
        print('Null car can\'t be started.')

    def stop(self) -> None:
        print('Null car can\'t be stopped.')
