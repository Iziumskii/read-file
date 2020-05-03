from pprint import pprint


def add_new_dish(feed, book):
    book.update({feed: []})


def add_new_recipe(feed, book, new_ingredient_name, new_quantity, new_measure):
    book[feed].append({"ingredient_name": new_ingredient_name, "quantity": new_quantity, "measure": new_measure})


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


