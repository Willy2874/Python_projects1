words = open('words.txt', 'r', encoding='utf-8')
print(words.read())
words.close()

#with open('words.txt', 'r', encoding='utf-8') as file:
    #print(file.read())

#with open('names.txt', 'w', encoding='utf-8') as file:
    #file.write('walobwa\n')

#with open('names.txt', 'a', encoding='utf-8') as file:
    #file.write('\nJames')

lst = ['\nDan', '\nIsmail', '\nJames', '\nKuno']

with open('name.txt', 'w', encoding= 'utf-8') as file:

    #with open ('emails.txt', 'r', encoding='utf-8') as file:
     #   emails = file.read()
      #  for email in emails:
       #     if email == 'Walobwadan@gmail.com':
        #        print('Found')
         #   else:
          #      print('Not Found')
        #print(emails)

    #print("I study at Zindua")