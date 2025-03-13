list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# TODO Разделите участников на две команды
a = len(list_players)
divide = a // 2
first_team = list_players[:divide]
second_team = list_players[divide:]
print(str(first_team))
print(str(second_team))