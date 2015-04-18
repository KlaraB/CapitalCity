__author__ = 'u269074'
import random

capital_city = {
    "United Kingdom": "London",
    "Germany": "Berlin",
    "Spain": "Madrid",
    "Italy": "Rome",
    "France": "Paris",
    "Romania": "Bucharest",
    "Austria": "Vienna",
    "Hungary": "Budapest",
    "Poland": "Warsaw",
    "Bulgaria": "Sofia",
    "Czech Republic": "Prague",
    "Slovenia": "Ljubljana",
    "Croatia": "Zagreb",
    "Finland": "Helsinki",
    "Swiss": "Bern",
    "Portugal": "Lisbon"
}
answer = "yes"

while answer == "yes":
    answer = raw_input("Do you want to guess a capital city(yes/no)? ")

    if answer == "yes":
        country = random.choice(capital_city.keys())
        odg2 = raw_input("What is the capital city of " + str(country) + "? ")

        if odg2.lower() == capital_city[country].lower():
            print("Your answer is correct!")
        else:
            print("Sorry, try again!")

    elif answer == "no":
        print("Ok, maybe next time!")
    else:
        print("Error")


