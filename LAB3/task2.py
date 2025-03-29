# TODO Напишите функцию find_common_participants
def find_common_participants(group1, group2, a = ','):
    first = group1.split(a)
    second = group2.split(a)
    set_1 = set(first)
    set_2 = set(second)
    new_group = set_1.intersection(set_2)
    return sorted(new_group)


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Проверьте работу функции с разделителем отличным от запятой
print(find_common_participants(participants_first_group, participants_second_group, a = '|'))