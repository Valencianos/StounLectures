# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z
# Данное выражение истинно при любых значениях предикат (предикат - переменная, которая может иметь только два значения True или False)
# Напишите программу, которая докажет это.

for x in range(0, 2):
    for y in range(0, 2):
        for z in range(0, 2):
            if not(x or y or z) == (not x and not y and not z):
                print(f'x = {x}, y = {y}, z = {z} - correct')
            else:
                print(f'x = {x}, y = {y}, z = {z} - incorrect')