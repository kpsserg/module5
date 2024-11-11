from functools import total_ordering, reduce


@total_ordering
class RomanNumeral:
    _roman = ({'M': 1000, 'D': 500, 'C': 100}, {'C': 100, 'L': 50, 'X': 10}, {'X': 10, 'V': 5, 'I': 1})

    def __init__(self, number: str) -> None:
        self._number = number
        self._arabic = self.__int__()

    def __str__(self) -> str:
        return self._number

    def __int__(self) -> int:
        current_value = 0
        prev_value = 0
        arabic_value = 0
        roman_dict = self.__class__._roman
        for char in reversed(self._number):
            current_value = reduce(lambda a, b: a | b, roman_dict)[char]
            if current_value < prev_value:
                arabic_value -= current_value
            else:
                arabic_value += current_value
            prev_value = current_value
        return arabic_value

    def __eq__(self, other) -> bool:
        if isinstance(other, RomanNumeral):
            return self._arabic == other._arabic
        return NotImplemented

    def __lt__(self, other) -> bool:
        if isinstance(other, RomanNumeral):
            return self._arabic < other._arabic
        return NotImplemented

    def __add__(self, other):
        if isinstance(other, RomanNumeral):
            return RomanNumeral(self.to_arabic(self._arabic + other._arabic))
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, RomanNumeral):
            return RomanNumeral(self.to_arabic(self._arabic - other._arabic))
        return NotImplemented

    def to_arabic(self, number: int) -> str:
        num = number
        romain = ''
        for dct in self.__class__._roman:
            items = list(map(lambda it: it[::-1], dct.items()))
            for key, value in items[:2]:
                multiplier = num // key
                difference = key * multiplier
                last_num = items[2]
                if multiplier > 0:
                    romain += value * multiplier
                    num -= difference
                if num - (key - last_num[0]) >= 0:
                    romain += last_num[1] + value
                    num -= key - last_num[0]
            else:
                multiplier = num // last_num[0]
                difference = last_num[0] * multiplier
                if multiplier > 0:
                    romain += last_num[1] * multiplier
                    num -= difference

        return romain

romans1 = ['I', 'X', 'L', 'IV', 'IX', 'XLV', 'CXXIV', 'MCMXCIV']
romans2 = ['I', 'VI', 'L', 'VI', 'XI', 'XXV', 'CDXLVIII', 'MCMXCI']

for x, y in zip(romans1, romans2):
    number = RomanNumeral(x) + RomanNumeral(y)
    print(number, int(number))
