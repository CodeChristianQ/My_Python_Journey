
#Here in this section the goal is to access our created file and read the file.
#Method 1
# file = open("my_file.txt")
# contents = file.read()
# print(contents)
# file.close()

#Method 2 (Most common)
# with open("my_file.txt") as file:
#     contents = file.read()
#     print(contents)

#Here in this section the goal is to access our file and write to it.
# with open("my_file.txt", mode="w") as file:
#     file.write("New text.")
    #This will replace what is written. use an "a" instead of a "w" in the mode parameter to append to the file.

#Similarly if you use (with open("my_file.txt", mode="w") as file:) and the file doesn't exist. It will be created.
#Example:
# with open("newest_file.txt", mode="w") as file:
#     file.write("Hello Universe!")
#This will only work in "w" (write) mode and if the file doesn't exist.

with open("/home/kaijuchristian/Desktop/my_file.txt") as file:
    content = file.read()
    print(content)