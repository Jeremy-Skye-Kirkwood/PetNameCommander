#A script to ask for a pet name and then return a commander
#based off that name

import string

#Assign the alphabet to numerical values
alpha = dict()
for index, letter in enumerate(string.ascii_lowercase):
    alpha[letter] = index + 1

colors = {range(1,5):"W",range(6,10):"U",range(11,15):"B",range(16,20):"R",range(21,26):"G"}

print(alpha)
#Define the split word function
def split(word):
    return [char for char in word]

#Gather pet name from user
pet_name = input("What is your pet's name? ")

#Double check to see if the name is split
print(split(pet_name))

#Put the split pet name into a list
letters = split(pet_name)

if colors.get(alpha[letters[0]])!=None:
    print("yes")
else:
    print("no")