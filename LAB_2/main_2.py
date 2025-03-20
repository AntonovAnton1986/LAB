salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов


total_spend = 0
for _ in range(months):
    total_spend += spend
    spend = spend * (increase + 1)
total_salary = salary * months
money_capital = round(total_spend - total_salary, 2)

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", money_capital)
