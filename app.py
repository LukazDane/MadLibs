# Attempt 3 - Starting over because I was doing way to much.
#-----------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------#
# Sites used for help/reference                                                                             #
# https://developer.rhino3d.com/guides/rhinopython/python-statements/                                       #
# https://www.w3resource.com/python/python-format.php                                                       #
# Also discussed various project solutions with Megan O'Bryan, Chris Barnes, Kye Williams and Audi Blades.  #
#-----------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------#

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

    print("You awake in a dimly lit room... \n As you look around you notice it appears to be a waiting room of sorts.\n There are no doors or windows as far as you can tell.\n You feel nothing but a stiff cold breeze that appears to be coming from all directions.\n The corners of the room seem darker than the rest.\n Almost as if the walls are ovrlapping eachother and folding into a space behind themselves. Where am I?\n ")
    print("A voice behiind you speaks, soft but heavy...\n \"Hello again, You've been here quite a while........ \n haven't you?\"")


# Ask user to input words to fill in blanks
firstAdj = user_input("Give me an adjective: ")
# Everytime the user gives you a word append that word to the list by calling the create function
create(firstAdj)
secondAdj = user_input("Derogatory Adj: ")
create(secondAdj)
thirdAdj = user_input("Discriptive adj: ")
create(thirdAdj)
noun = user_input("Random noun(item): ")
create(noun)
fourthAdj = user_input("Spooky Adj: ")
create(fourthAdj)
actionVerb = user_input("Action verb: ")
create(actionVerb)

# story with blanks filled in
print("\n \"You've been here quite a while, haven't you? You poor %s creature.\" \n \"Your soul is as %s, ageless and dry as the bark of the Yggdrasil.\" \n \"I know how you fear the unkown....\" \n \"Do not fret, it's nowhere near as %s and unfamiliar as you believe.\" \n \"Somewhere in this room is a key, that has taken the form of a %s.\" \n \"Touch it.\" \n \"If you are correct you will earn your freedom and another chance to obtain that which you believe you desire...\" \n \"Fail, however...\" \n \"and you will hear a thunderous %s sound, like that of a thousand souls churning in fire and you shall join them.\" \n \"Now %s as fast as you can! If you don't leave this place soon, you may forget how.... but that wouldn't be so bad would it?\" \n \n \n \n ...the voice fades away, and the room grows dark. \n Suddenly you feel as though you've awoken from a long, deep, slumber. \n There is a faint ringing in your ears, and a distant but familar memory of pained screaming in the back of your mind...\n .... \n" %
      (words_list[0], words_list[1], words_list[2], words_list[3], words_list[4], words_list[5]))


madLibs()
