# 10. Check whether an alphabet of a string inputted by the user is a vowel or consonant.

string = input('enter the string: ')
vowels = ['a','e','i','o','u']
vowel_array = []
consonant_array = []

for i in string :
  if i in vowels :
    vowel_array.append(i)
  else :
    consonant_array.append(i)

if len(vowel_array) == 0 :
    print('there are no vowels in this string')
else :
    print('the vowels are = ',vowel_array)

if len(consonant_array) == 0 :
    print('there are no consonants in this string')
else :
    print('the consonants are = ',consonant_array)
   
     