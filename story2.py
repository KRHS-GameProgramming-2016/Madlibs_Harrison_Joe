from input import *

#written by Joseph Poltack
def story():
    day1 = getWord("Enter a day of a week ")
    food1 = getFood("Enter a food item ")
    shoebrand1 = getWord("Enter shoe brand name ")
    place1 = getWord("Enter a place ")
    person_or_thing1 = getWord("Enter a person or thing ")
    something_you_can_wear1 = getWord("Something you can whare ")
    weapon1 = getWord("Enter a weapon ")
    weapon2 = getWord("Enter another weapon ")
    
    text =  ""
    text += " It was a " + day1
    text += " morning and I was hungry. I dicited to have " + food1
    text += " for beckfast. When I finished beakfast I then got drested and put on my " + shoebrand1
    text += " shoes. After that I dicited to go for a walk to a" + place1
    text += ". It was dark and spooky outside. Their was nobody around besides me and the cool air, or so I thought. Next thing I know their was a" + person_or_thing1
    text += " chaceing me. So I started running. This" + person_or_thing1
    text += " just keped on folowing me wheir ever I went. I finaly ran out of breath and I confrounted him face to face, but i coundn't see it's face. It was being coverd up by " + something_you_can_wear1
    text += " . So I just asked why he was fallowing me. Right after I finished that sentance he pulled out a" + weapon1
    text += " . Unlucky for him I also brought my" + weapon2
    text += " . Then we faought to the death."




    return text
