class Ingredient:
    def __init__(self, name: str, quantity: float, unit: str):
        self.name = name
        self.quantity = quantity
        self.unit = unit
    
    @property
    def quantity(self):
        return self._quantity
    
    @quantity.setter
    def quantity(self, value):
        if value < 0:
            raise ValueError("Количество должно быть положительным")
        self._quantity = float(value)

    def __str__(self):
        return f"{self.name}: {self.quantity} {self.unit}"

    def __repr__(self):
        return f"Ingredient('{self.name}', {self.quantity}, '{self.unit}')"
    
    def __eq__(self, other):
        if not isinstance(other, Ingredient):
            return False
        return self.name == other.name and self.unit == other.unit
    
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

    def scale(ratio: float):
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
