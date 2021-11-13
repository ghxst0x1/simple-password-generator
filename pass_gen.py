import random
small = "abcdefghijklmnopqrstuvwxyz" 
large = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numeric = "0123456789"
symbol = "!@#%^&*()_-=+.<>/?:,|\\" #add or remove according to your preference

#random String generating
string = small+large+numeric+symbol
size = 8 #it is the total no of character in the password, change to your like
passwd = "".join(random.sample(string,size))
print("\n Generated Password is ===>",passwd,"<===")
print("\n If you wish to use this password don't forgot to save this password somewhere \U0001F600")
print(" \033[91m {}\033[00m".format("\n Made with \u2764\uFE0F  by VoidGhxsT"))