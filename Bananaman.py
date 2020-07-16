def doomed():
    print ("\nWelp, they're doomed")
    print ("\n*Bananaman flies away, deaf to your anguished yells...*")
    print ("\nYOU LOSE")
    quit()

def one():
    name = input("Ok, who? (Enter 1 if you don't know who!) ")
    if name == ("1"):
        doomed()
    else:
        two(name)

def two(name):
    print()
    print(name, " did you say? Where are they? ")
    location = input("\nEnter 1 if you haven't the foggiest where they are! ")
    if location == '1':
        doomed()
    elif location.lower() == 'here':
        three()
    else:
        four(name, location)

def three():
    print ("\nOh really? I don't believe you")
    print ("\n*Bananaman punches you and everything goes black...*")
    print ("\nYOU LOSE")
    quit()

def four(name, location):
    print("\nSo, ", name, " is trapped in ", location,", huh? Come with me!")
    print ('''\n*You follow Bananaman into a secret lair full of strange gadgets.
You long to touch one. What do you do?*''')
    answer = input("\nA: you touch them, or B: you resist... ")
    if answer.upper() == 'A':
        five()
    elif answer.upper() == 'B':
        six(name, location)
    else:
        print("\nI'm sorry, Bananaman didn't quite get that!")

def five():
    print ("\nWait, no! That's too dangero-! *SPLAT!*")
    print ("\n*You and Bananaman are blasted to smithereens by a small alien blob*")
    print ("\nYOU LOSE")
    quit()

def six(name, location):
    print ("\n*You resist the temptation to touch them*")
    print ("\n*Soon Bananaman grabs you by the arm and flies off to ", location,
           ", where you meet ", name, "'s captor.*")
    meanie = input("\nWhat is the captor called? ")
    print ("\nWhat does", meanie, " look like? ")
    appearance = input('''\nA: they have sallow skin and an evil face...
B: they are short with a toothbrush moustache on their face...
C: they have green eyes and they are, in fact, an apple! ''')
    if appearance.upper() == 'A':
        seven(name, location, meanie)
    elif appearance.upper() == 'B':
        eight(name, location, meanie)
    elif appearance.upper() == 'C':
        nine(name, location, meanie)
    else:
        print("\nI'm sorry, Bananaman didn't quite get that...")

def seven(name, location, meanie):
    print ("\n*The sallow-skinned, evil faced ", meanie,
           "pulls a green ruler from their pocket and flings it at you. What do you do?*")
    choice = input("\nA: you try to catch the ruler, or B: you do nothing")
    if choice.upper() == ("A"):
        print ("\n*You raise your arm and catch the ruler, throwing it back at ",
               meanie, "'s face. They stumble to the ground, not yet defeated.*")
        print ("\n*Just as it seems all hope is lost, ", name,
               "comes to, and with a dazed grin, pummels ",meanie ,"into the ground...*")
        print ("\nCONGRATULATIONS! YOU WIN!")
        quit()
    elif choice.upper() == ("B"):
        print ("\n*The green ruler hits you square in the face, and you black out...*")
        print ("\nYOU LOSE")
        quit()

def eight(name, location, meanie):
    print ("\n*The tiny", meanie,
           '''\'s moustache wriggles like a caterpillar as they pull a slice of pizza
from their pocket. What do you do?*''')
    choice = input('''\nA: you break free from Bananaman's grip and try to steal the pizza...
B: you stay put... ''')
    if choice.upper() == ("A"):
        print ('''\n*You break free from Bananaman's grip, but as you fall you fail to notice the
beartrap beneath you...
...SNAP*''')
        print ("\nYOU LOSE")
        quit()
    elif choice.upper() == ("B"):
        print ("\n*You stay put as Bananaman sends a laser beam from his eyes. ",
           meanie, "gets a full blast and is reduced to a pile of ash, but thankfully ",
           name, "is alright...*")
        print ("CONGRATULATIONS! YOU WIN!")
        quit()

def nine(name, location, meanie):
    print ("\n*The strange, green-eyed apple laughs maniacally, holding ",
           name, ''' in their chubby fists. Just as they are about to hit you and Bananaman,
you notice a little mark on their round body. What do you do?*''')
    choice = input("\nA: you ignore it and accept your fate, or B: you tell Bananaman...")
    if choice.upper() == ("A"):
        print ("\n*As you sob at the pointlessness of it all, Bananaman attempts to stop",
               meanie, ''', but his attempt is in vain. You and he are plucked from the sky
and eaten up in one gulp.*
YOU LOSE''')
        quit()
    elif choice.upper() == "B":
        print ("\n*You whisper to Bananaman about the spot*")
        print ("\nGo! I'll distract him!")
        print ("\nWhat do you do?")
        distract = input("\nA: leave Bananaman and find the mark, or B: stay with him...")
        if distract.upper() == "A":
            ten(meanie)
        elif distract.upper() == 'B':
            eleven()

def ten(meanie):
    print ("\n*Bananaman sacrifices himself, but you find the brown mark and, upon kicking it,",
           meanie, "slumps to the ground, dead.*")
    print ("\nCONGRATULATIONS! YOU WIN!")
    quit()

def eleven():
    print ("\nYou stay with Bananaman, and are plucked from the sky and eaten up in one gulp.*")
    print ("\nYOU LOSE")
    quit()
    
# main
print ("Hello! I'm your friendly neighbourhood Bananaman, here to save the day!")
choice = input("Is anyone in trouble? ")
if choice.lower().startswith('y'):
    one()
else:
    print ("\nOk, bye then")
    print ("\n*Bananaman flies off into the distance...*")
    quit()
