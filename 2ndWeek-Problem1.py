#Write a program to calculate the credit card balance after one year if a person only
#pays the minimum monthly payment required by the credit card company each month.

balance = 484
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

#Returns the adjusted balance of monthly compounded credit card balances.
for i in range(12):
    updatedBalance = balance - balance * monthlyPaymentRate
    balance = updatedBalance + annualInterestRate / 12 * updatedBalance

print('Remaining balance: ' + str(round(balance, 2)))