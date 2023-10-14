users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']
slovar = {'Общее количество':0, 'Уникальные посещения':0}
kol =len(users)
unique_users = set(users)
kol_unic = len(unique_users)
slovar['Общее количество'] = kol
slovar['Уникальные посещения'] = kol_unic
print(slovar)