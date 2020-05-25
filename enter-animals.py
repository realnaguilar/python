# Enter the name of an animal you want to be add to the list
# Enter "quit" to end the program, enter an empty string to pop the last name in the list
# If an enter name is already in the list, it will delete the name from the list
# Made with love by Nicolás Aguilar
# 05/25/2020

animals = ['cat', 'dog', 'horse']

def list_o_matic():
    if name == '':
        animals.pop()
        message = print(' has been pop from the list.')
        return message
    elif name in animals:
        animals.remove(name)
        message = print(name + ' has been removed from the list.')
        return message
    else:
        animals.append(name)
        print(name + ' has been append to the list.')

while True:
    if animals == []:
        print('Goodbye')
        break
    else:
        print('Look at all the animals: ' + str(animals))
        name = input('Enter the name of an animal: ')
        if name == 'quit':
            print('Goodbye')
            break
        else:
            list_o_matic()