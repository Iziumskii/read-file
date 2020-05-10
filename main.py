from pprint import pprint


def add_new_dish(feed, book):
    book.update({feed: []})


def add_recipe(feed, book, new_ingredient_name, new_quantity, new_measure):
    book[feed].append({"ingredient_name": new_ingredient_name, "quantity": new_quantity, "measure": new_measure})


def add_ingredient(new_ingredient, book):
    for requested_ingredient in book:
        if new_ingredient == requested_ingredient:
            pass
        else:
            book.update({new_ingredient: {}})


def making_recipe(data):
    recipe = data.readline().strip().split()
    return recipe[-1], recipe[-3], ' '.join(recipe[:-4])


def create_recipe(amount, dish, book):
    for i in range(amount):
        measure, quantity, ingredient_name = making_recipe(f)
        add_recipe(dish, book, ingredient_name, quantity, measure)


def make_cookbook(data, book):
    while True:
        dish = data.readline().strip()
        if not dish:
            break
        add_new_dish(dish, book)
        amount_dish = int(data.readline().rstrip())
        create_recipe(amount_dish, dish, book)
        data.readline()


def create_cookbook(data):
    cook_book = {}
    make_cookbook(data, cook_book)
    pprint(cook_book)
    return cook_book


def get_shop_list_by_dishes(book, dishes, person_count):
    list_by_dishes = {}
    number = 0
    for dish_in_book in dishes:
        if dishes[number] in book:
            for ingredient in book.get(dishes[number]):
                if ingredient['ingredient_name'] in list_by_dishes.keys():
                    ing_name = list_by_dishes.get(ingredient['ingredient_name'])
                    upd_quantity = int(ing_name.get('quantity')) + int(ingredient['quantity']) * person_count
                    list_by_dishes.update({ingredient['ingredient_name']: {"quantity": upd_quantity,
                                                                           "measure": ingredient['measure']}})
                else:
                    list_by_dishes.update({ingredient['ingredient_name']: {"quantity": int(ingredient['quantity']) *
                                                                                       person_count,
                                                                           "measure": ingredient['measure']}})
        number += 1
    pprint(list_by_dishes)


with open("cookbook.txt", encoding='utf8') as f:
    get_shop_list_by_dishes(create_cookbook(f), ['Фахитос', 'Омлет'], 2)
