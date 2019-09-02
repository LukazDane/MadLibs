# Attempt 3 - Starting over because I was doing way to much.

# Create a list of words [required]
words_list = list()

# append to list


def create(item):
    words_list.append(item)

# User Input Functions


def user_input(prompt):
    user_input = input(prompt)
    return user_input


def madLibs():
    # Start the game
    print("You awake in a dimly lit room. As you look around you notice it appears to be a waiting room of sorts. There are no doors or windows as far as you can tell. You feel nothing but a stiff cold breeze that appears to be coming from all directions. The corners of the room seem darker than the rest. Alost as if the walls are ovrlapping eachother and folding into a space behind themselves. Where am I? ")
    print("A voice behiind you speaks, soft but heavy,\" ")

    # Display story with blanks
# print("You've been here quite a while, haven't you. You poor ___ creature. Your soul is as ___ and dry as the bark of the Yggdrasil. I know how you fear the unkown. Don't fret, it's nowhere near as ___ and dark as you believe. Somewhere in this room is a key, shaped like a large ___. Touch it. If you are correct you will earn your freedom and another chance. Fail and you will hear a ___ sound, like that of a thousand souls churning in fire and you shall join them. Now __ as fast as you can! If you don't leave this place soon, you may forget how.... but that wouldn't be so bad would it?")
# Ask user to input words to fill in blanks
firstAdj = user_input("Give me an adjective: ")
# Everytime the user gives you a word append that word to the list by calling the create function
create(firstAdj)
secondAdj = user_input("Derogatory Adj: ")
create(secondAdj)
thirdAdj = user_input("Discriptive adj: ")
create(thirdAdj)
noun = user_input("Random noun: ")
create(noun)
fourthAdj = user_input("Spooky Adj: ")
create(fourthAdj)
actionVerb = user_input("Action verb: ")
create(actionVerb)
# story with blanks filled in
print("You've been here quite a while, haven't you. You poor %s creature. Your soul is as %s and dry as the bark of the Yggdrasil. I know how you fear the unkown. Don't fret, it's nowhere near as %s and dark as you believe. Somewhere in this room is a key, shaped like a large %s. Touch it. If you are correct you will earn your freedom and another chance. Fail and you will hear a %s sound, like that of a thousand souls churning in fire and you shall join them. Now __ as fast as you can! If you don't leave this place soon, you may forget how.... but that wouldn't be so bad would it?" % (
    words_list[0], words_list[1], words_list[2], words_list[3], words_list[4], words_list[5]))


madLibs()
