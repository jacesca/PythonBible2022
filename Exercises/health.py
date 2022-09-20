import random

health = 50
difficulty = 3 #1: Easy, 2: Medium, 3: High

potion_health = int(random.randint(25, 50) / difficulty)
health += potion_health

print(health)
