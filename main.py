from UserManagement import User_Management
from SimpleBruteForceAttack import Simple_Brute_Force, Count_tracking_Simple_Brute_Force
from DictionaryAttack import DictionaryAttack
from HybridAttack import HybridAttack

user_database_file = "C:\\Python Introduction to Cybersecurity\\Project Brute\\user_database.txt"

try:
    um = User_Management(user_database_file)
    simple = Simple_Brute_Force(um)
    count = Count_tracking_Simple_Brute_Force(um)
    dict_attack = DictionaryAttack(um)
    hybrid = HybridAttack(um)

    while True:
        print("\n---Brute Force Attack Simulator---")
        print("1. User Management")
        print("2. Full Simple BruteForce Attack")
        print("3. Simple BruteForce Attack with Attempt Count")
        print("4. Dictionary Attack")
        print("5. Hybrid Attack")
        print("6. Exit")

        try:
            choice = int(input("\nEnter your choice: "))

            if choice == 1:
                um.menu()
            elif choice == 2:
                simple.crack()
            elif choice == 3:
                count.crack()
            elif choice == 4:
                dict_attack.crack()
            elif choice == 5:
                hybrid.crack()
            elif choice == 6:
                print("Exiting program. Goodbye!")
                break
            else:
                print("Invalid choice! Please enter a number between 1-6.")

        except ValueError:
            print("Error: Please enter a valid number.")
        except KeyboardInterrupt:
            print("\n\nProgram interrupted by user.")
            break
        except Exception as e:
            print(f"Error: An unexpected error occurred - {e}")

except FileNotFoundError:
    print("Error: User database file not found.")
    print("Please ensure the file exists at the specified path.")
except Exception as e:
    print(f"Error: Failed to initialize program - {e}")