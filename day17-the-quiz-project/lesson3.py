#My completed version 07/29/25
#Creating Methods.
class User:
    def __init__(self, user_id, username):#<---When a Variable is attached to an Object it's called an Attribute(What it has)
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):#<---When a Function is attached to an Object it's called a Method (What it Does)
        user.followers += 1#    Methods always have a self as the first parameter. Meaning it will always know the Object
        self.following += 1#    that called it when the Method gets called.

user_1 = User("0001", "Oracle")
user_2 = User("0002", "Echo")
print(user_1.username)
print(user_2.username)
user_2.follow(user_1)#<-- Here we're getting ahold of the Object(user_2) then the Method adds the += 1 to (user_1)followers Attribute
print(user_2.followers)#  and += 1 to user_2's following Attribute.
print(user_2.following)
print(user_1.followers)
print(user_1.following)
print(f"{user_1.username} has User Id #{user_1.id} with {user_1.followers} follower \n"
      f"and follows {user_1.following} other users.")
print(f"{user_2.username} has User Id #{user_2.id} with {user_2.followers} followers \n"
      f"and follows {user_2.following} other user.")
