import random
import sys
b = True
while b:
    rand1 = random.randint(1, 3)
    rand2 = random.randint(1, 3)
    if rand1 + rand2 == 2 or rand1 + rand2 == 4 or rand1 + rand2 == 6:
        print("Going outside, you see a singuler honeybee polinating a singuler flower")
        randchoice = input(" You decide to (1) approach the singular honeybee (2) Hope to god you don't need to approach the singular bee")
        if randchoice == "1":
            print("A massive horde of singular honeybees ambush you from all angles. In shock you struggle to retreat. You get impaled by the shear force of the honeybee's stings and submit to the honeybee hordes")
            print("By sheer chance of deus ex machina you get a chance to fix your mistakes")
        else:
            print("You reroll... may the RNG Gods bless you")
            pass
    elif rand1 + rand2 == 1 or rand1 + rand2 == 3:
        print("Going outside you feel blessed that there are no creatures on site, however we regret to inform you that you no longer have access. Please grab an admin to debug.")
        sys.exit()
    elif rand1 + rand2 == 5:
        print("WOAH you actually got the 1 in 6 chance to get this special super duper ending... umm you win taadaaaaaaaaaaa ples gib 100%")
        sys.exit()