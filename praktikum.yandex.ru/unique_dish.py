#! python
# -*- coding: utf-8 -*-

# напишите здесь функцию print_shopping_list(),
# подобрав уникальные названия продуктов и сложив значения
def print_shopping_list(dish1, dish2):
    unique_dish = set(dish1.keys()).union(set(dish2.keys()))
    #print(', '.join(unique_dish)) #check set
    new_dict = {}
    for product in unique_dish:
        if product in dish1.keys() and product in dish2.keys():
            new_dict[product] = dish1[product] + dish2[product]
        elif product in dish1.keys() and product not in dish2.keys():
            new_dict[product] = dish1[product]
        elif product in dish2.keys() and product not in dish1.keys():
            new_dict[product] = dish2[product]
        else:
            pass    #for some reason

    #print out
    for key, value in new_dict.items():
        print(key + ': ' + str(value))


pizza = {'мука, кг': 1,
         'помидоры, кг': 1.5,
         'шампиньоны, кг': 1.5,
         'сыр, кг': 0.8,
         'оливковое масло, л': 0.1,
         'дрожжи, г': 50}

salad = {'огурцы, кг': 1,
         'перцы, кг': 1,
         'помидоры, кг': 1.5,
         'оливковое масло, л': 0.1,
         'листья салата, кг': 0.4}

print_shopping_list(pizza, salad)
