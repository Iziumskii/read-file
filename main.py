from pprint import pprint


def add_new_dish(feed, book):
    book.update({feed: []})


def add_new_recipe(feed, book, new_ingredient_name, new_quantity, new_measure):
    book[feed].append({"ingredient_name": new_ingredient_name, "quantity": new_quantity, "measure": new_measure})


def add_ingredient(new_ingredient, book):
    for requested_ingredient in book:
        if new_ingredient == requested_ingredient:
            pass
        else:
            book.update({new_ingredient: {}})


def get_shop_list_by_dishes(dishes, book):
    list_by_dishes = {}
    number = 0
    for dish_in_book in dishes:
        if dishes[number] in book:
            for ingredient in book.get(dishes[number]):
                if ingredient['ingredient_name'] in list_by_dishes.keys():
                    ing_name = list_by_dishes.get(ingredient['ingredient_name'])
                    upd_quantity = int(ing_name.get('quantity')) + int(ingredient['quantity'])
                    list_by_dishes.update({ingredient['ingredient_name']: {"quantity": upd_quantity,
                                                                           "measure": ingredient['measure']}})
                else:
                    list_by_dishes.update({ingredient['ingredient_name']: {"quantity": ingredient['quantity'],
                                                                           "measure": ingredient['measure']}})
        number += 1
    pprint(list_by_dishes)


cook_book = {}

with open("cookbook.txt", encoding='utf8') as f:
    while True:
        dish = f.readline().strip()
        if not dish:
            break
        add_new_dish(dish, cook_book)
        amount = int(f.readline().rstrip())
        for i in range(amount):
            recipe = f.readline().strip().split()
            measure = recipe[-1]
            quantity = recipe[-3]
            ingredient = recipe[:-4]
            ingredient_name = ' '.join(ingredient)
            add_new_recipe(dish, cook_book, ingredient_name, quantity, measure)
        f.readline()
    pprint(cook_book)

    get_shop_list_by_dishes(['Фахитос', 'Омлет'], cook_book)
