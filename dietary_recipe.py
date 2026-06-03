from recipe import Recipe
from ingredient import Ingredient

class DietaryRecipe(Recipe):
    def __init__(self, title: str, diet_type: str, ingredients: list[Ingredient]=None):
        super().__init__(title, ingredients or [])
        self.diet_type = diet_type

    def scale(self, ratio: float):
        newRecept = DietaryRecipe(self.title, self.diet_type, [])
        for ingredient in super().scale(ratio).ingredients:
            newRecept.add_ingredient(Ingredient(ingredient.name, ingredient.quantity, ingredient.unit))
        return newRecept

    def __str__(self):
        parent_str = super().__str__()
        return f"[{self.diet_type}] {parent_str}"
