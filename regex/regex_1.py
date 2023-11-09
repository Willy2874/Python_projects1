import re

#^ -> The start of the string
#$ -> End of the string
#[] -> Any matching items inside the brackets
#+ -> Any character preceeding the previous
#. -> every character inside a string
#\ -> Allows to escape certain character
#| 

#small letters -> 3
#number -> 3 - 5
#non alphabets or numbers characters

# string = 'abc12345'
# pattern = "^[a-z]{3}[0-9]{3,5}[^a-zA-z0-9]{1}$"
# print(re.search(pattern, string))

number = "Number: +2540728753742"
pattern = "\+[0-9]{3}\s[0-9]{9}"
print(re.search(pattern, number))
