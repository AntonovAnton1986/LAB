def get_number(num):
    while True:
        try:
            return float(input(num))
        except ValueError:
            print("Ошибка: введите корректное число.")
''' 
Получает от пользователя символ и проверяет, что он число. В противном случае вызывает ошибку и перезапускает
 
'''


def get_operator():
    valid_operators = ['+', '-', '*', '/']
    while True:
        op = input("Введите оператор (+, -, *, /): ")
        if op in valid_operators:
            return op
        else:
            print("Ошибка: допустимые операторы — +, -, *, /.")
            
''' Получает от пользователя оператор, если не из списка дает ошибку и перезапускает'''            

def calculate(a, b, operator):
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    elif operator == '/':
        if b == 0:
            print("Ошибка: деление на ноль.")
            return None
        return a / b

''' Считает числа''' 

def main():
    print("=== Калькулятор ===")
    while True:
        num1 = get_number("Введите первое число: ")
        operator = get_operator()
        num2 = get_number("Введите второе число: ")

        result = calculate(num1, num2, operator)
        if result is not None:
            print(f"Результат: {num1} {operator} {num2} = {result}")

        cont = input("Хотите продолжить? (д/н): ").strip().lower()
        if cont != 'д':
            print("Выход из калькулятора.")
            break
''' Основная функция программы'''



main()
