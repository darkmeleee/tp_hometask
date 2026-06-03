from ingredient import Ingredient

class Recipe:
    def __init__(self, title: str, ingredients: list[Ingredient]):
        self.title = title
        self.ingredients = ingredients
    
    def add_ingredient(self, ingredient: Ingredient):
        if ingredient in self.ingredients:
            self.ingredients[self.ingredients.index(ingredient)].quantity += ingredient.quantity
        else:
            self.ingredients.append(ingredient)
    
    @staticmethod
    def is_valid_ratio(ratio: float):
        if type(ratio) == float and ratio > 0.0:
            return True
        return False

    def scale(self, ratio: float):
        newRecept = Recipe(self.title, [])
        for ingredient in self.ingredients:
            newRecept.add_ingredient(Ingredient(ingredient.name, ingredient.quantity * ratio, ingredient.unit))
        return newRecept
    
    def __len__(self):
        return len(self.ingredients)

    def __str__(self):
        str = f"{self.title}: {len(self)} ингредиентов\n"
        for ingredient in self.ingredients:
            str += f"  {ingredient}\n"
        return str
