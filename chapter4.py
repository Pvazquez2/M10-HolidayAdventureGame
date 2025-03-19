import random

class HauntedForestRealm:
    def __init__(self):
        self.ingredients = []  # List to hold magical ingredients

    # Function to enter the Haunted Forest Realm
    def enter_haunted_forest(self):
        print("\nYou step through the portal and find yourself in a dark, haunted forest.")
        print("The trees are twisted, and fog swirls around you, making it difficult to see.")
        print("You hear whispers from the shadows... lost souls, trapped in this cursed place.")
        
        choice = input("Do you want to investigate the eerie sounds? (y/n): ").lower()
        
        if choice == 'y':
            print("\nYou move forward, cautiously, through the fog.")
            self.spirit_interaction()
        else:
            print("\nYou decide to explore deeper into the forest, looking for answers.")
            self.spirit_interaction()

    # Function for spirit interaction
    def spirit_interaction(self):
        print("\nA glowing, translucent figure appears before you.")
        print("Spirit: 'Help us, traveler... We are trapped in this forest by a dark curse!'")
        
        answer = input("Will you help break the curse? (y/n): ").lower()
        
        if answer == 'y':
            print("\nSpirit: 'Thank you, traveler! We can guide you, but you must first solve the witch's puzzles.'")
            self.break_curse_challenge()
        else:
            print("\nSpirit: 'Without your help, we will remain trapped... Please, reconsider.'")
            self.break_curse_challenge()

    # Puzzle to break the curse
    def break_curse_challenge(self):
        print("\nTo break the curse, you must gather magical ingredients hidden in the forest.")
        print("The ingredients are guarded by ancient puzzles that protect the witch's power.")
        
        # Puzzle challenge 1: Riddle
        riddle_answer = input("\nA voice echoes in the forest: 'I speak without a mouth and hear without ears. I have no body, but I come alive with wind. What am I?' ").lower()
        
        if riddle_answer == "echo":
            print("\nCorrect! You gather the first magical ingredient: Echo Dust.")
            self.ingredients.append("Echo Dust")
        else:
            print("\nThat's not the right answer. The voice disappears, and you continue searching.")
        
        # Puzzle challenge 2: Number Puzzle
        print("\nYou come across a stone tablet with a number puzzle.")
        number_puzzle_answer = input("Solve this: 'What is the next number in the sequence: 1, 4, 9, 16, 25? (Hint: It's a perfect square)': ")
        
        if number_puzzle_answer == "36":
            print("\nCorrect! You gather the second magical ingredient: Moonstone Shards.")
            self.ingredients.append("Moonstone Shards")
        else:
            print("\nThat's not the right answer. You continue looking for more clues.")
        
        # Puzzle challenge 3: Memory Game
        print("\nYou see a magical chest with three locked symbols. The chest whispers: 'Remember the pattern.'")
        pattern = random.sample(['🟠', '🔵', '🟢', '🟣'], 3)
        print("The pattern is:", pattern)
        
        # The player has to guess the pattern
        guess = input("Enter the pattern you saw (e.g., 🟠🔵🟣): ")
        
        if guess == ''.join(pattern):
            print("\nCorrect! You gather the third magical ingredient: Spirit Essence.")
            self.ingredients.append("Spirit Essence")
        else:
            print("\nThe chest remains locked, but you can try again later.")

        # If the player has gathered all ingredients
        if len(self.ingredients) == 3:
            print("\nYou have gathered all the ingredients needed to break the curse.")
            self.confront_witch()
        else:
            print("\nYou haven't gathered all the ingredients yet. Keep searching!")
            self.break_curse_challenge()

    # Confront the Witch
    def confront_witch(self):
        print("\nWith the ingredients in hand, you approach the witch’s lair deep in the forest.")
        print("The witch stands before you, her eyes glowing with dark power.")
        
        choice = input("Do you confront the witch or try to sneak past her? (confront/sneak): ").lower()
        
        if choice == "confront":
            print("\nWitch: 'You dare challenge me, traveler? I am the master of this cursed forest!'")
            self.battle_witch()
        elif choice == "sneak":
            print("\nYou try to sneak past the witch, but she senses your presence and catches you!")
            self.battle_witch()
        else:
            print("\nThe witch grows impatient with your hesitation.")
            self.battle_witch()

    # Battle the Witch (Mini-game)
    def battle_witch(self):
        print("\nYou engage in a fierce battle with the witch. She attacks with dark magic!")
        
        # Battle mechanics: Random chance to succeed
        success = random.choice([True, False])
        
        if success:
            print("\nYou successfully use the magical ingredients to break the witch's curse!")
            print("The witch screams and disappears, leaving the forest free of her dark influence.")
            print("The trapped spirits are freed, and the forest begins to glow with light!")
            self.break_the_curse()
        else:
            print("\nThe witch's magic is too strong! You need more power to defeat her.")
            print("You must gather more ingredients before confronting the witch again.")
            self.break_curse_challenge()

    # Breaking the Curse
    def break_the_curse(self):
        print("\nWith the witch defeated and the curse broken, the forest is no longer dark and haunted.")
        print("The trapped spirits thank you for your bravery.")
        print("You have earned a powerful token from the spirits and a clear path to your next adventure!")
        
        # Portal to next chapter
        print("\nA portal appears before you, guiding you to your next journey...")
        print("You step through and prepare for what lies ahead.")

    # Start the game
    def start_game(self):
        print("Welcome, Lost Traveler! Your adventure begins now.")
        self.enter_haunted_forest()


