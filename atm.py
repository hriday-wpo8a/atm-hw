class Atm:
    def __init__(self,cardNo,pin):
        self.cardNo=cardNo
        self.pin=pin

    def check_balance(self):
        print("Your balance is 50000")

    def withdrawal(self,amount):
        new_amount=50000-amount
        print("you have withdrawn amount " + str(amount))

def main():
    card_number=input("insert your card number : ")
    pin_number = input("enter your pin number : ")
    new_user=Atm(card_number,pin_number)

    print("choose your activity")
    print("1. balance enquiry 2.withdrawl")
    activity = int(input("enter the activity number : "))

    if (activity==1):
        new_user.check_balance()

    elif(activity ==2):
        amount = int(input("enter the amount: "))
        new_user.withdrawal(amount)
    else :
        print("enter a valid number")

if __name__ =="__main__":
    main()