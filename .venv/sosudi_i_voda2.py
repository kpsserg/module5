class Container:
    name = ''
    _volume: int = 0
    _current_volume: int = 0
    pour_out: int = 0

    # Метод, который выливает воду из сосуда.
    def pour_out_liquid(self):
        if self._current_volume > 0:
            self._current_volume -= self.pour_out
            return self.pour_out
        else:
            print(f'{self.name} пуст')
            return 0

    # метод, который принимает воду в сосуде
    def pour_liquid(self, volume: int) -> None:
        if self._current_volume + volume <= self._volume:
            self._current_volume += volume
        else:
            print(f'{self.name} полон')

    # Метод, который выводит инфо о сосуде
    def info(self):
        print(f'{self.name} = {self._current_volume}')


class Jug(Container):
    name = 'Jug'
    _volume: int = 1000
    _current_volume: int = 600
    pour_out: int = 100


class Glass(Container):
    name = 'Glass'
    _volume: int = 300
    _current_volume: int = 0
    pour_out: int = 50


def main() -> None:
    jug = Jug()
    glass = Glass()
    i = 0
    while i < 15:
        jug.info()
        glass.info()
        glass.pour_liquid(jug.pour_out_liquid())
        i += 1


if __name__ == '__main__':
    main()
