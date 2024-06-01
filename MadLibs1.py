print("Lets play Mad Libs.")
print("Are you ready?")

pNoun1 = input("Please give me a proper name. ")
print("What gender is",pNoun1, "?" "boy, girl, or non?")
assign = input()
adj1 = input("Please give me an adjective. ")
noun2 = input("Please give me a noun. ")
verb1 = input("Please give me a verb. ")
bpart1 = input("Please give me a plural body part. ")
celeb1 = input("Please give me a Celebrity Name. ")
num1 = input("Please give me a number. ")
animal1 = input("Please give an animal(plural). ")

if assign == "boy":
    gen = ["he", "his"]
elif assign == "girl":
    gen = ["her","hers"]
elif assign == "non":
    gen = ["they", "theirs"]
else:
    print("please use a valid entry")

print("Today I will tell you a story about", pNoun1, "and", gen[0], "adventure in the land of",adj1 +"ville.") 
print("One day", pNoun1, "was sitting on", gen[0], noun2, "when a huge wind stated to blow")
print(pNoun1, "was quickly able to", verb1, "away from", gen[0], noun2, "but the wind was too strong and", gen[0], "landed on", gen[1], bpart1)
print("Fortunately ,", celeb1, "was right there to catch", pNoun1, "and prevented any serious damage from happening")
print(pNoun1, "was so thankfull they decided to give", celeb1, "a tip of $" + num1, "dollars.")
print(celeb1, "was so overjoyed they asked you to be in their next movie with them")
print("Before", pNoun1, "knew it they had a smash hit on their hands called ", pNoun1, "and the", num1, animal1)