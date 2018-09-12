import os
import json

data = json.load(open("data.json",'r'))

def translate(word):
	if word in data:
		return data[word]
	else:
		return "Your word does not exist. Please double check and try again"

wordInput = input("Please input the word you want to search for: ")

print (translate(wordInput))



