"""
MadLib v1.0
by: Jonathan Chapman
date: September 3, 2018
"""

a = "Hello "
b = "Stranger!"
print(a + b)

def welcome():
    print("Welcome to MADLIB!!!")

welcome()

adjective = input("Enter an adjective: ")
noun = input("Enter a noun: ")
verb = input("Enter a verb: ")
person = input("Enter a person's name: ")
country = input("Enter a country: ")
money = int(input("Enter a number: "))
pluralNoun = input("Enter a plural noun: ")
adverb = input("Enter an adverb: ")
bonusMoney = 753

print("Once there was a ", noun, ". This ", noun, " lived in ", country, ". ")
print(country, " was in a giant war and was desperately in need of help. One day ")
print(person, ", President of ", country, ", visited this ", adjective, noun, " and ")
print("said that if it would help ", verb," their enemies, he would give the ")
print(noun, " $", money, ". The", noun, " decided it was worth the money and ", verb)
print("the foes. The ", pluralNoun, " from ", country, " then awarded the ", noun, " his ")
print("$", money, " along with a bonus of $", bonusMoney, " that made a total of $", money + bonusMoney, ".")
print("The now rich ", adverb, adjective, noun, " lived happily ever after.")
