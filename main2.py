kniga = 100 * 50 * 25 * 4
mega_kniga = kniga / (1024 ** 2)
kol = int(1.44 // mega_kniga)
print("Количество книг, помещающихся на дискету:", kol)