# string concatenation (how to put strings together)
# suppose we wanted to create a string that said "Hello, user!"
# there are a few ways to do this;
# \ at the end of a line tells python the statement has gone to a new line

# user = "World"

# print("Hello, " + user)
# print("Hello, {}!".format(user))
# print(f"Hello, {user}!")

# the f string format is the cleanest method to concatenate values together
# and can be used inside of a variable such as;
# variable = f"Computer Programming is super {adj}! It makes me feel {verb}!
# afterwards you just have to assign the variables adj, and verb, which could be a user input or set by you

# adj = input("Select an adjective: ") or in this case = great
# verb = input("Select a verb: ") or in this case = creative
# variable = f"Computer Programming is super {adj}! It makes me feel {verb}!
# print(variable)

# "Computer Programming is super great! It makes me feel creative"

# STORY ELEMENTS
title = "*** The Quest for the Lost Treasure Island ***"

brave_adventurer = input("Who, pray-tell is our Brave Adventurer?!")
homeland = input("And where does this Adventurer hail from?!")
shipName = input("Very good! Surely you are able to command a ship, but what of the ship's name?!")
navigator = input("Name someone who shall be your guiding hand in dark times.")
engineer = input("Name the clever one who is capable of solving even the hardest of puzzles!")
captain = input("What is the name of you little companion that follows you around?")

rareMaterial = input("What is a rare Stone or Metal?")
jewel = input("What is if favourite gem stone?")
artifact = input("Name the item you have been seeking!")
goldItem = input("Some items that would be awesome in Gold!")


# THE STORY
adventure_story = f""" {title}

Once upon a time in a land of {homeland}, lived a young adventurer named {brave_adventurer}. {brave_adventurer} had heard whispers of a legendary treasure island 
hidden in the heart of the vast ocean. Determined to unravel this enigma, {brave_adventurer} gathered a crew of intrepid companions and set sail on a grand 
voyage.

The crew consisted of {navigator}, the boisterous but kind-hearted navigator; {engineer}, the quick-witted engineer who could fix anything; and Captain {captain}, 
a parrot with a penchant for solving riddles. With their ship, the "{shipName}", creaking and groaning, they embarked on a journey that 
promised both danger and excitement.

Their first challenge arose when a fierce storm struck. Waves as tall as mountains threatened to engulf the ship, but {navigator}'s unwavering navigational 
skills guided them through the tempest. As they sailed into calmer waters, they stumbled upon a mysterious message in a bottle. The parchment read:

\"Beyond the horizon, where seagulls dance,
Lies the island of treasure, take a chance.
Three keys you'll need to open the way,
Solve riddles and puzzles, don't stray.\"

Intrigued by the riddle, the crew decided to follow its cryptic instructions. {engineer} proved to be a master puzzle-solver, deciphering ancient maps 
and unraveling riddles with ease. Captain {captain}'s squawks often contained the missing pieces of the puzzle, as if the parrot itself held ancient 
wisdom.

Their journey took them through treacherous waters and lush jungles, where they encountered playful monkeys and elusive creatures. Each step 
brought them closer to the heart of the mystery. Along the way, they discovered two of the three keys, intricately carved from {rareMaterial}.

As they ventured deeper into the heart of the island, they faced their final challenge - a massive stone door engraved with intricate patterns. 
To open it, they had to solve a complex riddle that required all their collective knowledge and wit. With teamwork and determination, they cracked 
the code, and the stone door slowly creaked open.

Inside the hidden chamber, they found a trove of glittering {jewel}, ancient {artifact}s, and chests of gold {goldItem}. The air was thick with awe 
as they realized they had truly found the Lost Treasure of {homeland}. But more than the riches, it was the journey, the camaraderie, and the thrill 
of the adventure that filled their hearts with true treasure.

With their hands full of priceless treasures and their spirits lifted by their conquest, the crew of the "{shipName}" sailed back to {homeland}'s Capital. 
Their tale of bravery, friendship, and discovery became legendary, inspiring others to seek their own adventures and create stories worth telling 
for generations to come.
"""

# PRINTING THE STORY
print(adventure_story)
