# easter_realm.py

import random

class EasterRealm:
    def __init__(self):
        self.eggs_found = 0

    # Function to enter the Easter Realm
    def enter_easter_realm(self):
        print("\nYou step through the portal and arrive in a beautiful enchanted garden.")
        print("The air smells like spring, and colorful eggs are hidden throughout.")
        print("But something seems off... the Easter Bunny looks worried.")

        choice = input("Do you approach the Easter Bunny to ask what's wrong? (y/n): ").lower()

        if choice == 'y':
            print("\nYou walk up to the Easter Bunny, who looks distressed.")
            self.bunny_interaction()
        else:
            print("\nYou wander around but notice the garden feels unusually empty.")
            print("Eventually, you spot the Easter Bunny and decide to talk.")
            self.bunny_interaction()

    # Function for Easter Bunny interaction
    def bunny_interaction(self):
        print("\nEaster Bunny: Oh no, traveler! My magical eggs have been stolen!")
        print("Without them, the grand Easter parade cannot happen!")

        answer = input("Will you help find the missing eggs? (y/n): ").lower()

        if answer == 'y':
            print("\nEaster Bunny: Thank you! But beware, a rogue bunny is causing trouble.")
            self.egg_hunt_challenge()
        else:
            print("\nEaster Bunny: Without your help, Easter may never be the same...")
            print("You hesitate, but the thought of a ruined Easter parade changes your mind.")
            self.egg_hunt_challenge()

    # Egg Hunt Mini-game
    def egg_hunt_challenge(self):
        print("\nYou begin searching the garden for missing eggs hidden in bushes and behind trees.")
        
        locations = ["Under a bush", "Behind a tree", "Near a pond", "Inside a flower bed"]

        for _ in range(3):
            print("\nYou look around and spot something...")
            location = random.choice(locations)
            find_egg = input(f"Do you check {location}? (y/n): ").lower()

            if find_egg == 'y':
                print(f"You found a hidden egg at {location}!")
                self.eggs_found += 1
            else:
                print("You ignore it and keep searching...")

        if self.eggs_found >= 2:
            print("\nYou found enough eggs, but some are still locked in magical chests!")
            self.color_pattern_puzzle()
        else:
            print("\nYou haven't found enough eggs! Keep looking.")
            self.egg_hunt_challenge()

    # Color & Pattern Puzzle Mini-game
    def color_pattern_puzzle(self):
        print("\nYou find some eggs inside a glowing chest, but it won’t open!")
        print("The chest has a puzzle: Match the correct colors and patterns to unlock it.")

        patterns = ["Stripes", "Polka Dots", "Swirls"]
        colors = ["Blue", "Pink", "Yellow"]

        correct_pattern = random.choice(patterns)
        correct_color = random.choice(colors)

        guess_pattern = input(f"Choose a pattern ({patterns}): ").title()
        guess_color = input(f"Choose a color ({colors}): ").title()

        if guess_pattern == correct_pattern and guess_color == correct_color:
            print("\nThe chest glows and opens! You collect the magical eggs!")
            self.rogue_bunny_encounter()
        else:
            print("\nThe chest remains locked... Try again!")
            self.color_pattern_puzzle()

    # Rogue Bunny Encounter Mini-game
    def rogue_bunny_encounter(self):
        print("\nAs you collect eggs, a mischievous bunny hops in front of you, snatching an egg!")
        print("Rogue Bunny: 'Catch me if you can!'")

        attempts = 3
        while attempts > 0:
            action = input("\nDo you chase (run) or try to outsmart the bunny (trick)? ").lower()

            if action == "trick":
                print("\nYou pretend to look away, and when the bunny lets its guard down, you grab the egg!")
                break
            elif action == "run":
                if random.choice([True, False]):
                    print("\nYou sprint after the bunny and snatch the egg back!")
                    break
                else:
                    print("\nThe bunny is too fast! Try another way.")
                    attempts -= 1
            else:
                print("Invalid choice. Try again.")
        
        print("\nWith all the eggs recovered, you return to the Easter Bunny!")
        self.restore_eggs()

    # Restoring the Easter Eggs
    def restore_eggs(self):
        print("\nYou return the eggs to the Easter Bunny, and suddenly, the garden glows with magic!")
        print("The Easter parade is saved, and the bunny rewards you with a special token!")
        print("\nA portal appears, leading you to your next adventure...")

    # Start the game
    def start_game(self):
        print("Welcome, Lost Traveler! Your next adventure begins now.")
        self.enter_easter_realm()
