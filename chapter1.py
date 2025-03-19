# chapter1.py

import time
import random

class ChristmasRealm:
    def __init__(self):
        self.clues = 0
        self.weapons = []
        self.health = 100  # Player starts with full health

    def print_snow_scene(self):
        print("""
          *    *  ()   *   *
        *        * /\         *
             *   /i\\    *  *
           *     o/\\  *      *
                ///\i\    
           *   /*/o\\    *   
         *    /i//\*\      *
              o/*\\i\
        *       \\o/
            *    ||       *
        """)
        time.sleep(1)

    def print_snow_monster(self):
        print("""
           (    )
          ((((()))
          |o\\ /o)|
          ( (  _')
          (._.  /\\__
         ,\\___,/ '  ')
         '.,_'   (  (
             |\\   \\ \\
             | \\   | \\
             | /\\_ | /\\
             |/ /|/ /\\)
             (_/ (_/ 
        """)
        time.sleep(1)

    def gather_clues_and_weapons(self):
        print("\nYou come across three challenges to gather clues and weapons:")
        print("1. Ice Maze Escape")
        print("2. Ice Fishing Challenge")
        print("3. Build a Snowman")

        for _ in range(3):
            challenge = input("Pick a challenge (1/2/3): ")
            if challenge == "1":
                print("You brave the icy maze, but the cold bites at your skin (-10 Health).")
                self.weapons.append("Ice Sword")
                self.clues += 1
                self.health -= 10
            elif challenge == "2":
                print("You fish through a frozen lake, but slip on the ice (-5 Health).")
                self.weapons.append("Ice Crystal")
                self.clues += 1
                self.health -= 5
            elif challenge == "3":
                print("You build a snowman, and it gifts you a snowflake charm for warmth! (+5 Health)")
                self.weapons.append("Snowflake Charm")
                self.clues += 1
                self.health += 5
            else:
                print("You wander aimlessly, feeling the cold seep into your bones (-5 Health).")
                self.health -= 5

            print(f"Current Health: {self.health}\n")
            if self.health <= 0:
                print("You collapsed in the snow... Game Over.")
                exit()

    def fight_snow_monster(self):
        print("\nWith the clues and weapons gathered, you face the snow monster!")
        self.print_snow_monster()

        fight = input("Do you fight the snow monster? (yes/no): ").lower()
        if fight == "yes":
            print("You bravely fight the monster, using your ice sword and charms...")
            if "Ice Sword" in self.weapons:
                print("You slash the monster with your Ice Sword!")
                self.health -= 20
            else:
                print("You fight with your bare hands, taking heavy damage (-40 Health).")
                self.health -= 40

            print(f"Remaining Health: {self.health}")

            if self.health <= 0:
                print("The monster overpowers you... You fall in the snow. Game Over.")
                exit()
            else:
                print("You defeat the monster, and Santa is saved! The village celebrates.")
        else:
            print("You flee into the blizzard, leaving the village's fate unknown.")
        
        print(f"Final Health: {self.health}\n")

    def start(self):
        print("\nWelcome to the Christmas Realm!")
        self.print_snow_scene()
        print(f"You find yourself in a snowy village where Santa has vanished, and the gifts are gone! Your health is {self.health}.")

        choice = input("Do you want to ask the villagers for clues? (yes/no): ").lower()
        if choice == "yes":
            print("The villagers tell you about a fearsome snow monster seen lurking nearby.")
        else:
            print("You decide to search alone, but the blizzard makes it hard to see (-5 Health).")
            self.health -= 5

        print(f"Current Health: {self.health}\n")
        self.gather_clues_and_weapons()
        self.fight_snow_monster()
        print("The portal to the next realm opens...")

if __name__ == "__main__":
    game = ChristmasRealm()
    game.start()




