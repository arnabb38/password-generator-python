import random

capletters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
smallletters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".lower()
symbols = "!@#$%*-_"
numeric = "0123456789"

#combining character set
stringcombination = capletters + smallletters + symbols + numeric

#length of the password
length =  12

#generating random password
generatedpassword = "".join(random.sample(stringcombination, length))

print(generatedpassword)