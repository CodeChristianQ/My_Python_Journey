#My completed solution 07/22/2025
from random import randint
dice_images = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(1, 6)
print(dice_images[dice_num])
#there is no index 6, 0 is also not included in our dice_num
# fix is dice_num = randint(0, 5)
