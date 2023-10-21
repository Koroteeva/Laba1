money_capital = 20000
salary = 5000
spend = 6000
increase = 0.05
mes = 0
while money_capital >= 0:
    money_capital = money_capital + salary - spend
    spend = spend + spend * increase
    mes = mes + 1
    if money_capital < 0: mes = mes - 1
print("Количество месяцев, которое можно протянуть без долгов:", mes)