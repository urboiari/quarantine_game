import time
import random
import sys
# PLAYER VARIABLES
inventory = []
seconds = 1.5
knowledge = 0
visit = 1

# BATTLE VARIABLES
defense = 0
health = 10 + defense
cleanliness = 0
damage = 5
self_isolate = "no"

# FRIEND RANDOMIZER
friends = ["Steve", "Ameer", "Charissa", "Ehecatl",
           "Abril", "Syd", "Brandon", "Katherine",
           "Jason", "Saad", "Mei", "Daniel", "Sam"]
friend = random.choice(friends)


# COLOR TEXT
def red_text_bold(m):
    print("\033[1;91m{}\033[00m" .format(m))
    time.sleep(seconds)


def red_text(m):
    print("\033[91m{}\033[00m" .format(m))
    time.sleep(seconds)


def blue_text(m):
    print("\033[34m{}\033[00m" .format(m))
    time.sleep(seconds)


def purp_text(m):
    print("\033[95m{}\033[00m" .format(m))
    time.sleep(seconds)


def green_text(m):
    print("\033[32m{}\033[00m" .format(m))
    time.sleep(seconds)


# PRINT FUNCTIONS
def narrate(m):
    print(m)
    time.sleep(seconds)


def narrate_quick(m):
    print(m)
    time.sleep(seconds / 2)


# SETTING FUNCTIONS
def back():
    narrate("You head back to the living room.")
    living_room()


def game_over():
    narrate("You have been defeated.")
    choice = input("Play again?(y/n)\n")
    if choice == "y":
        play()
    else:
        time.sleep(1)
        exit()


def win():
    narrate("You won!")
    choice = input("Play again?(y/n)\n")
    if choice == "y":
        play()
    else:
        time.sleep(1)
        exit()


# ENCOUNTER ENGINE
def encounter_chance(knowledge):
    if knowledge == 10:
        return "no"
    elif knowledge == 5:
        chance = random.choice([1, 0])
        if chance == (1):
            return "yes"
        else:
            return "no"
    else:
        return "yes"


# BATTLE OPTIONS
def wash_hands():
    global cleanliness
    narrate("You washed your hands")
    green_text("Cleanliness +1")
    cleanliness += 1


def drink_water():
    global health
    narrate("You drank plenty of water")
    green_text("Health +2")
    health += 2


def sanitize():
    global cleanliness
    narrate("You used the hand sanitizer that "
            + friend + " gave you.")
    green_text("Cleanliness +5")
    cleanliness = 5


def self_iso():
    global damage
    global self_isolate
    narrate("You self isolated")
    narrate("The virus now does less damage")
    damage -= 2
    self_isolate = "yes"


# BATTLE ENGINE
def fight(action):
    if action == "1":
        wash_hands()
    elif action == "2":
        drink_water()
    elif action == "3":
        self_iso()
    elif action == "4":
        if "sanitizer" in inventory:
            sanitize()
        else:
            battle_options()
    else:
        battle_options()


def fight2(action):
    if action == "1":
        wash_hands()
    elif action == "2":
        drink_water()
    elif action == "3":
        if "sanitizer" in inventory:
            sanitize()
        else:
            battle_options()
    else:
        battle_options()


def battle_options():
    global self_isolate
    global health
    global cleanliness
    global damage
    global friend
    if self_isolate == "no":
        options = ("1. Wash your hands\n"
                   "2. Drink Water\n"
                   "3. Self Isolate\n")
        if "sanitizer" in inventory:
            options = options + "4. Use hand sanitizer\n"
        action = input(options)
        fight(action)
    else:
        options = ("1. Wash your hands\n"
                   "2. Drink Water\n")
        if "sanitizer" in inventory:
            options = options + "3. Use hand sanitizer\n"
        action = input(options)
        fight2(action)


# BATTLE SEQUENCE
def battle():
    global defense
    global self_isolate
    global health
    global cleanliness
    global damage
    narrate("On your way, you didn't follow the pandemic "
            "safety guidelines and the virus has attacked you!")
    cleanliness = 0
    while cleanliness < 5:
        print("Health: " + str(health))
        print("Cleanliness: " + str(cleanliness))
        narrate("What will you do?")
        battle_options()
        red_text("You lose " + str(damage) + " health from the sickness.")
        health -= damage
        if health <= 0:
            narrate("The sickness has taken over your body.")
            game_over()
    narrate("You managed to wash away the virus!")


# INTRO
def intro():
    narrate("You are in your room, sitting on your bed "
            "and staring out the window.")
    narrate("It's been 2 months since the pandemic hit.")
    narrate("You miss the outdoors.")
    narrate("The cool air on your skin.")
    narrate("Your friends.")
    narrate("You sigh and lay down on your bed, wondering "
            "how you will spend your day.")
    narrate("...")
    red_text_bold(name.upper() + "!!!!!")
    narrate("Your mother yells at you from the living room.")
    ignore_mother()


def ignore_mother():
    choice = input("Do you ignore her?(y/n)\n")
    if choice == "y":
        narrate("You cover your ears with your pillow "
                "and decide not to respond.")
        narrate("Suddenly you hear angry footsteps coming up the stairs...")
        narrate_quick("THUMP!")
        narrate_quick("THUMP!!")
        narrate("THUMP!!!")
        narrate("Your door swings open, standing there in the frame "
                "is your furious mother.")
        red_text_bold(name.upper() + ", HOW DARE YOU NOT ANSWER!!!")
        red_text_bold("YOU ARE GROUNDED FOR LIFE!!!")
        game_over()
    elif choice == "n":
        purp_text("WHAT, MOM.")
        narrate("You yell back at her from your room.")
        red_text_bold("WE ARE OUT OF TOILET PAPER!")
        narrate("Oh brother, sounds like I'm gonna have to "
                "head to Safeway again.")
        narrate("You get up off your bed and make your "
                "way down the stairs to the living room.")
    else:
        ignore_mother()


# CLOSET
def closet():
    global defense
    narrate("You waddle over to the closet and open it.")
    narrate("It's too dark to see anything!")
    if "flashlight" in inventory:
        narrate("You turn on the flashlight.")
        if "facemask" and "remote" in inventory:
            narrate("It doesn't look like there's "
                    "anything left to find in here.")
        elif "facemask" in inventory:
            narrate("You suspect that there might be "
                    "something more in here...")
            keep_digging()
        else:
            narrate("Dust particles float around as "
                    "you rummage through the muck.")
            narrate("In the filth, you find an old Spongebob "
                    "facemask from your 13th birthday.")
            narrate("You put it on and it still fits.")
            inventory.append("facemask")
            green_text("+10 defense")
            defense += 10
            keep_digging()
    else:
        narrate("You remember that your mom keeps a flashlight "
                "in the garage.")
    back()


def keep_digging():
    choice = input("Keep searching?(y/n)\n")
    if choice == "y":
        narrate("You continue to claw through the dark "
                "and dingy closet.")
        narrate("In a crevice between some boxes, you find "
                "the lost remote for the TV.")
        inventory.append("remote")
        green_text("+1 TV Remote")
    elif choice == "n":
        return
    else:
        keep_digging()


# TELEVISION
def tv():
    global knowledge
    narrate("You sit down on the couch to watch some TV.")
    if "remote" in inventory:
        if knowledge == 0:
            narrate("Using the remote you found,"
                    "you switch to the local news channel.")
            blue_text("To stay safe during the pandemic, "
                      "follow these guidelines:")
            blue_text("1. Wash your hands often!")
            blue_text("2. Don't touch your face!")
            blue_text("3. Stay six feet apart from others!")
            narrate("I guess you learn something new everyday.")
            green_text("+5 Disease Prevention Knowledge")
            knowledge += 5
            watch_more()
        elif knowledge == 5:
            narrate("The local news is still on...")
            watch_more()
        else:
            narrate("As you flip through channels you realize "
                    "that there is nothing to watch.")
    else:
        narrate("You can't find the remote to turn it on.")
        narrate("Maybe you should look around the house.")
    back()


def watch_more():
    global knowledge
    choice = input("Keep watching?(y/n)\n")
    if choice == "y":
        blue_text("There are over 80,000 confirmed cases of "
                  "the virus, and the number continues to climb!")
        blue_text("We urge you all to stay at home and only go out "
                  "when necessary!")
        blue_text("Please be vigilant and stay healthy!")
        green_text("+5 Disease Prevention Knowledge")
        knowledge += 5
        narrate("The news channel starts playing a documentary about "
                "the rise and fall of the fax machine")
        back()
    elif choice == "n":
        return
    else:
        watch_more()


# FACETIME
def facetime():
    global friend
    narrate("You go to your room to "
            "call your friend " + friend + ".")
    narrate_quick("'ring'")
    narrate_quick("'ring'")
    narrate_quick("'ring'")
    if "sanitizer" in inventory:
        narrate("Hmm, no answer")
    else:
        blue_text("What's up " + name + "!")
        blue_text("Thanks for calling me up, I've actually "
                  "been meaning to hit your line.")
        blue_text("I've been worried about you, so I decided "
                  "to ship some hand sanitizer to your doorstep.")
        blue_text("Also, if you're going to Safeway anytime soon, "
                  "I heard that the line is massive.")
        blue_text("But people say that the employee at the front "
                  "loves McDonalds™.")
        blue_text("Anyways, that's all. See ya!")
        narrate("You check your doorstep and find an Amazon "
                "package with hand sanitizer inside.")
        inventory.append("sanitizer")
        green_text("+1 Hand Sanitizer")
        narrate("How nice of " + friend + "!")
    back()


# GARAGE
def garage():
    narrate("You head to the garage.")
    if "flashlight" in inventory:
        narrate("It still smells musty, and you'd rather not "
                "be here.")
    else:
        narrate("Upon entry, the smell of dirty underwear and dog food "
                "smacks you in the face.")
        narrate("You look through the first drawer and pick up "
                "the flashlight inside.")
        green_text("+1 Fleshlight")
        narrate("...")
        narrate("You put it back and wash your hands.")
        red_text("-1 Fleshlight")
        narrate("You check some more drawers and find an actual flashlight.")
        green_text("+1 Flashlight")
        inventory.append("flashlight")
    back()


# SAFEWAY
def safeway():
    global knowledge
    global visit
    narrate("You decide to walk to safeway.")
    encounter = encounter_chance(knowledge)
    if encounter == "no":
        narrate("You follow the pandemic safety guidelines "
                "on your walk and arrive safely.")
    elif encounter == "yes":
        battle()
    narrate("You arrive and immediately notice the three block "
            "long line in front of the store.")
    narrate("There is a man by the doors letting people in, "
            "a few at a time.")
    if "facemask" in inventory:
        if "bigmac" in inventory:
            blue_text("Is that a Big Mac!")
            narrate("The man seems to be filled with joy.")
            blue_text("Thank you so much! Go right on in.")
        else:
            if visit == 1:
                blue_text("Hey, you!")
                narrate("The man barks at you.")
                blue_text("I've been here all day tending to this line and "
                          "I haven't had a chance to eat.")
                blue_text("If you get me something to eat, "
                          "I'll cut you through the line!")
                narrate("You keep the man's offer in mind.")
                visit += 1
            elif visit == 2:
                narrate("The man looks at you with sad eyes.")
                blue_text("You still don't have my food?")
            wait()
        congrats()
    else:
        narrate("The man looks at you.")
        blue_text("Sorry sir, we can't let you in without a facemask.")
        narrate("How could you forget?!")
        back()


def wait():
    choice = input("Will you wait in line?(y/n)\n")
    if choice == "y":
        narrate("You head to the back of the line to wait.")
        line()
    elif choice == "n":
        narrate("You decide that the line is too long "
                "and go back home.")
        living_room()
    else:
        wait()


def line():
    global seconds
    for s in range(5):
        for k in range(10):
            print(".")
            time.sleep(1)
        exit_line()
    narrate("You finally reach the front of the line and the "
            "man lets you in.")


def exit_line():
    choice = input("Will you leave in line?(y/n)\n")
    if choice == "y":
        narrate("You decide that the line is too long "
                "and go back home.")
        living_room()
    elif choice == "n":
        narrate("You continue to wait.")
    else:
        exit_line()


def congrats():
    narrate("You find your way to the toilet paper and "
            "grab a pack.")
    narrate("Wasting no time, you pay for it at the check out "
            "and return home.")
    narrate("Your mother thanks you, and you go upstairs.")
    narrate("You sit on your bed and stare out the window.")
    narrate("It's gonna be a long year.")
    win()


# MCDONALDS
def mcdonalds():
    narrate("You drive to McDonalds™ to get some food.")
    narrate("They are only open for take out.")
    narrate("You purchase a Big Mac.")
    green_text("+1 Big Mac")
    inventory.append("bigmac")
    narrate("Mmmmmmmmm, yummy!")
    back()


# LIVING ROOM
def living_room():
    narrate("What do you do now?")
    select = input("1. Check the closet\n"
                   "2. Watch some TV\n"
                   "3. Facetime a friend\n"
                   "4. Look through the garage\n"
                   "5. Head to Safeway\n"
                   "6. Go to McDonalds™\n")
    if select == "1":
        closet()
    elif select == "2":
        tv()
    elif select == "3":
        facetime()
    elif select == "4":
        garage()
    elif select == "5":
        safeway()
    elif select == "6":
        mcdonalds()
    else:
        living_room()


# PLAY FUNCTION
def play():
    intro()
    living_room()


name = input("What is your name?\n")
time.sleep(1)
play()
