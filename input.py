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
    food = "asparagus, apples, avacado, alfalfa, acorn squash, almond, arugala, artichoke, applesauce, asian noodles, antelope, ahi tuna, albacore tuna, Apple juice, Avocado roll, Bruscetta, bacon, black beans, bagels, baked beans, BBQ, bison, barley, beer, bisque, bluefish, bread, broccoli, buritto, babaganoosh, Cabbage, cake, carrots, carne asada, celery, cheese, chicken, catfish, chips, chocolate, chowder, clams, coffee, cookies, corn, cupcakes, crab, curry, cereal, chimichanga"
    while not goodInput:
        response = raw_input(prompt)
        goodInput = True
        for character in response:
            if character not in food:
                goodInput = False
                print "Food only please!"
    return response
        



















