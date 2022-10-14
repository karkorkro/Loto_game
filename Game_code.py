from Class_description_for_cards import *


# создание списков, с которыми будем дальше работать:


players_number = int(input('Выберите количество игроков людей: '))
comp_players_number = int(input('Введите количество игроков компьютеров: '))
human_players = Card.create_class_item(players_number, 'human_player')
comp_players = ComputerCard.create_class_item(comp_players_number, 'computer_player')
total_players = human_players + comp_players

# печать карт игроков:
for i in total_players:
    print(i, i.appearance, sep='\n')
# создает 90 чисел(бочонков), кладет их в список в рандомном порядке
# каждое использованное число убирается из списка:
kegs_list = random.sample(range(1, 91), 90)
while max(total_players) != 15:
    keg = kegs_list.pop(random.randint(0, len(kegs_list)-1))
    print(f'Выпал бочонок с номером {keg}')
# вычеркивает из карты номер на бочонке, если он есть в карте
# в картах пользователей метод класса сам уточняет, надо ли зачеркивать номер
# в картах компьютера все вычеркивается автоматически:
    for i in total_players:
        i.strike(keg)
        if i.lost:
            total_players.remove(i)
    if len(total_players) == 1:
        print(f'{total_players[0]} wins')
        break
# заново создает список количеств вычеркнутых значений в картах
# если в какой-то из карт он достигает 15, обьявляется победитель, игра заканчивается

    for i in total_players:
        if i == 15:
            print(f'Game over. {i} wins')
            break
        print(i, i.appearance, sep='\n')
