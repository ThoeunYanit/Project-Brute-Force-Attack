# Simple Brute Force Attack

from UserManagement import *

import itertools
import string


class Simple_Brute_Force:

    def __init__(self, user_database_file): ##change user_management to user manager not use thsi class 
        self.user_manager = user_database_file ##we will take argument from the um (user_management)

    def crack(self):
        char = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
        attempt_count = 0
  
        try :
             self.user_manager.reload_user()
        except FileNotFoundError:
            print("Error: User database file not found.")
            return
        except PermissionError:
            print("Error: Permission denied to access user database.")
            return
        except Exception as e:
            print(f"Error: Failed to load user database - {e}")
            return     

        users = self.user_manager.get_user() #use of instance

        target_user = input("Enter a target username: ")
    

        if target_user not in users:
            print("Target is not available!")
            return
        else :
            target_password = users[target_user]

        
        for length in range(1, len(target_password)+1):
            for combo in itertools.product(char, repeat=length):
                attempt_count += 1
                
                attempt = "".join(combo)
                print(f"Trying {attempt}")

                if attempt == target_password:
                    print(f"User {target_user} : Password FOUND -> {target_password}")
                    print(f"Attempts Count: {attempt_count}")
                    return
        



class Count_tracking_Simple_Brute_Force:

    def __init__(self, user_database_file):
        self.user_manager = user_database_file

    def crack(self):
        char = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation

        attempt_count = 0
        try :
            self.user_manager.reload_user()
        except FileNotFoundError:
            print("Error: User database file not found.")
            return
        except PermissionError:
            print("Error: Permission denied to access user database.")
            return
        except Exception as e:
            print(f"Error: Failed to load user database - {e}")
            return

        users = self.user_manager.get_user()

        target_user = input("Enter a target username: ")
    

        if target_user not in users:
            print("Target is not available!")
            return
        else :
            target_password = users[target_user]


        
        for length in range(1, len(target_password)+1):
            for combo in itertools.product(char, repeat=length):  ## we will get tuple ('a','b','c') then we join those word together we get aa, ab, ac,bb,....
                attempt_count += 1
                
                attempt = "".join(combo)

                if attempt_count % 10000 == 0 :
                    print(f"Attempts Count = {attempt_count}")

                if attempt == target_password:
                    print(f"User {target_user} : Password FOUND -> {target_password}")
                    print(f"Attempts Count: {attempt_count}")
                    return



if __name__ == '__main__' :
    try:
        user = User_Management("C:\\Python Introduction to Cybersecurity\\Project Brute\\user_database.txt")

        # sb = Simple_Brute_Force(user)
        # sb.crack()

        ct = Count_tracking_Simple_Brute_Force(user)
        ct.crack()
    
    except Exception as e:
        print(f"Error: Program initialization failed - {e}")

