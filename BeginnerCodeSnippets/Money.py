
operation = input('Welcome to the CS Banking\n'
    '1: Take money\n'
    '2: Put money\n'
    '3: Money transfer\n'
    'Q:Quitting\n')

if operation== '1':
    money = int(input('How much money do you want to take ? : '))
    balance = int(input('How much money do you have ? : '))
    if balance<money:
        print('You can not do this operation!\nYour balance is not enough to do this operation!')
    else:
        print("Your money: ", (balance - money))
elif operation=='2':
    money = int(input('How much money do you want to put? : '))
    balance = int(input('How much money do you have? : '))
    print('Your name balance is: ', (money + balance))
elif operation=='3':
    balance = int(input('How much money do you have? : '))
    transfer = int(input('How much money do you want to transfer? : '))
    if balance>transfer:
        print('You transferred : ', transfer, '$')
        print('Your name balance is now: ', (balance - transfer), '$')
    elif balance<transfer:
        print('There is not enough Money to do the transfer :( ')
