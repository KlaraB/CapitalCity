__author__ = 'U269074'

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

answer = "kdo pa ve"

while answer != "da":
    answer = raw_input("Do you want to guess a capital city? ")

    if answer == "yes":
        for country in capital_city:
            odg2 = raw_input("What is the capital city of " + str(country) + "? ")

            if odg2.lower() == capital_city[country].lower():
                print("Your answer is correct!")
                answer = raw_input("Do you want to guess a capital city? ")
                if answer == "no":
                    break

            else:
                print("Sorry your answer is not correct. Try another one!")

    elif answer == "no":
        print("Okay, maybe next time!")
        break
    else:
        print("Sorry, we don't understand, let's try again!")


