print('Record Keeping App'.upper())
print('A. Add a Record \nB. View All Record \nC. Clear All Records \nD. Exit')
choices = str(input('Please enter your  choice: '))

try:
    file = open('record.txt', 'r')
except FileNotFoundError:
    file = open('record.txt', 'x')

if choices.upper() == 'A':
    name = str(input('Enter Name: '))
    email = str(input('Enter Email: '))
    address = str(input('Enter Address: '))
    file = open('record.txt', 'a')
    file.write(f'\n{name}, {email}, {address}')
    file.close()
elif choices.upper() == 'B':
    file = open('record.txt', 'r')
    print(file.read())
    file.close()
elif choices.upper() == 'C':
    print('No records found!')
    file = open('record.txt', 'r+')
    file.truncate(0)
    file.close()
elif choices.upper() == 'D':
    print('Thank you!')
else:
    print('Invalid Input')