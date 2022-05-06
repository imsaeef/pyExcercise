firstname = input('enter the first name: ')
length = len(firstname)

if length < 5:
    surename = input('enter the sure name: ')
    name = firstname+surename
    name = name.upper()
    print(name)
else:
    firstname = firstname.lower()
    print(firstname)
