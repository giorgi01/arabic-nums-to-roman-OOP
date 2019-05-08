from random import randrange


class ArabicNum:

    def __init__(self, num):
        self.num = num

    def show_arabic(self):
        print('In arabic:', self.num)

    def to_roman(self):
        roman_num = ''
        keys = {'M': 1000, 'CM': 900, 'D': 500, 'CD': 400,
                'C': 100, 'XC': 90, 'L': 50, 'XL': 40, 'X': 10,
                'IX': 9, 'V': 5, 'IV': 4, 'I': 1}
        while self.num > 0:
            for key, value in keys.items():
                while self.num >= value:
                    roman_num += key  # +'M' თუ მეტია 1000-ზე
                    self.num -= value  # -1000 თუ მეტია 1000-ზე
        print('In roman this num will be written like that:', roman_num)


random_num = ArabicNum(randrange(444, 999, 2))
random_num.show_arabic()
random_num.to_roman()
