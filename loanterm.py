print("======= loan calculator =======")

loanamount = float(input("Enter the loan amount: "))
loanterm = int(input("Enter the loan term months: "))

monthly_interest_rate = 0.05 

interest_per_month = loanamount * monthly_interest_rate
totalinterest = interest_per_month * loanterm
total = loanamount + totalinterest
monthlypayment = total / loanterm

print("===== Result ======\n")
print(f"{'Monthly interest rate:':<25} {monthly_interest_rate*100:>7.2f}%")
print(f"{'Interest per month:':<25} {interest_per_month:>10,.2f}")
print(f"{'Total Interest for ' + str(loanterm) + ' months:':<25} {totalinterest:>10,.2f}")
print(f"{'Total of payment for ' + str(loanterm) + ' months:':<25} {total:>10,.2f}")
print(f"{'Payment every month:':<25} {monthlypayment:>10,.2f}")






