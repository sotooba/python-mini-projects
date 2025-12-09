# To print calories

calorie_dict = {
    # Fruits (approx. kcal per 100 g)
    "apple": 52,
    "banana": 89,
    "orange": 47,
    "mango": 60,
    "strawberry": 32,
    "watermelon": 30,
    "pineapple": 50,
    "grapes": 69,
    "blueberries": 57,
    "pear": 57,
    "peach": 42,
    "plum": 46,
    "apricot": 48,
    "avocado": 160,
    "kiwi": 61,
    "pomegranate": 83,
    "papaya": 43,
    "cherry": 50,
    "raspberry": 53,
    "blackberries": 43,
    "cantaloupe": 34,
    "lime": 30,
    "lemon": 29,
    "fig": 74,
    "coconut_meat": 354,

    # Vegetables (approx. kcal per 100 g)
    "carrot": 41,
    "tomato": 18,
    "cucumber": 15,
    "spinach": 23,
    "broccoli": 34,
    "cauliflower": 25,
    "bell_pepper": 31,
    "lettuce": 5,
    "green_beans": 31,
    "zucchini": 17,
    "peas": 81,
    "asparagus": 20,
    "eggplant": 25,
    "kale": 49,
    "sweet_potato": 86,
    "radish": 16,
    "cabbage": 25,
    "celery": 16,
    "onion": 40,
    "beetroot": 43,
    "brussels_sprouts": 43,
    "pumpkin": 26,
    "mushroom": 22,
    "corn": 96,
    "artichoke": 47,
    "leek": 61,
    "turnip": 28,
    "garlic": 149,
    "ginger": 80,
    "yam": 118,
    "butternut_squash": 45,
    "parsnip": 75
}


item = input("What you ate today? (Fruit / Vegetable): ").strip().lower()

if item in calorie_dict:
    print(f"{item.capitalize()} contains {calorie_dict[item]} kcal per 100g")
else:
    print("Invalid input! Please input Fruit or Vegetable")
