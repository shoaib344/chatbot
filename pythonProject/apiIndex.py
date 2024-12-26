from test00 import setup

uniData, countryIx, nameIx = setup()

LIMIT = 10


def uniList():
    while True:
        user = str(input("UniBot:""Choose a country for universities: "))
        userLow = user.lower()
        print("UniBot:""Results found!")
        print("UniBot:""Here are lists of all universities in", user)

        try:
            countryIndicies = countryIx[userLow]
        except KeyError:
            print("Unknown country, please try again")
            continue

        count = 0
        for index in countryIndicies:
            info = uniData[index]
            print(info)
            if count >= LIMIT:
                break
            count += 1

        break


def uniteller():
    """
    user gives a name of a university
    get the index from nameIndex using user input.
    Use the index to get uni information from uniData
    print out the uni information
    """
    while True:
        user = input("UniBot:""Enter the name of university: ")

        try:
            desiredIndex = nameIx[user]
        except KeyError:
            print("Please enter the correct name for the university")
            continue

        desiredIndex = nameIx[user]
        desiredInfo = uniData[desiredIndex]

        webPage = desiredInfo['web_pages']
        uniName = desiredInfo['name']
        country = desiredInfo['country']

        print("UniBot: ", uniName, "is located in", country, )
        print("For more information you can visit to this University Website", webPage)
        break
