import re
import itertools
from dataclasses import dataclass


def partitions(n, k):
    '''source: https://stackoverflow.com/questions/28965734/general-bars-and-stars'''
    for c in itertools.combinations(range(n+k-1), k-1):
        yield [b-a-1 for a, b in zip((-1,)+c, c+(n+k-1,))]

@dataclass(slots=True)
class Ingredient:
    type: str
    capacity: int
    durability: int
    flavor: int
    texture: int
    calories: int

    def __post_init__(self):
        self.capacity = int(self.capacity)
        self.durability = int(self.durability)
        self.flavor = int(self.flavor)
        self.texture = int(self.texture)
        self.calories = int(self.calories)

@dataclass(slots=True)
class CookieRating:
    score: int
    calories: int

type Teaspoon = int
type Recipe = list[tuple[Ingredient, Teaspoon]]

def score_cookie(recipe: Recipe) -> CookieRating:
    capacity = 0
    durability = 0
    flavor = 0
    texture = 0
    calories = 0

    for ingredient, qty in recipe:
        capacity += ingredient.capacity * qty
        durability += ingredient.durability * qty
        flavor += ingredient.flavor * qty
        texture += ingredient.texture * qty

        calories += ingredient.calories * qty

    score = max(capacity, 0) * max(durability, 0) * max(flavor, 0) * max(texture, 0)
    return CookieRating(score, calories)

regex = r'(\w+): capacity ([-]?\d+), durability ([-]?\d+), flavor ([-]?\d+), texture ([-]?\d+), calories ([-]?\d+)'

maximum_teaspoons = 100

text = open('input.txt').read()
pantry = [Ingredient(*fields) for fields in re.findall(regex, text)]
number_of_ingredients = len(pantry)

best_rating = None
best_recipe = None

best_rating_500cal = 0
best_recipe_500cal = None

for quantities in partitions(maximum_teaspoons, number_of_ingredients):
    recipe = [(ingredient, qty) for ingredient, qty in zip(pantry, quantities)]

    rating = score_cookie(recipe)

    better_than_best = not best_rating or rating.score > best_rating.score

    if better_than_best:
        best_rating = rating
        best_recipe = recipe

    if rating.calories != 500:
        continue

    better_than_best_500cal = not best_rating_500cal or rating.score > best_rating_500cal.score

    if better_than_best_500cal:
        best_rating_500cal = rating
        best_recipe_500cal = recipe

assert best_recipe
assert best_recipe_500cal

print("Best Recipe: (part one)")
for ingredient, qty in best_recipe:
    print(f'{ingredient.type}({qty}) ', end='')

print('\nScore:', best_rating)

print("Best 500 Calorie Recipe: (part two)")
for ingredient, qty in best_recipe_500cal:
    print(f'{ingredient.type}({qty}) ', end='')

print('\nScore:', best_rating_500cal)
