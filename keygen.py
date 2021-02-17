import random

longpass = int(input('Longueur du mot de passe : '))
s = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!"#$%&()*+,-./:;<=>?@[]^_`{|}~'
# join sert à regrouper les caractère en un seul mot
password = "".join(random.sample(s, longpass))
print(password)