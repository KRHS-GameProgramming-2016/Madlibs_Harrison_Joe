from input import *

#Written by Joseph Poltack and Harrison Lord
def story():
    name1 = getWord("Enter a name ")
    name2 = getWord("Enter a name ")
    building1 = getWord("Enter a building ")
    food1 = getWord("Enter a food item ")
    
    
    text = ""
    text += "Two people named " + name1
    text += " and " + name2
    text += " lived in a(n) " + building1
    text += ". They were both hungry so they went out to get some " + food1
    text += ". " + name1
    text += "jumped into " +name2
    text += "'s car."
    
    
    
      
    return text
