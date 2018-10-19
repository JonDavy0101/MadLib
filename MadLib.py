"""
name: MadLib v2.0
by: Jonathan Chapman
date: September 9, 2018
"""

def welcome():
    print("\nWelcome to MADLIB!!!\n")

welcome()

while True:
    try:
        userName = str(input("Please enter your name: "))
        if userName.isalpha() == True:
            break
        else:
            print("Sorry. This word cannot have any numbers, spaces, or special characters.")
            pass
    except:
        print("Sorry. This is not a name. You must enter a name.")
        pass
print("Nice to meet you, " + userName + "!\n")
while True:
    try:
        adjective = str(input("Enter an adjective: "))
        if adjective.isalpha() == True:
            break
        else:
            print("Sorry, " + userName + ". This word cannot have numbers, spaces, or special characters.")
            pass
    except:
        print("Sorry, " + userName + ". This is not a word. You must enter an adjective.")
        pass
while True:
    try:
        noun = str(input("Enter a noun: "))
        if noun.isalpha() == True:
            break
        else:
            print("Sorry, " + userName + ". This word cannot have numbers, spaces, or special characters.")
            pass
    except:
        print("Sorry, " + userName + ". This is not a word. You must enter a noun.")
        pass
while True:
    try:
        verb = str(input("Enter a verb: "))
        if verb.isalpha() == True:
            break
        else:
            print("Sorry, " + userName + ". This word cannot have numbers, spaces, or special characters.")
            pass
    except:
        print("Sorry, " + userName + ". This is not a word. You must enter a verb.")
        pass
while True:
    try:
        person = str(input("Enter a person's name: "))
        if person.isalpha() == True:
            break
        else:
            print("Sorry, " + userName + ". This word cannot have numbers, spaces, or special characters.")
            pass
    except:
        print("Sorry, " + userName + ". This is not a word. You must enter a name.")
        pass
while True:
    try:
        country = str(input("Enter a country: "))
        if country.isalpha() == True:
            break
        else:
            print("Sorry, " + userName + ". This word cannot have numbers, spaces, or special characters.")
            pass
    except:
        print("Sorry, " + userName + ". This is not a word. You must enter a country.")
        pass


while True:
    try:
        money = int(input("Enter a number: "))
        break
    except:
        print("Sorry, " + userName + ". This is not a number. You must enter a number (without decimals).")
        pass


while True:
    try:
        pluralNoun = str(input("Enter a plural noun: "))
        if pluralNoun.isalpha() == True:
            break
        else:
            print("Sorry, " + userName + ". This word cannot have numbers, spaces, or special characters.")
            pass
    except:
        print("Sorry, " + userName + ".This is not a word. You must enter a plural noun: ")
        pass
while True:
    try:
        adverb = str(input("Enter an adverb: "))
        if adverb.isalpha() == True:
            break
        else:
            print("Sorry, " + userName + ". This word cannot have numbers, spaces, or special characters.")
            pass
    except:
        print("Sorry, " + userName + ". This is not a word. You must enter an adverb.")
        pass


while True:
    try:
        randomNumber = float(input("Enter a random number with a decimal: "))
        break
    except:
        print("Sorry, " + userName + ". This is not a decimal value. You must enter a number with a decimal.")
        pass

BONUS_MONEY = 450

print("\nOnce there was a ", noun, ". This ", noun, " lived in ", country + ". ", sep='')
print(country, " was in a giant war and was desperately in need of help. One day ", sep='')
print(person, ", President of ", country, ", visited this ", adjective, " ", noun, " and ", sep='')
print("said that if it would help ", verb," their enemies, he would give the ", sep='')
print(noun, " $", money, ". The ", noun, " decided it was worth the money and ", verb, sep='')
print("the foes. The ", pluralNoun, " from ", country, " then awarded the ", noun, " his ", sep='')
print("$", money, " along with a bonus of $", BONUS_MONEY, " that made a total of $", money + BONUS_MONEY, ".", sep='')
print("The now rich ", adverb, " ", adjective, " ", noun, " lived happily ever after for", sep='')
print(randomNumber, " years when it died in peace. The " + pluralNoun + " of " + country + " gave the", sep='')
print("heroic " + noun + " a lavish burial and constructed a memorial in its name.", sep='')
print("If it wasn't for the " + noun + ", the " + pluralNoun + " of " + country + " would not have", sep='')
print("enjoyed the peace they have today.", sep='')
print("\nTHE END")
