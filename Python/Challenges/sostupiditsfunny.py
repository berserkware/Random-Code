import random

responses = ["Go away", "I dont care", "I didnt ask", "Give me beans", "*screams*", "beans"]

def talk():
    s = input()

    print(responses[random.randint(0, len(responses) - 1)])

    talk()

talk()