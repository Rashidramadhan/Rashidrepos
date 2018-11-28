birthdays = {'ben':'dec 12','rash':'Nov 21','hamis':'may 15', 'jijo':'dec 31','jemo':'dec 25'}

while True:
    print('Enter blank space to quit')
    name = input("Enter your friend's name:\n")
    if name =='':
        break
    if name in birthdays:
        print(birthdays [name] +' is the birthday of ' + name)
    else:
        print('There is no information for ' + name)
        print('What his/her birthday?\n')
        bday = input()
        birthdays[name]= bday
        print('data updated\n Thank you and have a great day')

    
    
