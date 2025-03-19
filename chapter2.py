# chapter2.py

import random

class StPatricksDayRealm:
    def __init__(self):
        self.realm_name = "St. Patrick's Day Realm"

    def start(self):
        print(f"\nYou step through the portal and arrive in a lush, green Irish village.")
        print("The sky is gray, and rainbows seem faded. The leprechauns look distressed.")
        
        choice = input("Do you approach the leprechauns and ask what's wrong? (y/n): ").lower()
        
        if choice == 'y':
            print("\nYou approach the village square where a group of leprechauns have gathered.")
            self.villager_interaction()
        else:
            print("\nYou wander around but sense a strange, unlucky aura everywhere.")
            print("Eventually, curiosity gets the best of you, and you return to the village.")
            self.villager_interaction()

    def villager_interaction(self):
        npc_name = random.choice(["Finnigan", "Clover", "Seamus", "Lucky"])
        
        print(f"\n{npc_name}: Top o’ the mornin’ to ya, traveler! We have a problem—the rival leprechaun clan stole our pot of gold!")
        print("Without it, our village is losing luck, and the rainbows are fading!")
        
        answer = input("Will you help us recover our pot of gold? (y/n): ").lower()
        
        if answer == 'y':
            print(f"\n{npc_name}: You’re a true friend! But be careful, the tricksters have set up traps!")
            self.journey_to_find_gold()
        else:
            print(f"\n{npc_name}: Oh dear, without our gold, bad luck may follow us forever…")
            print("You hesitate, but deep down, you feel like you should help. You turn back.")
            self.journey_to_find_gold()

    def journey_to_find_gold(self):
        print("\nYou follow a winding path out of the village, determined to retrieve the pot of gold.")

        # Challenge 1: Lucky Forest Maze
        print("\nA thick mist surrounds you as you enter the Lucky Forest. You must find the right path through the maze!")
        self.lucky_forest_maze()

        # Challenge 2: Riddle Challenge
        print("\nAfter escaping the maze, an old leprechaun blocks your path.")
        print("'Only those who can solve my riddles may pass,' he cackles.")
        self.riddle_challenge()

        # Challenge 3: Trickster Leprechauns’ Hideout
        print("\nYou reach the Trickster Leprechauns' hideout, where the pot of gold is hidden.")
        self.trickster_hideout()

        # Restoring the pot of gold
        print("\nYou return the pot of gold to the village, and suddenly the sky brightens!")
        print("Rainbows shine in the sky, and the town’s luck is restored!")
        print("\nThe leprechauns cheer, and you feel a warm glow as magic surrounds you...")
        print("The portal reappears, ready to take you to your next adventure!")

    def lucky_forest_maze(self):
        choices = ["Left", "Right", "Forward"]
        
        for _ in range(3):
            move = input("Which direction do you choose? (Left/Right/Forward): ").capitalize()
            correct_path = random.choice(choices)
            
            if move == correct_path:
                print("You found the correct path and escaped the forest!")
                return
            else:
                print("The mist thickens, and you feel lost. Try again!")
        print("After wandering for a while, you finally find the right path.")

    def riddle_challenge(self):
        riddles = [
            {"question": "What has hands but can’t clap?", "answer": "Clock"},
            {"question": "I am always running but never move. What am I?", "answer": "River"},
            {"question": "The more you take, the more you leave behind. What am I?", "answer": "Footsteps"}
        ]
        
        riddle = random.choice(riddles)
        answer = input(f"\nRiddle: {riddle['question']} ").capitalize()
        
        if answer == riddle["answer"]:
            print("The leprechaun nods. 'You may pass!'")
        else:
            print(f"The leprechaun smirks. 'Wrong! The answer was {riddle['answer']}! But I’ll let you pass anyway.'")

    def trickster_hideout(self):
        print("\nYou sneak into the Trickster Leprechauns' hideout and see the pot of gold guarded by traps.")
        
        traps = ["Fake Gold Decoy", "Magic Net", "Pitfall Trap"]
        trap = random.choice(traps)
        
        print(f"\nOh no! A {trap} is in your way!")
        
        if trap == "Fake Gold Decoy":
            choice = input("Do you examine the gold closely before grabbing it? (y/n): ").lower()
            if choice == 'y':
                print("You notice the fake gold and avoid the trap!")
            else:
                print("The gold turns to dust in your hands, but luckily, the real pot is nearby!")

        elif trap == "Magic Net":
            choice = input("Do you use a lucky charm to escape the net? (y/n): ").lower()
            if choice == 'y':
                print("Your charm glows, breaking the spell!")
            else:
                print("You struggle for a while before wriggling free.")

        elif trap == "Pitfall Trap":
            choice = input("Do you test the ground before stepping forward? (y/n): ").lower()
            if choice == 'y':
                print("You find a hidden plank and safely cross!")
            else:
                print("You fall in but manage to climb out using vines!")

        print("\nYou grab the pot of gold and run back to the village!")
