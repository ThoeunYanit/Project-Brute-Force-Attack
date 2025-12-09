from UserManagement import User_Management

class DictionaryAttack:
    def __init__(self, user_database_file):
        self.user_manager = user_database_file

    def crack(self):
        try :
            self.user_manager.reload_user()
        except FileNotFoundError :
            print("Error: User database file not found!")
            return
        except Exception as e:
            print(f"Error: Failed to load user database - {e}")
            return
        except PermissionError:
            print("Error: Permission denied to access user database.")
            return
        
        users = self.user_manager.get_user() ##make use of dictionary not file

        target_user = input("Enter target username: ")

        if target_user not in users:
            print("User not found!")
            return

        target_password = users[target_user].strip()
        wordlist = 'C:\\Python Introduction to Cybersecurity\\Project Brute\\dictionary_list.txt'

        attempt = 0
        try :
            with open(wordlist, 'r') as f:
                for word in f:
                    attempt += 1
                    print(f"Trying: {word.strip()}")

                    if word.strip() == target_password:
                        print(f"\nPASSWORD FOUND ► {target_password}")
                        print(f"Attempts: {attempt}")
                        return
        except FileNotFoundError:
            print(f"Error: Dictionary file not found.")
        except PermissionError:
            print(f"Error: Permission denied to read dictionary file.")
        except Exception as e:
            print(f"Error: Failed to read dictionary file - {e}")
            




if __name__ == '__main__' :
    try: 
        user = User_Management("C:\\Python Introduction to Cybersecurity\\Project Brute\\user_database.txt")
        da = DictionaryAttack(user)
        da.crack()
    except Exception as e:
        print(f"Error: Program initialization failed - {e}")    