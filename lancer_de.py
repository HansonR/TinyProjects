import random

while True:
    x = int(input("1 -> lancer le dé -- 0 -> quitter : "))
    if x == 0:
        print("Exit")
        break
    elif x == 1:
        print(random.randint(1, 6))
    else:
        print("entrée incorrect")