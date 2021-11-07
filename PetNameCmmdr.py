#A script to ask for a pet name and then return a commander
#based off that name
import requests
import string
import webbrowser

endpoint = "https://api.scryfall.com/cards/search?"

#Assign the alphabet to numerical values
alpha = dict()
for index, letter in enumerate(string.ascii_lowercase):
    alpha[letter] = index + 1

#print(alpha)
#Define the split word function
def split(word):
    return [char for char in word]

#Gather pet name from user
pet_name = input("What is your pet's name? ")

#Double check to see if the name is split
#print(split(pet_name))

#Put the split pet name into a list
letters = split(pet_name)
numbers = []

for each in letters:
    if each in alpha:
        numbers.append(alpha[each])
        numbers.sort(reverse=True)
        #print(numbers)
        
def colormark(marker):
    if 1 <= marker < 6:
        return 'w'
    elif 6 <= marker < 10:
        return 'u'
    elif 10 <= marker < 16:
        return 'b'
    elif 16 <= marker < 20:
        return 'r'
    elif 20 <= marker <= 26:
        return 'g'

iden = colormark(numbers[0])
params = {"maxResults": 3}
commander = requests.get(f"https://api.scryfall.com/cards/random?q=c:{iden}+t:legend+r>=r+t:creature").json()
print(commander["name"])
webbrowser.open(commander['image_uris']['normal'])