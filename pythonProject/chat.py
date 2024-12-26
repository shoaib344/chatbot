import random
from api import uniteller
from api import uniList

user_Greetings = ['hello','hi','hey','good day']
bot_greeting=['Hello','Hi','Hi There','Welcome','How Can I Help']

user_Purpose = ['what is your work','your job','what is your job','what is your purpose','your purpose','how can you help']
bot_purpose = ["I can give you a List of all University in a Country",'I can tell you about the University',
               'I can guide you why Abroad Education is Beneficial']

user_abroad = ['why abroad education','why i should study abroad']
bot_abroad = ['There are many reasons to pursue an education abroad,\nIncluding the opportunity to see the world,\n'
               'Chance to gain new skills and knowledge, as well as the opportunity to meet new people and make new friends.',
               'There are many reasons why you should study abroad, including gaining a new perspective on the world,\n'
               'Learning a new language, and experiencing a new culture.']

user_uni = ['tell me about a university','i want to know about a university','give information of a university','about uni','uni']
user_List = ['country','countries for uni','tell me about a country for universities','show list of universities','show list']

thx = ['thanks','ok','alright','thank you']
bye = ['bye','see you']

print("Bot : I'm University ChatBot")

while True:
    user2 = input("User: ")

    if user2.casefold() in user_Greetings:
        print("Bot:",random.choice(bot_greeting))

    elif user2.casefold() in user_Purpose:
        print("Bot:",random.choice(bot_purpose))

    elif user2.casefold() in user_abroad:

        print("Bot:"+random.choice(bot_abroad))

    elif user2.casefold() in user_uni :
        while True:
            bot = uniteller()
            break

    elif user2.casefold() in user_List:
        while True:
            bot = uniList()
            break

    elif user2.casefold() in thx:
        bot_thx=['Your Welcome','No Worries :-)']
        print("Bot :",random.choice(bot_thx))

    elif user2.casefold() in bye:
        bot_bye =['Ok bye','See You Soon','Take Care',');']
        print("Bot: ",random.choice(bot_bye))
        break

    else:
        print("Bot: ","Sorry! I didn't understood what you have typed")


# References

# https://raw.githubusercontent.com/Hipo/university-domains-list/master/world_universities_and_domains.json
# https://www.youtube.com/watch?v=q30GEwUe5gY&t=740s
# https://www.youtube.com/watch?v=GwSe6FfNWm8
# https://docs.python.org/3/