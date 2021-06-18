class Atm:
    def __init__(self,cardnum,pin):
        self.cardnum = cardnum
        self.pin = pin

    def checkbalance(self):
        print("Your balance is 1000000000")

    def withdrawl(self,amount):
        newamount = 1000000000 - amount
        print("you have withdrawn money "+(amount) +"Your remaining balance is "+ (newamount))



Cardnum = input("enter your card number")
pinnumber  = input("enter your pin number")

newuser =  Atm(Cardnum ,pinnumber)

print("Choose your activity ")
print("1.Need to know my Balance   2.withdrawl")
activity = int(input("enter  the number"))

if (activity == 1):
        newuser.checkbalance()
elif (activity == 2):
        amount = input("enter the amount")
        newuser.withdrawl(amount)
else:
        print("please enter a valid number")


