# TODO решите задачу
import json

def task(filename='input.json'):
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)

        total = sum([item["score"] * item["weight"] for item in data])

    result = round(total, 3)
    return result


# Вызов функции
task()


print(task())
