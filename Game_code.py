from Class_description_for_cards import *

# создает список кортежей по числу игроков,
# где первый элемент - имя игрока, а второй - обьект класса карта:


def create_class_item(quantity, class_name_str, item_name):
    players = []
    for i in range(quantity):
        exec(f'a{i} = {class_name_str}')
        exec(f'players.append(a{i})')
    players = [(f'{item_name}{players.index(i) + 1}', i) for i in players]
    return players

# создание списков, с которыми будем дальше работать:


players_number = int(input('Выберите количество игроков людей: '))
comp_players_number = int(input('Введите количество игроков компьютеров: '))
human_players = create_class_item(players_number, 'Card()', 'player')
comp_players = create_class_item(comp_players_number, 'ComputerCard()', 'computer_player')
total_players = human_players + comp_players
cross_number_count_list = [i[1].crossed_nums for i in total_players]
# печать карт игроков:
for i in total_players:
    print(i[1].appearance)
# создает 90 чисел(бочонков), кладет их в список в рандомном порядке
# каждое использованное число убирается из списка:
kegs_list = random.sample(range(1, 91), 90)
while max(cross_number_count_list) != 15:
    keg = kegs_list[0]
    kegs_list.remove(keg)
    print(f'Выпал бочонок с номером {keg}')
# вычеркивает из карты номер на бочонке, если он есть в карте
# в картах пользователей метод класса сам уточняет, надо ли зачеркивать номер
# в картах компьютера все вычеркивается автоматически:
    for i in total_players:
        i[1].strike(keg)
        if i[1].lost:
            total_players.remove(i)
    if len(total_players) == 1:
        print(f'{total_players[0][0]} wins')
        break
# заново создает список количеств вычеркнутых значений в картах
# если в какой-то из карт он достигает 15, обьявляется победитель, игра заканчивается
    cross_number_count_list = []
    for i in total_players:
        cross_number_count_list.append(i[1].crossed_nums)
        if i[1].crossed_nums == 15:
            print(f'Game over. {i[0]} wins')
            break
        print(i[1].appearance)
