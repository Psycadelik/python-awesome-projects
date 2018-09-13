import os
import json
import difflib
from difflib import get_close_matches

data = json.load(open("data.json",'r'))

def translate(word):
	word=word.lower()
	if word in data:
		return data[word]
	elif word.title() in data:
		return data[word.title()]
	elif word.upper() in data:
		return data[word.upper()]
	elif len(get_close_matches(word, data.keys())) > 0:
		yn = input("Did you mean %s instead? Enter Y if yes, or N if no." % get_close_matches(word, data.keys())[0])

		if yn == "Y":
			return data[get_close_matches(word, data.keys())[0]]
		elif yn == "N":
			return "Your word does not exist. Please double check and try again"
		else:
			return "We didn't quite catch that :(. Please input Y or N "
	else:
		return "Your word does not exist. Please double check and try again"

wordInput = input("Please input the word you want to search for: ")

output = translate(wordInput)

if type(output) == list:
	for item in output:
		print(item)
else:
	print(output)		



