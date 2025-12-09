from UserManagement import *
from SimpleBruteForceAttack import *
from DictionaryAttack import *
from HybridAttack import *

user_database_file = "C:\\Python Introduction to Cybersecurity\\Project Brute\\user_database.txt"

user = User_Management(user_database_file)
user1 = Simple_Brute_Force(user_database_file)
user2 = Count_tracking_Simple_Brute_Force(user_database_file)
user3 = DictionaryAttack(user_database_file)
user4 = HybridAttack(user_database_file)


# user.reload_user()
# user.menu()
# user2.crack()
# user3.crack()
# user1.crack()
user4.crack()

