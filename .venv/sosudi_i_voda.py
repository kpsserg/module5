class Container:
    def __init__(self, name: str, volume: int, current_volume: int, pour_out: int = 100) -> None:
        self.__name = name
        self.__volume = volume
        self.current_volume = current_volume
        self.pour_out = pour_out

    # Метод, который выливает воду из сосуда.
    def pour_out_liquid(self):
        if self.current_volume >0:
            self.current_volume -= self.pour_out
            return  self.pour_out
        else:
            print(f'{self.__name} пуст')
            return 0

    # метод, который принимает воду в сосуде
    def pour_liquid(self, volume: int) -> None:
        if self.current_volume + volume <= self.__volume:
            self.current_volume += volume
        else:
            print(f'{self.__name} полон')

    # Метод, который выводит инфо о сосуде
    def info(self):
        print(f'{self.__name} = {self.current_volume}')

def main() -> None:
    jug = Container(name = 'jug', volume = 1000, current_volume=1000)
    glass = Container(name = 'glass', volume=200, current_volume = 0, pour_out = 50)
    i = 0
    while i<15:
        jug.info()
        glass.info()
        glass.pour_liquid(jug.pour_out_liquid())
        i +=1

if __name__ == '__main__':
    main()
