from ingredient import Ingredient
from recipe import Recipe
from shopping_list import ShoppingList
from dietary_recipe import DietaryRecipe

def test_ingredient_creation():
    ingredient = Ingredient("Тестовый ингредиент", 1.0, "г")
    assert ingredient.name == "Тестовый ингредиент"
    assert ingredient.quantity == 1.0
    assert ingredient.unit == "г"

def test_ingredient_str():
    ingredient = Ingredient("Тестовый ингредиент", 1.0, "г")
    assert str(ingredient) == "Тестовый ингредиент: 1.0 г"

def test_ingredient_eq():
    ingredient1 = Ingredient("Тестовый ингредиент", 1.0, "г")
    ingredient2 = Ingredient("Тестовый ингредиент", 1.0, "г")
    assert ingredient1 == ingredient2

def test_ingredient_eq_unit():
    ingredient1 = Ingredient("Тестовый ингредиент", 1.0, "г")
    ingredient2 = Ingredient("Тестовый ингредиент", 2.0, "г")
    assert ingredient1 == ingredient2

def test_ingredient_ne_name():
    ingredient1 = Ingredient("Тестовый ингредиент", 1.0, "г")
    ingredient2 = Ingredient("Другой ингредиент", 1.0, "г")
    assert ingredient1 != ingredient2

def test_ingredient_ne_unit():
    ingredient1 = Ingredient("Тестовый ингредиент", 1.0, "г")
    ingredient2 = Ingredient("Тестовый ингредиент", 1.0, "кг")
    assert ingredient1 != ingredient2

def test_recipe_creation():
    ingredients = [Ingredient("Рис", 500.0, "г"), Ingredient("Лосось", 2.0, "шт")]
    recipe = Recipe("Роллы", ingredients)
    assert recipe.title == "Роллы"
    assert len(recipe.ingredients) == 2
    assert recipe.ingredients[0].name == "Рис"

def test_add_ingredient_new():
    recipe = Recipe("Роллы", [])
    ingredient = Ingredient("Рис", 500.0, "г")
    recipe.add_ingredient(ingredient)
    assert len(recipe.ingredients) == 1
    assert recipe.ingredients[0].name == "Рис"

def test_add_ingredient_existing():
    recipe = Recipe("Роллы", [Ingredient("Рис", 500.0, "г")])
    ingredient = Ingredient("Рис", 200.0, "г")
    recipe.add_ingredient(ingredient)
    assert len(recipe.ingredients) == 1
    assert recipe.ingredients[0].quantity == 700.0

def test_scale_returns_new():
    ingredients = [Ingredient("Рис", 500.0, "г")]
    recipe = Recipe("Роллы", ingredients)
    scaled = recipe.scale(2.0)
    assert scaled is not recipe
    assert recipe.ingredients[0].quantity == 500.0

def test_scale_multiplies_quantities():
    ingredients = [Ingredient("Рис", 500.0, "г"), Ingredient("Лосось", 2.0, "шт")]
    recipe = Recipe("Роллы", ingredients)
    scaled = recipe.scale(2.0)
    assert scaled.ingredients[0].quantity == 1000.0
    assert scaled.ingredients[1].quantity == 4.0

def test_scale_invalid_ratio():
    ingredients = [Ingredient("Рис", 500.0, "г")]
    recipe = Recipe("Роллы", ingredients)
    try:
        recipe.scale(0)
        assert False, "Ожидалось исключение ValueError"
    except ValueError:
        pass

def test_len():
    ingredients = [Ingredient("Рис", 500.0, "г"), Ingredient("Лосось", 2.0, "шт")]
    recipe = Recipe("Роллы", ingredients)
    assert len(recipe) == 2

def test_add_recipe():
    ingredients = [Ingredient("Рис", 500.0, "г")]
    recipe = Recipe("Роллы", ingredients)
    shopping_list = ShoppingList([])
    shopping_list.add_recipe(recipe, 1.0)
    assert len(shopping_list._items) == 1

def test_add_recipe_invalid_portions():
    ingredients = [Ingredient("Рис", 500.0, "г")]
    recipe = Recipe("Роллы", ingredients)
    shopping_list = ShoppingList([])
    try:
        shopping_list.add_recipe(recipe, 0)
        assert False, "Ожидалось исключение ValueError"
    except ValueError:
        pass

def test_remove_recipe():
    ingredients = [Ingredient("Рис", 500.0, "г")]
    recipe = Recipe("Роллы", ingredients)
    shopping_list = ShoppingList([])
    shopping_list.add_recipe(recipe, 1.0)
    shopping_list.remove_recipe("Роллы")
    assert len(shopping_list._items) == 0

def test_remove_recipe_nonexistent():
    ingredients = [Ingredient("Рис", 500.0, "г")]
    recipe = Recipe("Роллы", ingredients)
    shopping_list = ShoppingList([])
    shopping_list.add_recipe(recipe, 1.0)
    shopping_list.remove_recipe("Не существует")
    assert len(shopping_list._items) == 1

def test_get_list_sums_same_ingredients():
    ingredients1 = [Ingredient("Рис", 500.0, "г")]
    ingredients2 = [Ingredient("Рис", 300.0, "г")]
    recipe1 = Recipe("Роллы", ingredients1)
    recipe2 = Recipe("Суши", ingredients2)
    shopping_list = ShoppingList([])
    shopping_list.add_recipe(recipe1, 1.0)
    shopping_list.add_recipe(recipe2, 1.0)
    result = shopping_list.get_list()
    assert len(result) == 1
    assert result[0].quantity == 800.0

def test_get_list_sorted():
    ingredients = [Ingredient("Лосось", 2.0, "шт"), Ingredient("Рис", 500.0, "г")]
    recipe = Recipe("Роллы", ingredients)
    shopping_list = ShoppingList([])
    shopping_list.add_recipe(recipe, 1.0)
    result = shopping_list.get_list()
    assert result[0].name == "Лосось"
    assert result[1].name == "Рис"

def test_add_shopping_lists():
    ingredients1 = [Ingredient("Рис", 500.0, "г")]
    ingredients2 = [Ingredient("Лосось", 2.0, "шт")]
    recipe1 = Recipe("Роллы", ingredients1)
    recipe2 = Recipe("Суши", ingredients2)
    list1 = ShoppingList([])
    list2 = ShoppingList([])
    list1.add_recipe(recipe1, 1.0)
    list2.add_recipe(recipe2, 1.0)
    combined = list1 + list2
    assert len(combined._items) == 2

def test_add_shopping_lists_originals_unchanged():
    ingredients1 = [Ingredient("Рис", 500.0, "г")]
    ingredients2 = [Ingredient("Лосось", 2.0, "шт")]
    recipe1 = Recipe("Роллы", ingredients1)
    recipe2 = Recipe("Суши", ingredients2)
    list1 = ShoppingList([])
    list2 = ShoppingList([])
    list1.add_recipe(recipe1, 1.0)
    list2.add_recipe(recipe2, 1.0)
    combined = list1 + list2
    assert len(list1._items) == 1
    assert len(list2._items) == 1



