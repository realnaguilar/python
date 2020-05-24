# Integer or Q while loop
# This function will take all your enter numbers as input and add each one to the total
# The parameters for the function can be 'A' or 'T'
# Enter Q in uppercase to quit
# Nicolás Aguilar

def adding_report(report):
    items = ''
    total = 0
    while True:
        input_string = input('Integer or Q: ')
        if input_string.isdigit():
            total += int(input_string)
            if report == 'A':
                items += input_string
                items += '\n'
        elif input_string.startswith('Q'):
            if report == 'A':
                print()
                print('Items\n' + items + '\nTotal\n' + str(total))
            elif report == 'T':
                print()
                print('Total\n' + str(total))
            else:
                pass
            break
        else:
            print('Input is invalid')
adding_report('T')