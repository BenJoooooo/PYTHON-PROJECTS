name = input('Enter your name: ')
years = float(input('Enter years in service: '))
office = input('Enter office: ')

if office == 'it' and 'IT':
    if years >= 10:
        print(f'Hi {name} your bonus is 10,000')
    else:
        print(f'Hi {name} your bonus is 5,000')
elif office == 'acct':
    if years >= 10:
        print(f'Hi {name} your bonus is 12,000')
    else:
        print(f'Hi {name} your bonus is 6,000')
elif office == 'hr':
    if years >= 10:
        print(f'Hi {name} your bonus us 15,000')
    else:
        print(f'Hi {name} your bonus is 7,500')
else:
    print('Invalid input')
