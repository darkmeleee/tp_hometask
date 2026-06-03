from ingredient import Ingredient
from recipe import Recipe

class ShoppingList:
    def __init__(self, _items: list[tuple[Ingredient, str]]):
        self._items = _items

    def add_recipe(self, recipe: Recipe, portions: float):
        if portions <= 0:
            raise ValueError("Количество порций должно быть положительным")
        for ingredient in recipe.scale(portions).ingredients:
            self._items.append((ingredient, recipe.title))

    def remove_recipe(self, title: str):
        self._items = [item for item in self._items if item[1] != title]
    
    def get_list(self):
        buyList = dict()
        for item in self._items:
            key = (item[0].name, item[0].unit)
            if key in buyList:
                buyList[key] += item[0].quantity
            else:
                buyList[key] = item[0].quantity
        result = [Ingredient(name, quantity, unit) for (name, unit), quantity in buyList.items()]
        result.sort(key=lambda x: x.name)
        return result

    def __add__(self, other: 'ShoppingList'):
        new_items = self._items + other._items
        return ShoppingList(new_items)
