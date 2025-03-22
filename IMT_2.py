print('Расчет индекса массы тела')

male_group_one = [20,21,22,23,24,25] # 19-24 age
male_group_two = [21,22,23,24,25,26] # 25-24 age
male_group_three = [22,23,24,25,26,27] # 35-44 age
male_group_four = [23,24,25,26,27,28] # 45-54 age
male_group_five = [24,25,26,27,28,29] # 55-64 age
male_group_six = [25,26,27,28,28,30] # 65+ age
female_group_one = [19,20,21,22,23,24] # 19-24 age
female_group_two = [20,21,22,23,24,25] # 25-24 age
female_group_three = [21,22,23,24,25,26] # 35-44 age
female_group_four = [22,23,24,25,26,27] # 45-54 age
female_group_five = [23,24,25,26,27,28] # 55-64 age
female_group_six = [24,25,26,27,28,29] # 65+ age


while True:
    choise = input("""Выбери действие:
    1 - Рассчитать индекс
    2 - Закончить программу 
    """)

    if choise == '1':
        age = input('Введите Ваш возраст: ')
        gender = input('Введите Ваш пол м\ж: ')
        height = input('Введите Ваш рост в см: ')
        weight = input('Введите Ваш вес в кг: ')
        height_meter = int(height) / 100
        imt = int(weight) // height_meter ** 2
        print(f'Ваш индекс массы тела - {imt}\n')

        if gender == "м":
            if 19 <= int(age) <= 24:
                if imt in male_group_one:
                    print('Вес в норме')
                if imt < male_group_one[0]:
                    new_imt =  male_group_one[0] - imt
                    add_weight = new_imt * height_meter ** 2
                    print(f'Недостаточный вес, {weight} кг, до нормы необходимо добавить вес на {add_weight} кг')
                elif imt > male_group_one[5]:
                    new_imt = imt - male_group_one[5]
                    add_weight = new_imt * height_meter ** 2
                    print(f'Избыточный вес, {weight} кг, до нормы необходимо скинуть вес на {add_weight} кг')
            if 25 <= int(age) <= 34:
                if imt in male_group_two:
                    print('Вес в норме')
                if imt < male_group_two[0]:
                    new_imt = male_group_two[0] - imt
                    add_weight = new_imt * height_meter ** 2
                    print(
                        f'Недостаточный вес, {weight} кг, до нормы необходимо добавить вес на {add_weight} кг')
                elif imt > male_group_two[5]:
                    new_imt = imt - male_group_two[5]
                    add_weight = new_imt * height_meter ** 2
                    print(f'Избыточный вес, {weight} кг, до нормы необходимо скинуть вес на {add_weight} кг')
            if 35 <= int(age) <= 44:
                if imt in male_group_three:
                    print('Вес в норме')
                if imt < male_group_three[0]:
                    new_imt = male_group_three[0] - imt
                    add_weight = new_imt * height_meter ** 2
                    print(
                        f'Недостаточный вес, {weight} кг, до нормы необходимо добавить вес на {add_weight} кг')
                elif imt > male_group_three[5]:
                    new_imt = imt - male_group_three[5]
                    add_weight = new_imt * height_meter ** 2
                    print(
                        f'Избыточный вес, {weight} кг, до нормы необходимо скинуть вес на {add_weight} кг')
            if 45 <= int(age) <= 54:
                if imt in male_group_four:
                    print('Вес в норме')
                if imt < male_group_four[0]:
                    new_imt = male_group_four[0] - imt
                    add_weight = new_imt * height_meter ** 2
                    print(
                        f'Недостаточный вес, {weight} кг, до нормы необходимо добавить вес на {add_weight} кг')
                elif imt > male_group_four[5]:
                    new_imt = imt - male_group_four[5]
                    add_weight = new_imt * height_meter ** 2
                    print(
                        f'Избыточный вес, {weight} кг, до нормы необходимо скинуть вес на {add_weight} кг')
            if 55 <= int(age) <= 64:
                if imt in male_group_five:
                    print('Вес в норме')
                if imt < male_group_five[0]:
                    new_imt = male_group_five[0] - imt
                    add_weight = new_imt * height_meter ** 2
                    print(
                        f'Недостаточный вес, {weight} кг, до нормы необходимо добавить вес на {add_weight} кг')
                elif imt > male_group_five[5]:
                    new_imt = imt - male_group_five[5]
                    add_weight = new_imt * height_meter ** 2
                    print(
                        f'Избыточный вес, {weight} кг, до нормы необходимо скинуть вес на {add_weight} кг')
            if 65 <= int(age):
                if imt in male_group_six:
                    print('Вес в норме')
                if imt < male_group_six[0]:
                    new_imt = male_group_six[0] - imt
                    add_weight = new_imt * height_meter ** 2
                    print(f'Недостаточный вес, {weight} кг, до нормы необходимо добавить вес на {add_weight} кг')
                elif imt > male_group_six[5]:
                    new_imt = imt - male_group_six[5]
                    add_weight = new_imt * height_meter ** 2
                    print(f'Избыточный вес, {weight} кг, до нормы необходимо скинуть вес на {add_weight} кг')

        if gender == "ж":
            if 19 <= int(age) <= 24:
                if imt in female_group_one:
                    print('Вес в норме')
                if imt < female_group_one[0]:
                    new_imt = female_group_one[0] - imt
                    add_weight = new_imt * height_meter ** 2
                    print(f'Недостаточный вес, {weight} кг, до нормы необходимо добавить вес на {add_weight} кг')
                elif imt > female_group_one[5]:
                    new_imt = imt - female_group_one[5]
                    add_weight = new_imt * height_meter ** 2
                    print(f'Избыточный вес, {weight} кг, до нормы необходимо скинуть вес на {add_weight} кг')
            if 25 <= int(age) <= 34:
                if imt in female_group_two:
                    print('Вес в норме')
                if imt < female_group_two[0]:
                    new_imt = female_group_two[0] - imt
                    add_weight = new_imt * height_meter ** 2
                    print(f'Недостаточный вес, {weight} кг, до нормы необходимо добавить вес на {add_weight} кг')
                elif imt > female_group_two[5]:
                    new_imt = imt - female_group_two[5]
                    add_weight = new_imt * height_meter ** 2
                    print(f'Избыточный вес, {weight} кг, до нормы необходимо скинуть вес на {add_weight} кг')
            if 35 <= int(age) <= 44:
                if imt in female_group_three:
                    print('Вес в норме')
                if imt < female_group_three[0]:
                    new_imt = female_group_three[0] - imt
                    add_weight = new_imt * height_meter ** 2
                    print(f'Недостаточный вес, {weight} кг, до нормы необходимо добавить вес на {add_weight} кг')
                elif imt > female_group_three[5]:
                    new_imt = imt - female_group_three[5]
                    add_weight = new_imt * height_meter ** 2
                    print(f'Избыточный вес, {weight} кг, до нормы необходимо скинуть вес на {add_weight} кг')
            if 45 <= int(age) <= 54:
                if imt in female_group_four:
                    print('Вес в норме')
                if imt < female_group_four[0]:
                    new_imt = female_group_four[0] - imt
                    add_weight = new_imt * height_meter ** 2
                    print(f'Недостаточный вес, {weight} кг, до нормы необходимо добавить вес на {add_weight} кг')
                elif imt > female_group_four[5]:
                    new_imt = imt - female_group_four[5]
                    add_weight = new_imt * height_meter ** 2
                    print(f'Избыточный вес, {weight} кг, до нормы необходимо скинуть вес на {add_weight} кг')
            if 55 <= int(age) <= 64:
                if imt in female_group_five:
                    print('Вес в норме')
                if imt < female_group_five[0]:
                    new_imt = female_group_five[0] - imt
                    add_weight = new_imt * height_meter ** 2
                    print(f'Недостаточный вес, {weight} кг, до нормы необходимо добавить вес на {add_weight} кг')
                elif imt > female_group_five[5]:
                    new_imt = imt - female_group_five[5]
                    add_weight = new_imt * height_meter ** 2
                    print(f'Избыточный вес, {weight} кг, до нормы необходимо скинуть вес на {add_weight} кг')
            if 65 <= int(age):
                if imt in female_group_six:
                    print('Вес в норме')
                if imt < female_group_six[0]:
                    new_imt = female_group_six[0] - imt
                    add_weight = new_imt * height_meter ** 2
                    print(f'Недостаточный вес, {weight} кг, до нормы необходимо добавить вес на {add_weight} кг')
                elif imt > female_group_six[5]:
                    new_imt = imt - female_group_six[5]
                    add_weight = new_imt * height_meter ** 2
                    print(f'Избыточный вес, {weight} кг, до нормы необходимо скинуть вес на {add_weight} кг')


    elif choise == '2':
        break
    else:
        print('Ввели неправльное значение')
        continue