# Write a program that uses bisection search to find the lowest payment to
# pay off a monthly compounded balance in a 12 month period to the nearest cent.


balance = 999999
annualInterestRate = 0.18
monthlyInterestRate = annualInterestRate/12
upperLimit = round((balance*(1 + monthlyInterestRate)**12)/12, 2)
lowerLimit = balance/12


while balance > 0:
    testBalance = balance
    minPayment = (upperLimit + lowerLimit)/2
    for i in range(12):
        testBalance = testBalance - minPayment
        testBalance = round(testBalance + monthlyInterestRate * testBalance, 3)
    if testBalance < 0:
        upperLimit = minPayment
    elif testBalance > 0:
        lowerLimit = minPayment
    else:
        break


print('Lowest payment: ' + str(round(minPayment, 2)))