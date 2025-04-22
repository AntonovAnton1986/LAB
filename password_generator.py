import random
import string

def generate_password(length: int, special_chars: str = "") -> str:
    """
    Генерирует случайный пароль заданной длины.

    :param length: Длина пароля (целое число больше 5)
    :param special_chars: Строка со специальными символами, которые можно использовать
    :return: Сгенерированный пароль
    """
    chars = string.ascii_letters + string.digits + special_chars
    password = ''.join(random.choice(chars) for _ in range(length))
    return password

def validate_password_length(user_input: str) -> int:
    """
    Проверяет, что введённая пользователем длина пароля — корректное целое число > 5.

    :param user_input: Ввод пользователя в виде строки
    :return: Корректное целое число — длина пароля
    :raises ValueError: Если значение некорректно
    """
    if not user_input.isdigit():
        raise ValueError("Длина пароля должна быть целым числом.")
    length = int(user_input)
    if length <= 5:
        raise ValueError("Длина пароля должна быть больше 5.")
    return length

def save_password_to_file(password: str, filename: str) -> None:
    """
    Сохраняет пароль в указанный файл.

    :pram password: Строка пароля
    :param filename: Название файла для записи
    """
    with open(filename, 'w') as file:
        file.write(password)
    print(f"Пароль сохранён в файл: {filename}")

def main() -> None:
    """
    Главная функция программы. Выполняет взаимодействие с пользователем и управляет процессом генерации пароля.
    """
    print("Добро пожаловать в генератор случайных паролей!")

    # Запрос длины пароля с валидацией
    while True:
        length_input = input("Введите длину желаемого пароля (целое число > 5): ")
        try:
            password_length = validate_password_length(length_input)
            break
        except ValueError as e:
            print(f"Ошибка: {e}. Пожалуйста, попробуйте снова.")

    # Запрос спецсимволов
    special_chars = input("Введите специальные символы, которые можно использовать (!@#$% и т.п.): ")

    # Генерация пароля
    password = generate_password(password_length, special_chars)

    # Запрос имени файла
    filename = input("Введите название файла для сохранения пароля (или оставьте пустым для вывода в консоль): ").strip()

    if filename:
        save_password_to_file(password, filename)
    else:
        print(f"Сгенерированный пароль: {password}")

if __name__ == "__main__":
    main()

