salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен
money_capital = 0
for mes in range(0,months):
    money_capital = money_capital + salary - spend
    spend = spend + spend * increase
money_capital = round(money_capital / (-1) ,2)
print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", money_capital)