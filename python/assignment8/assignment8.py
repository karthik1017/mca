# 1. Return the characters of the given string
>>> import re
>>> p = re.compile('\w') 
>>> print(p.findall("karthik devaraj"))

# 2. Return each word of the given string
>>> import re 
>>> p = re.compile('\w+') 
>>> print(p.findall("karthik devaraj")) 

# 3. Return the first word of a given string
>>> import re
>>> p = re.compile('^\w+')
>>> print(p.findall('i studied in sri sathya sai vidya'))

# 4. Return the last word of a given string
>>> import re
>>> p = re.compile('\w+$')
>>> print(p.findall('rama krishna'))

# 8. Return the domain types of given email ids

>>> import re
>>> re.findall(r'@+\S+[.]','karthik@gmail.com')
    ['@gmail.']

# 9. Return the domain types with extensions of given email ids

>>> import re
>>> re.split('[.]','karthik@gmail.com')[-1]
    'com'

# 10. Return the domain of given email ids

>>> import re
>>> re.findall('@+\S+','karthik@gmail.com')
    ['@gmail.com']

# 11. Return the date from a given string

>>> import re
>>> str = 'karthik was born on 23/12/1996'
>>> re.findall('(\d{1,2})/(\d{1,2})/(\d{4})',str)
[('23', '12', '1996')]

# 12. Return the year of the date from a given string

>>> import re
>>> str = 'karthik was born on 23/12/1996'
>>> re.findall(r'(\d{4})',str)
    ['1996']

# 13. Return the words that start with a vowel

>>> import re
>>> str = 'i am a hero in india'
>>> re.findall("[aeiouAEIOU]\w+",str)
   ['am', 'ero', 'in', 'india']    

# 15. Validating a phone number

import re
string=input("Enter a number")
if re.match(r'[789]\d{9}$',string):   
    print ('valid' ) 
else:  
	print ('invalid')

# 16. Split with multiple delimiters

>>> import re
>>> text = 'i am karthik, i am studying \n in pes university; my domain is MCA'
>>> print(re.split('; |, |\*|\n',text))

# 18. matches a string that has an a followed by zero or more b's

import re
string=input("Enter a string")
if re.search('ab*?',  text):
	print('Found a match!')
else:
	print('Not matched!')

# 19. find sequences of lowercase letters joined with a underscore.

import re
string=input("Enter a string")
if re.search('^[a-z]+_[a-z]+$',text):
    print('Found a match!')
else:
    print('Not matched!')

# 20. matches a string that has an 'a' followed by anything, ending in 'b'

import re
string=input("Enter a string")
if re.search('a.*?b$',text):
    print('Found a match!')
else:
    print('Not matched!')

# 21. matches a word containing 'z', not start or end of the word.

import re
string=input("Enter a string")
if re.search('\Bz\B',  text):
    print('Found a match!')
else:
    print('Not matched!')

# 22. extract year, month and date from a an url

>>> import re
>>> url= "http://www.gmail.com/users/12345/bids/start/2012/01/01/end/2012/01/31"
>>> re.findall(r'/(\d{4})/(\d{1,2})/(\d{1,2})/', url)
    [('2012', '01', '01')]

# 23. separate and print the numbers of a given string.

>>> import re
>>> str = 'kartik12345'
>>> re.findall('\d',str)
['1', '2', '3', '4', '5']






