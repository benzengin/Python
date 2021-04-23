invited_guests = ['Sushi', 'Shoya', 'Karin', 'Bayram', 'Attila']

name = input('What is your name? ')
if name in invited_guests:
    print('Welcome, ', name)
else:
    print('Your are not invited!')
