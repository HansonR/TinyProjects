import random

print("Welcome to Guess The Number!")
print("The rules are simple. I will think of a number and you try to guess it.")

number = random.randint(1, 10)
isGuessRight = False

while isGuessRight != True:
  guess = input("Devinez un chiffre en 1 et 10 :")
  if int(guess) == number:
    print("Vous avez deviné {}. Félicitations ! Vous avez réussi !".format(guess))
    isGuessRight = True
  elif int(guess) > number:
    print("Vous avez devinez {}. Ce chiffre est plus PETIT, continuez ".format(guess))
  elif int(guess) < number:
    print("Vous avez devinez {}. Ce chiffre est plus GRAND, continuez ".format(guess))