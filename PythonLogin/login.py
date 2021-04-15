def hasAccount():
    account = input("Do you have an account? y/n >>> ")
    if account == "y":
        return True
    elif account == "n":
        return False
    elif account == "maybe":
        print("What the fuck does that mean?")
        return hasAccount()
    else:
        print("You have to enter a valid input you dumb whore.")
        return hasAccount()


def login():
    correct = False
    email = input("What's your email? >>> ")
    password = input("What's your password? >>> ")
    with open("supersecrettextdoc.txt", "r") as file:
        content = file.readlines()
    content = [x.strip() for x in content]
    for i in range(0,int(len(content) / 3)):
        if email == content[i*3]:
            if password == content[i*3 +1]:
                print("Your secret phrase is: " + content[i*3 +2])
                correct = True
                break
    if not correct:
        print("Your email or password was incorrect.")


def wantAccount():
    want = input("Would you like to create an account? y/n >>> ")
    if want == "y":
        email = input("What's your email? >>> ")
        password = input("What's your password? >>> ")
        secretPhrase = input("What's your secret phrase? >>> ")
        with open("supersecrettextdoc.txt", "a") as file:
            file.write("\n" + email + "\n" + password + "\n" + secretPhrase)
    elif want == "n":
        print("What are you even doing here?")
    elif want == "maybe":
        print("Stop playing games.")
    else:
        print("You have to enter a valid input you dumb whore.")
        return wantAccount()


#ACTUAL CODE (SINCE I'M PUTTING EVRYTHING IN FUNCTIONS LOL)
while True:
    if hasAccount():
        login()
    else:
        wantAccount()

