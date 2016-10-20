def isSwear(word):
    swearList = ["poop",
                 "pee"]
    if word in swearList:
        return True
    else:
        return False

def getMenuOption():
    goodInput = False
    goodResponses = ["1",
                     "2",
                     "3",
                     "q"]
    while not goodInput:
        response = raw_input("Make a selection: ")
        if response.lower() in goodResponses:
            goodInput = True
        else:
            print "Please make a valid selection!"
    return response.lower()

def getWord(prompt):
    goodInput = False
    while not goodInput:
        response = raw_input(prompt)
        goodInput = True
        if isSwear(response):
            goodInput = False
            print "Don't use that kind of language with me!"
    return response

def getNumber(prompt):
    goodInput = False
    numbers = "0123456789."
    while not goodInput:
        response = raw_input(prompt)
        goodInput = True
        for character in response:
            if character not in numbers:
                goodInput = False
                print "Numbers only please!"
    return response
        
def getFood(prompt):
    goodInput = False
    food = ["asparagus",
            "apples",
            "apple",
            "avacado",
            "alfalfa",
            "acorn",
            "squash",
            "almond",
            "arugala",
            "artichoke",
            "applesauce",
            "asian noodles",
            "antelope",
            "ahi tuna",
            "albacore tuna",
            "apple juice",
            "avocado roll",
            "bruscetta",
            "bacon",
            "black beans",
            "bagels,",
            "baked beans",
            "BBQ",
            "bison",
            "barley",
            "beer",
            "bisque",
            "bluefish",
            "bread",
            "broccoli",
            "buritto",
            "babaganoosh",
            "cabbage",
            "cake",
            "carrots",
            "carne asada",
            "celery",
            "cheese",
            "chicken",
            "catfish",
            "chips",
            "chocolate",
            "chowder",
            "clams",
            "coffee",
            "cookies",
            "corn",
            "cupcakes",
            "crab",
            "curry",
            "cereal",
            "chimichanga",
            "dates",
            "dips",
            "duck",
            "dumplings",
            "donuts",
            "eggs",
            "enchilada",
            "eggrolls",
            "english muffins",
            "edimame",
            "eel sushi",
            "fajita",
            "falafel",
            "fish",
            "franks",
            "fondu",
            "french toast",
            "french dip",
            "garlic",
            "ginger",
            "gnocchi",
            "goose",
            "granola",
            "grapes",
            "green beans",
            "guancamole",
            "gumbo",
            "grits",
            "graham crackers",
            "ham",
            "halibut",
            "hamburger",
            "honey",
            "huenos rancheros",
            "hash browns",
            "hot dogs",
            "haiku roll",
            "hummus",
            "ice cream",
            "irish stew",
            "indian food",
            "italian bread",
            "jambalaya",
            "jelly",
            "jam",
            "jerky",
            "jalapeño",
            "kale",
            "kabobs",
            "ketchup",
            "kiwi",
            "kidney beans",
            "kingfish",
            "lobster",
            "lamb",
            "linguine",
            "lasagna",
            "meatballs",
            "moose",
            "milk",
            "milkshake",
            "noodles",
            "ostrich",
            "Pizza",
            "Pepperoni",
            "Porter",
            "Pancakes",
            "quesadilla",
            "quiche",
            "reuben",
            "spinach",
            "spaghetti",
            "tater tots",
            "toast",
            "venison",
            "waffles",
            "wine",
            "walnuts",
            "yogurt",
            "ziti",
            "zucchini"]
            
    while not goodInput:
        response = raw_input(prompt)
        goodInput = True
        if response not in food:
            goodInput = False
            print "Food only please!"
    return response
        



















