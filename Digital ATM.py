#I'm stuck at the newUser part
class ATM:
    def __init__(self, cardNumber, pin):
        self.cardNumber = cardNumber
        self.pin = pin
    def balance ():
        currentBalance = 10000
        print ("Your current balance is", currentBalance, "AED")
    def withdraw ():
        currentBalance = 10000
        withdrawlAmount = int (input ("How much money would you like to withdraw? "))
        currentBalance -= withdrawlAmount
    balance ()
    withdraw ()
newUser = ATM (cardNumber, pin)
