...

#Given an integer x, return true if x is a 
#palindrome
# and false otherwise.

 

#Example 1:

#Input: x = 121
#Output: true
#Explanation: 121 reads as 121 from left to right and from right to left.
...

#name = 'Walobwa Dan'
#lst = ['Ismail', 'Kuno']

#print(name.lower())
#print(name.upper())
#print(name.strip())
#print(name[:: -1])
#print(name.split())
#print('and'.join(lst))


def palindrome(num):
    convert = str(num)
    result = convert[1:]
    if (convert == result):
        return 'Is a palindrome'
    else:
        return 'Is not a palindrome'
    


print(palindrome(121))

sentence = 'A man a plan a canal Panama'

#print(name.split()) - separates individual items on a list form
#print(' and '.join(lst)) - combines the items with the argument given
#print(name[:: -1]) - copies and reverses the string
# 
def palindromeString():
    splitted = sentence.split()
    joined = ''.join(splitted).lower()
    if joined ==  joined[:: -1]:
        return 'Is a palindrome'
    else:
        return 'Is not palindrome'
    
    def palindromeString(string):
        string1 = string.split()
        string1 = ''.join(splitted).lower()
    if string1 ==  string1[:: -1]:
        return 'Is a palindrome'
    else:
        return 'Is not palindrome'
    
    print(palindromeString())
    