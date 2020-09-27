import json
from difflib import get_close_matches
data=json.load(open('data.json'))
def dict(x):
	if x in data:
		return data[x]
	elif x.upper() in data:
		return data[x.upper()]
	elif x.title() in data:
		return data[x.title()] 
	else:
		return "word does not exist!"
x=input('Enter the Word: ').lower()
x=get_close_matches(x,data.keys())
if len(x)>0:
	x=x[0]
else:
	x='nowordgiven'
print('Searching for ('+x+')...\n')
y=dict(x)
if type(y)==list:
	for i in range(0,len(y)):
	    print(y[i])
else:
	print(y)
