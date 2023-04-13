# На вход подается возраст и вес спортсмена. Вывести группу по возрасту и весовую категорию, в которой он будет принимать участие согласно следующим правилам.
# Соревнования юношей младшей возрастной группы (14—15 лет) проводятся без деления участников на весовые категории.
# Соревнования для юношей старшего возраста (16—17 лет) проводятся в весовых категориях:
# легчайшая - до 52 кг, легкая - до 57, средняя - до 70, тяжёлая - до 80, вторая тяжелая свыше 80
# Соревнования для юниоров (18—19 лет) и взрослых (20 лет и старше)
# легчайшая - до 54 кг, легкая - до 60, средняя - до 75, тяжелая свыше 81
# Лица младше 14 или весом ниже 44 кг до соревнований не допускаются

age = int(input('Enter your age: '))
if age < 14:
    print("You're not allowed for competition")
else:
    weight = int(input('Enter your weight: '))
    if weight < 44:
        print("You're not allowed for competition")
    elif 14 <= age <= 15:
        print("You're in Younger group")
    elif 16 <= age <= 17:
        print("You're in Adolescent group", end = ' ')
        if weight < 52:
            print("& in the lightest weight category")
        elif weight < 57:
            print("& in the light weight category")
        elif weight < 70:
            print("& in the average weight category")
        elif weight < 80:
            print("& in the heavy weight category")
        else:
            print("& in the 2nd heavy weight category")
    elif 18 <= age <= 19:
        print("You're in Junior group", end = ' ')
        if weight < 54:
            print("& in the lightest weight category")
        elif weight < 60:
            print("& in the light weight category")
        elif weight < 75:
            print("& in the average weight category")
        elif weight < 81:
            print("& in the heavy weight category")
        else:
            print("& in the 2nd heavy weight category")
    elif age >= 20:
        print("You're in Adult group", end = ' ')
        if weight < 54:
            print("& in the lightest weight category")
        elif weight < 60:
            print("& in the light weight category")
        elif weight < 75:
            print("& in the average weight category")
        elif weight < 81:
            print("& in the heavy weight category")
        else:
            print("& in the 2nd heavy weight category")


