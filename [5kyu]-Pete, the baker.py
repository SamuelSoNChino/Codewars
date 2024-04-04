def cakes(recipe, available):
    num = float("inf")
    for ingredient in recipe.keys():
        try:
            pos = available[ingredient] // recipe[ingredient]
            if pos < num:
                num = pos
        except KeyError:
            return 0
    return num


recipe = {"flour": 500, "sugar": 200, "eggs": 1}
available = {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}
print(cakes(recipe, available))
