import random


class Card:
    def __init__(self, rank: str, suit: str) -> None:
        self.rank = rank
        self.suit = suit

    # Метод определяет и возвращает вес карты
    def get_value(self) -> int:
        if self.rank in 'ТВДК':
            return 10
        else:
            return ' A23456789'.index(self.rank)  # возвращается индекс последовательности ' A23456789'

    # Метод выводит информацио о карте
    def get_rank(self) -> str:
        return f'{self.suit}{self.rank}'


class DeskCard:
    def __init__(self) -> None:
        _rank = 'A23456789ТВДК'
        _suit = 'ПБЧК'
        self.__cards = [Card(r, s) for s in _suit for r in _rank]
        random.shuffle(self.__cards)

    # выдача карты
    def get_card(self) -> Card:
        return self.__cards.pop()


# Теперь нам нужен игрок. У него есть рука с картами, есть очки по картам. + имя игрока
class Player:
    def __init__(self, name) -> None:
        self._hand = []
        self.count = 0
        self.name = name

    @property
    def hand(self) -> str:
        return f'Карты в руке: {self._hand}; Очков - {self.count}'

    @hand.setter
    def hand(self, card: Card) -> None:
        self.count += card.get_value()
        self._hand.append(card.get_rank())


# Клас для игрока-компьютера
class Dealer(Player):

    # метод который берет карту для игрока-компьютера.
    # Мы даем ему всю колоду, из которой он берет себе карту
    # def get_card(self, cards: DeskCard):
    #     while self.count < 18:
    #         self.hand = cards.get_card()
    def get_card(self, cards: DeskCard):
        while self.count < 21:
            self.hand = cards.get_card()


class Game:
    # создадим колоду и игрока
    def __init__(self, player_name: str) -> None:
        self.cards = DeskCard()
        self.player = Player(name=player_name)
        self.dealer = Dealer(name='Dealer')

    def print(self) -> str:
        return f'\n{self.player.name}:\n{self.player.hand}\n{self.dealer.name}:\n{self.dealer.hand}'

    def check_count(self):
        if self.player.count > 21:
            print(f'Вы проиграли', self.print())
        elif self.dealer.count>21 and self.player.count <= 21:
            print(f'Вы победили!!!', self.print())
        elif self.dealer.count == self.player.count:
            print(f'Ничья', self.print())
        elif self.dealer.count > self.player.count:
            print(f'Вы проиграли :(', self.print())
        elif self.dealer.count < self.player.count:
            print(f'Вы победили :) !', self.print())

    # Опишем сам процесс игры
    def start(self) -> None:
        #  Выдадим 2 карты игроку
        self.player.hand = self.cards.get_card()
        self.player.hand = self.cards.get_card()
        #  Выдадим 2 карты игроку-компьютеру (Дилеру)
        self.dealer.hand = self.cards.get_card()
        self.dealer.hand = self.cards.get_card()

        # отобразим выданные карты и набранные очки
        print(self.player.hand)

        # Предложение взять карту, если у игрока меньше 21 очка
        while self.player.count < 21:
            answer = input('Берем карту? y/n')
            if answer == 'y':
                self.player.hand = self.cards.get_card()
                print(self.player.hand)
            elif answer == 'n':
                self.dealer.get_card(self.cards)
                break
        self.check_count()


def main() -> None:
    name = input("Ваше имя ")
    game = Game(name)
    game.start()


if __name__ == '__main__':
    main()
