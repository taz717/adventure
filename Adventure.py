'''
Moataz Khallaf
20/9/2018
Adventure
'''
import time
import sys
import random
###Variables
start = 0
choice1 = 0
choice2 = 0
choice3A = 0
choice4A = 0 ##this was just used to debug some code. I still don't know if it helps or not
choice4C = 0
##subroutines 
def intro():
    print("Hello this is a virtual reality game you are playing. Please take off your headset. Syke these are just your glasses.")
    
def kitchen():
    print(" The kitchen is tiled with a series of red and grey tiles in the shape of a bird. The cupboards are made out of maple and the counter is black marble.")
    time.sleep(2)
    print("The perimeter is engulfed with counters along with a semi circuler island in the middle.")
    time.sleep(2)
    print("Under a window there is an electric oven powerd by the water mill just outside")
    time.sleep(2)
    print("Above the counters, about a meter high are a series of cupboards stocked with fresh apples (heal 1 hp) and cheese wheels (heal 2 hp)")
    kitchenchoice = input(" (1) Grab an apple (2) Grabe a cheese wheel (3) ")
    if kitchenchoice == "1" or kitchenchoice == "2":
        print("You grab an object and the rest come crumbling down on you. You slowly suffocate unable to move the cornacopia of food")
        print("Wow you actually died from a poorly stacked pile of odd foods. Serves you right to want to know details...")    

def randscene():##random encounter scene because ples gib 100%
    b = True
    while b:
        rand1 = random.randint(1, 3)
        rand2 = random.randint(1, 3)
        if snap == 1 and choice2 == 2:
                        print("RNG simply isn't in your favour.") ## the choice2 path was made to be serious but I wantyou to be able to reach this part from any choice path
        if rand1 + rand2 == "2" or rand1 + rand2 == "4" or rand1 + rand2 == "6":
            print("Going outside, you see a singuler honeybee polinating a singuler flower")
            randchoice = input(" You decide to (1) approach the singular honeybee (2) Hope to god you don't need to approach the singular bee" )
            if randchoice == "1":
                print("A massive horde of singular honeybees ambush you from all angles. In shock you struggle to retreat. You get impaled by the shear force of the honeybee's stings and submit to the honeybee hordes")
                b == False
            else:
                print("You reroll... may the RNG Gods bless you")
                pass
        elif rand1 + rand2 == "1" or rand1 + rand2 == "3":
            print("Approaching the door, You have feel somewhat blessed for there are no bees in the proximity, however we regret to inform you that you no longer have access. Please grab an admin to debug.")
            sys.exit()
        else:
            print("WOAH you actually got the 1 in 6 chance to get this special super duper ending... umm you win taadaaaaaaaaaaa ples gib 100%")
            sys.exit()
def cheekybeeky2():
    print("you still don't get this do you? Screw it sys.exit() have a good day sir")
    sys.exit()
## WE DON'T TAKE ANSWERS OTHER THAN 1 2 OR 3
def cheekybeeky():
    print("Wow cool guy. You should probably know we don't accept anything other than 1, 2 or 3")
    time.sleep(1)
    print("Ok ... you are telaported 50ft above your house... ")
    print("You spread your body as wide as possible to grab as much drag as you can. It's not working man")
    cheeky = input("(1) You try flying like the birds do (2) you baptise yourself and pray to god you don't die (3) You wonder how you have enough time to baptise yourself or how you even got the water to do it. ")
    if cheeky == "1" or cheeky == "2" or cheeky == "3":
        print("lol no you dead bro.")



###GAME TIME
play = True
while play:
    intro()
    time.sleep(1) ## all of these is to pretty much just make sure you aren't overwhelmend by the literal wall of text that's ocming
    start = input("Press 1 to start and 2 to exit ")
    if start == "2":
        sys.exit() ##start screen essentially.
    else:
        pass
    
    print("You wake up in your room.")
    choice1 = (input("You decide to (1) go back to bed (2) Get up and start the morning routine: ")) ##lol please this is just scene 1
    
    if choice1 == "1":
        print("sleepy boi hours goodnight.")
        time.sleep(3)
        sys.exit()
    elif choice1 == "2":
        print("You get up, walk straight to the kitchen and observe") ##scene 2 or like when actual choices matter
        print("You see ...")
        time.sleep(2)
        choice2 = input("(1) dishes in the sink (2) an empty quiver on the kitchen counter (3) nothing and decide you need more details on how the kitchen looks ")
    
    
    
        if choice2 == "3":
            kitchen()
        
        elif choice2 == "1":
            print("Wow the sink is piled up from last night's dinner.")
            time.sleep(1)
            print("You feel that you should leave it for the afternoon though")
            choice3A = input(" (1) to force yourself to do the dishes (2) go outside to get some fresh air trying to recollect what happened last night (3) get a detailed observation of how the kitchen look ")
         

            if choice3A == "1":
                print("Wow you are sooo cool. Doing the dishes is soo the reason I play video games too...")
                time.sleep(2)
                print(".... I just broke the 4th wall...")
                print("I'm sorry have fun with your dishes")
            elif choice3A == "2":
                randscene()
            elif choice3A =="3":
                kitchen()

            elif choice3A != "1" and choice3A != "2" and choice3A != "3":
                cheekybeeky()

        elif choice2 == "2":
            print("As you approach the empty quiver, you spot inside of it")
            print('"Nice job on the last dungeon, hope you are feeling well"-Dash')
            print("you spot three gold coins deeper inside the quiver")
            print("flashbacks of last night start to imerge")
            choice4A = input("Dark ... room ... running ... quiver's empty ... (1) snap out of it (2) reach for your dagger ")

            if choice4A == "1":
                randscene()

            elif choice4A == "2":
                print("You reach for your dagger. A sudden roar emerges from behind chilling you to your very core")
                print('''"behind you!" as you turn your head a giant bear knocks you over. it's massive body easily sends you to the other side of the room''')
                print('''You stumble to get up and grab a somewhat firm hold of your dagger. The bear looking enraged stands on it's hind legs infront of you''')
                choice4B = input("(1) Slowly edge your way to the wall (2) leap into the bear's belly with your dagger pointed at him ")

                if choice4B != "1" and choice4B != "2" and choice4B != "3":
                    cheekybeeky()

                if choice4B == "1":
                    print("As you edge away, the bear simply bites your head clean off and returns to his nest")

                snap = random.randint(1, 2)
                if snap == 1:
                    print("You snap out of it and realize you are simply in your own home again. Wanting fresh air you decide to head out")
                    randscene()
                elif snap == 2:
                    print("The bear not expecting this sudden strike faulters and simply submits defeat as you press your dagger against it's chest ever so harder")
                    print('''"Nice job there lad" You turn to see Dash dusting some dirt off of his shoulder''')
                    choice4C = input('''(1)"Yeah you could've at least tried to help" (2)"All in a days work" (3)"boi" ''')
                    
                    if choice4C != "1" and choice4C != "2" and choice4C != "3":
                        cheekybeeky()

                    if choice4C == "1":
                        print(''' "Yeah I know, but you seemed to have it under control so I figured I should just watch. Anyways I'll just pick up the bounty and give you your share tommorrow"''')
                        print(''' "don't forget to pick up your quiver!"''')
                        time.sleep(2)
                        print("You head back home without listening to dash and pass out on your bed.")
                        print("end")
            
                    elif choice4C == "2":
                        print("yeahhh we aren't even getting paid for the bear man... at least we can sell the pelt... I'll get you your share of the bounty tommorrow")
                        print(''' "don't forget to pick up your quiver!"''')
                        time.sleep(2)
                        print("You head back home without listening to dash and pass out on your bed.")
                        print("end")
    
                    elif choice4C =="3":
                        print("simply not understanding what you just said, Dash simply fires and arrow at it")
                        print(" *hit* as the arrow pierces your heart, you wonder what could've happened if you didn't use modern day slang")
                        print("end")
            
                    elif choice4C != "1" and choice4C != "2" and choice4C != "3":
                        cheekybeeky()
                elif choice4B != "1" and choice4B != "2" and choice4B != "3":
                    cheekybeeky()
            elif choice4A != "1" and choice4A != "2" and choice4A != "3":
                    cheekybeeky()
        elif choice2 != "1" and choice2 != "2" and choice2 != "3":
            cheekybeeky()
    elif choice1 != "1" and choice1 != "2":   ##   --------   /
        cheekybeeky() ## I must complete the rombus ---------/