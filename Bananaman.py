print ("Hello! I'm your friendly neighbourhood Bananaman, here to save the day!")
print ("Is anyone in trouble?")
while True:
    answer1 = input()
    if answer1 == ("Yes") or answer1 == ("yes"):
        print ("Ok, who?")
        answer2 = input()
        if answer2 == ("I don't know") or answer2 == ("I dont know") or answer2 == ("i don't know") or answer2 == ("i dont know"):
             print ("Welp, they're doomed")
             print ("*Bananaman flies away, deaf to your anguished yells...*")
             print ("YOU LOSE")
             quit()
        print (answer2,", did you say? Where are they?")
        answer3 = input()
        if answer3 == ("I don't know") or answer3 == ("I dont know") or answer3 == ("i don't know") or answer3 == ("i dont know"):
            print ("Welp, they're doomed")
            print ("*Bananaman flies away, deaf to your anguished yells...*")
            print ("YOU LOSE")
            quit()
        elif answer3 == ("Here") or answer3 == ("here"):
            print ("Oh really? I don't believe you")
            print ("*Bananaman punches you and everything goes black...*")
            print ("YOU LOSE")
            quit()
        else:
            print ("So",answer2,"is trapped in",answer3,", huh? Come with me")
            print ("*You follow Bananaman into a secret lair full of strange gadgets. You long to touch one. What do you do?*")
            print ("A: you touch them, or B: you resist.")
            answer4 = input()
            if answer4 == ("A") or answer4 == ("a"):
                print ("Wait, no! That's too dangero-! *SPLAT!*")
                print ("*You and Bananaman are blasted to smithereens by a small alien blob*")
                print ("YOU LOSE")
                quit()
            elif answer4 == ("B") or answer4 == ("b"):
                print ("*You resist the temptation to touch them*")
                print ("*Soon Bananaman grabs you by the arm and flies off to",answer3,", where you meet",answer2,"'s captor.*")
                print ("What is the captor called?")
                answer5 = input()
                print ("What does",answer5,"look like?")
                print ("A: they have sallow skin and an evil face, B: they are short with a toothbrush moustache on their face, or C: they have green eyes and they are, in fact, an apple.")
                answer6 = input()
                if answer6 == ("A") or answer6 == ("a"):
                    print ("*The sallow-skinned, evil faced",answer5,"pulls a green ruler from their pocket and flings it at you. What do you do?*")
                    print ("A: you try to catch the ruler, or B: you do nothing")
                    answer8 = input()
                    if answer8 == ("A") or answer8 == ("a"):
                        print ("*You raise your arm and catch the ruler, throwing it back at",answer5,"'s face. They stumble to the ground, not yet defeated.*")
                        print ("*Just as it seems all hope is lost,",answer2,"comes to, and with a dazed grin, pummels",answer5,"into the ground...*")
                        print ("CONGRATULATIONS! YOU WIN!")
                        quit()
                    elif answer8 == ("B") or answer8 == ("b"):
                        print ("*The green ruler hits you square in the face, and you black out...*")
                        print ("YOU LOSE")
                        quit()
                elif answer6 == ("B") or answer6 == ("b"):
                    print ("*The tiny",answer5,"'s moustache wriggles like a caterpillar as they pull a slice of pizza from their pocket. What do you do?*")
                    print ("A: you break free from Bananaman's grip and try to steal the pizza, or B: you stay put")
                    answer7 = input()
                    if answer7 == ("A") or answer7 == ("a"):
                        print ("*You break free from Bananaman's grip, but as you fall you fail to notice the beartrap beneath you...*")
                        print ("*SNAP*")
                        print ("YOU LOSE")
                    elif answer7 == ("B") or answer7 == ("b"):
                        print ("*You stay put as Bananaman sends a laser beam from his eyes. ",answer5,"gets a full blast and is reduced to a pile of ash, but thankfully",answer2,"is alright...*")
                        print ("CONGRATULATIONS! YOU WIN!")
                        quit ()
                elif answer6 == ("C") or answer6 == ("c"):
                    print ("*The strange, green-eyed apple laughs maniacally, holding",answer2,"in their chubby fists. Just as they are about to hit you and Bananaman, you notice a little mark on their round body. What do you do?*")
                    print ("A: you ignore it and accept your fate, or B: you tell Bananaman")
                    answer9 = input()
                if answer9 == ("A") or answer9 == ("a"):
                    print ("*As you sob at the pointlessness of it all, Bananaman attempts to stop",answer2,",but his attempt is in vain. You and he are plucked from the sky and eaten up in one gulp.*")
                    print ("YOU LOSE")
                    quit()
                elif answer9 == ("B") or answer9 == ("b"):
                    print ("*You whisper to Bananaman about the spot*")
                    print ("Go! I'll distract him!")
                    print ("What do you do?")
                    print ("A: leave Bananaman and find the mark, or B: stay with him")
                    answer10 = input()
                if answer10 == ("A") or answer10 == ("a"):
                    print ("*Bananaman sacrifices himself, but you find the brown mark and, upon kicking it,",answer5,"slumps to the ground, dead.*")
                    print ("CONGRATULATIONS! YOU WIN!")
                    quit()
                elif answer10 == ("B") or answer10 == ("b"):
                    print ("You stay with Bananaman, and are plucked from the sky and eaten up in one gulp.*")
                    print ("YOU LOSE")
                    quit()
    elif answer1 == ("no") or answer1 == ("No"):
        print ("Ok, bye then")
        print ("*Bananaman flies off into the distance...*")
        quit()
