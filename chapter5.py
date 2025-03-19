import random
import time

class ThanksgivingRealm:
    def __init__(self):
        self.ingredients = []

    # Function to enter the Thanksgiving Realm
    def enter_thanksgiving_realm(self):
        print("\nYou step through the portal and find yourself in a quaint village surrounded by golden fields and orchards.")
        print("The air smells like fall, with pumpkins and turkeys scattered around the town.")
        print("But something is wrong. The crops aren't growing, and the villagers are worried about the harvest.")
        
        choice = input("Do you want to speak with the villagers about the harvest? (y/n): ").lower()
        
        if choice == 'y':
            print("\nYou approach the village square, where the villagers are gathered, looking concerned.")
            self.villager_interaction()
        else:
            print("\nYou decide to explore the town to gather more clues about what's happening with the harvest.")
            self.investigate_mystery()

    # Function for villager interaction
    def villager_interaction(self):
        print("\nVillager: 'Our crops aren't growing, and the weather keeps changing. We don't know what to do!'")
        print("Another villager approaches you.")
        
        print("Villager: 'We believe something magical is interfering with the harvest. Can you help us restore the crops?'")
        
        answer = input("Will you help us restore the harvest? (y/n): ").lower()
        
        if answer == 'y':
            print("\nVillager: 'Thank you, traveler! We need your help to gather some ingredients and figure out how to fix the weather.'")
            self.gather_ingredients()
        else:
            print("\nVillager: 'Please, reconsider. The harvest is our only hope for a successful feast.'")
            self.gather_ingredients()

    # Function to gather ingredients for the harvest
    def gather_ingredients(self):
        print("\nTo restore the harvest, you need to gather special ingredients from around the village.")
        print("The villagers believe that the weather can be controlled with a special ritual.")
        
        # Ingredient gathering process
        ingredients = ["Golden Apples", "Autumn Leaves", "Pumpkin Spice", "Mystical Corn"]
        
        print("\nYou head out to gather the ingredients.")
        
        for ingredient in ingredients:
            print(f"\nYou search for {ingredient}.")
            found = random.choice([True, False])
            
            if found:
                print(f"You found {ingredient}!")
                self.ingredients.append(ingredient)
            else:
                print(f"You couldn't find {ingredient} this time. You need to keep searching.")
        
        print("\nYou have gathered the ingredients needed for the ritual.")
        self.perform_ritual()

    # Function to perform the ritual to restore the harvest
    def perform_ritual(self):
        print("\nWith the ingredients in hand, you head to the village square, where the villagers have prepared for the ritual.")
        print("A magical circle is drawn on the ground, and the air is thick with tension as you prepare to perform the ritual.")
        
        # Ritual puzzle: The player must perform a simple puzzle or pattern matching
        print("\nTo perform the ritual, you must arrange the ingredients in the correct order.")
        ritual_order = random.sample(["Golden Apples", "Autumn Leaves", "Pumpkin Spice", "Mystical Corn"], 4)
        print("Arranged ingredients:", ritual_order)
        
        choice = input("What is the correct order to complete the ritual? (e.g., Golden Apples, Autumn Leaves, Pumpkin Spice, Mystical Corn): ")
        
        if choice == ', '.join(ritual_order):
            print("\nThe ritual is a success! The weather stabilizes, and the crops begin to grow again.")
            self.celebrate_thanksgiving()
        else:
            print("\nThe ritual fails. The crops are still withered, and the villagers remain anxious.")
            self.gather_ingredients()  # Retry gathering ingredients

    # Function to celebrate Thanksgiving
    def celebrate_thanksgiving(self):
        print("\nWith the harvest restored, the villagers prepare for a grand Thanksgiving feast.")
        print("You are invited to join the feast, where you are thanked for your help in saving the village.")
        print("\nVillager: 'Thank you, traveler, for helping us restore the harvest. Our feast will be bountiful this year.'")
        
        # Player receives a token
        print("\nAs a token of gratitude, the villagers give you a magical harvest token. You can feel the warmth of the harvest in your hands.")
        
        # Portal to the next chapter
        print("\nA portal appears before you, glowing with the colors of autumn, guiding you to your next adventure...")
        print("You step through the portal, ready to face the next challenge in your journey.")

    # Start the game
    def start_game(self):
        print("Welcome, Lost Traveler! Your adventure begins now.")
        self.enter_thanksgiving_realm()
