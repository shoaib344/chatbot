import random
print("hello, what is your name")
Mr_Simon = input()

name = "UniBot"
work = "right university for student's bright future"

countries = "across all the countries in the world"
best = "USA and Uk the most as they are english speaking countries"
budget = "minimum $30000 for your tution fees per year"
UK = "UK is the home of many high ranked universities and provides quality education"

bot_template = "UniBot : {0}"
bot_ans = Mr_Simon + " : {0}"

Answers = {

"what's your name?": [
   "They call me {0}".format(name),
   "I usually go by {0}".format(name),
   "My name is the {0}".format(name)],

"What is your work?": [
    "We help in deciding {0}".format(work),
    "We help to {0}".format(work)],

"Which are the best countries for education?": [
    "All countries are good but I recommend {0}".format(best),
    "I really like {0}".format(best)],

"In Which countries you deal?": [
    "We deal in all {0}".format(countries),
    "We help in all {0}".format(countries)],

"What should be the budget?": [
  "You should have {0}".format(budget),
  "You should be capable for {0}".format(budget)],

"Why UK is the best options for abroad education?": [
    "{0}".format(UK)],


"Sorry": ["Sorry what?"]

}

def respond(answer):
    if answer in Answers:
      bot_answer = random.choice(Answers[answer])
    else:
      bot_answer = random.choice(Answers["Sorry"])
    return bot_answer

def best_match(questions):
    if "name" in questions:
      y_text = "what's your name?"
    elif "work" in questions:
      y_text = "What is your work?"
    elif "how are" or "hello" or "hi" in questions:
      y_text = "Hey! how are you?"
    elif "best" in questions:
      y_text = "Which are the best countries for education?"
    elif "which countries" in questions:
      y_text = "In Which countries you deal?"
    elif "budget" in questions:
      y_text = "What should be the budget?"
    elif "UK" in questions:
      y_text = "Why UK is the best options for higher education?"
    else:
      y_text =""
    return y_text

def give_response(answer):
   (bot_ans.format(answer))


   response = respond(answer)
   print(bot_template.format(response))

while True:
   user_input = input()
   user_input = user_input.lower()
   best_match_text = best_match(user_input)
   give_response(best_match_text)
   if user_input == "exit" or user_input == "stop" or user_input == "thank you":
      break