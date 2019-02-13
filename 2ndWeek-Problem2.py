# Write a program that calculates the minimum fixed monthly payment needed in order pay off a credit card balance
# within 12 months. By a fixed monthly payment, we mean a single number which does not change each month, but instead
# is a constant amount that will be paid each month.Assume that the interest is compounded monthly according to the
# balance at the end of the month (after the payment for that month is made). The monthly payment must be a multiple
# of $10 and is the same for all months . Notice that it is possible for the balance to become negative using this
# payment scheme, which is okay.


balance = 3926
annualInterestRate = 0.2
minPayment = 0

while balance > 0:
    minPayment += 10
    testBalance = balance
    for i in range(12):
        updatedBalance = testBalance - minPayment
        testBalance = updatedBalance + annualInterestRate / 12 * updatedBalance
    if testBalance <= 0:
        break

print('Lowest payment: ' + str(minPayment))

