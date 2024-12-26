import json
import requests

link = f'https://raw.githubusercontent.com/Hipo/university-domains-list/master/world_universities_and_domains.json'
intents = requests.get(link)
data = json.loads(intents.text)

def uniList():

    while True:
        user = str(input("UniBot:""Choose a country for universities: "))

        for info in data:
            country = info['country']
            name = info['name']
            shrtform = info['alpha_two_code']

            if user == country.casefold() or user == shrtform:
                    print(name)
        print("---------------")
        print("UniBot:""Results found!")
        print("UniBot:""Here are lists of all universities in",user)
        break

def uniteller():

    while True:
        user1=input("UniBot:""Enter the name of university: ")

        for info in data:
            country = info['country']
            name = info['name']
            website = info['web_pages']
            state = info['state-province']

            if user1 == name:
                print("UniBot:""This university is located in",country,".","In the province of :",state)
                print("For more information you can visit to this University Website",website)
        break