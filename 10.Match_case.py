#  match case are switch cases that was introduced in python in python 3.10

# wap to create atm
# 1. Check Balance
# 2. Deposit Money
# 3. Withdraw Money
# 4. Exit\

balance=10000

userinput=int(input('''Enter 1. Check Balance
                2. Deposit Money
                3. Withdraw Money
                4. Exit
         '''))

match userinput:
    case 1:
        print("your balance is :\t",balance)
    case 2:
        blc=int(input('enter the amount'))
        balance+=blc
        print("Money deposited successfully and new balance is",balance)

    case 3:
        withamt=int(input('enter the amount'))
        if(withamt<=balance):
            balance-=withamt
            print("Money withdrawn successfully and new balance is",balance)

    case 4:
        quit

    case _:
        print("invalid input")
