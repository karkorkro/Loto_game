import random


class IncorrectInput(ValueError):
    def __str__(self):
        return 'Некорректный ввод. Введите "y" или "n"'


class Card:

    def __init__(self):
        self.nums = random.sample(range(1, 91), 15)
        self.crossed_nums = 0
        self.lost = False

        card = []
        for i in range(3):
            nums = sorted(self.nums[5 * i: 5 * (i + 1)])
            for j in range(4):
                index = random.randint(0, len(nums))
                nums.insert(index, 0)
            card += nums
        self.card = card
        result = ''
        for num_index, num in enumerate(self.card):
            if num == 0:
                result += '  '
            elif num < 0:
                result += ' -'
            elif 0 < num < 10:
                result += f' {num}'
            else:
                result += str(num)

            if (num_index + 1) % 9 == 0:
                result += '\n'
            else:
                result += ' '
        self.appearance = f'{"-" * 26}\n{result}{"-" * 26}'

    def update_appearance(self):
        result = ''
        for num_index, num in enumerate(self.card):
            if num == 0:
                result += '  '
            elif num < 0:
                result += ' -'
            elif 0 < num < 10:
                result += f' {num}'
            else:
                result += str(num)

            if (num_index + 1) % 9 == 0:
                result += '\n'
            else:
                result += ' '
        self.appearance = f'{"-" * 26}\n{result}{"-" * 26}'

    def cross(self, number):
        x = self.card.index(number)
        self.card[x] = -1
        self.update_appearance()
        self.crossed_nums += 1

    def strike(self, number):
        command = input('Хотите зачеркнуть номер на своей карточке? (y/n)  ')
        while command != 'y' and command != 'n':
            command = input('Вы ввели неверную команду, введите "y" или "n"')
        if command == 'y':
            if number in self.card:
                self.cross(number)
            else:
                print('You entered incorrect number. Game over. ')
                self.lost = True
        elif command == 'n':
            if number in self.card:
                print('you missed your number')
                self.lost = True
            else:
                pass


class ComputerCard(Card):

    def strike(self, number):
        if number in self.card:
            self.cross(number)
        else:
            pass


if __name__ == '__main__':
    new_card = Card()
    comp_card = ComputerCard()
    print(new_card.appearance)
    print(comp_card.appearance)
    new_card.strike(50)
    comp_card.strike(50)
    print(new_card.appearance)
    print(comp_card.appearance)
