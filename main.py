import chapter1
import chapter2
import chapter3  # Easter Realm
import chapter4  # Haunted Forest Realm
import chapter5  # Thanksgiving Realm

def start_game():
    while True:
        print("\nWelcome to the Holiday Adventure Game!")
        print("1. Christmas Realm")
        print("2. St. Patrick's Day Realm")
        print("3. Easter Realm")
        print("4. Haunted Forest Realm")
        print("5. Thanksgiving Realm")
        print("6. Quit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            game = chapter1.ChristmasRealm()  # Create an instance of ChristmasRealm
            game.start()  # Start the game for Chapter 1
        elif choice == '2':
            game = chapter2.StPatricksDayRealm()  # Create an instance of StPatricksDayRealm
            game.start()  # Start the game for Chapter 2
        elif choice == '3':
            game = chapter3.EasterRealm()  # Create an instance of EasterRealm 
            game.start_game()  # Start the EasterRealm adventure
        elif choice == '4':
            game = chapter4.HauntedForestRealm()  # Create an instance of HauntedForestRealm
            game.start_game()  # Start the Haunted Forest adventure
        elif choice == '5':
            game = chapter5.ThanksgivingRealm()  # Create an instance of ThanksgivingRealm 
            game.start_game()  # Start the Thanksgiving adventure
        elif choice == '6':
            print("Thank you for playing! Goodbye!")
            break  # Exit the game
        else:
            print("Invalid choice! Please choose a valid option.")

if __name__ == "__main__":
    start_game()





