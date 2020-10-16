import random

capletters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
smallletters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".lower()
symbols = "!@#$%*-_"
numeric = "0123456789"

stringcombination = capletters + smallletters + symbols + numeric

length =  12

generatedpassword = "".join(random.sample(stringcombination, length))

print(generatedpassword)