import random


def gen(string, size):
    passwd = "".join(random.sample(string, int(size)))
    print("\n Generated Password is ===>", passwd, "<===")
    print(
        "\n If you wish to use this password don't forgot to save this password somewhere \U0001F600"
    )
    print(" \033[91m {}\033[00m".format("\n Made with \u2764\uFE0F  by HoLyGhxsT"))


def main():

    small = "abcdefghijklmnopqrstuvwxyz"
    large = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numeric = "0123456789"
    # symbol = "!@#%^&*()_-=+.<>/?:,|\\"  # add or remove according to your preference
    symbol = "!@#$%&*_-<>?:" #recommended

    # random String generating
    string = small + large + numeric + symbol
    # size = 8  # it is the total no of character in the password, change to your like
    size = input("\nEnter the length of the password you wish to generate: ")
    if int(size) < 8 and int(size) > 5:
        print(
            "\nIt is Recomended to create password with length greater than or equal to 8 !"
        )
        op = input("\n Press 'Y' to continue: ")
        if op == "Y" or op == "y":
            gen(string, size)
        else:
            exit()
    elif int(size) < 6:
        print("\nAre you generating a password??? Exiting...")
        exit()
    else:
        gen(string, size)


if __name__ == "__main__":
    main()
