print("======= loan calculator =======")

loanamount = float(input("Enter the loan amount: "))
loanterm = int(input("Enter the loan term months: "))

print("\n")
interestrate = 0.06
totalinterest = loanamount * interestrate * (loanterm / 12)
total=float(loanamount) + totalinterest
monthlypayment = total /int (loanterm)

print("===== Result ======\n")
print(f"Interest per month @6% :{interestrate:>,.2f}")
print(f"Total Interest for {loanterm} months:{totalinterest:>,.2f}")
print(f"Total of payment for {loanterm} months:{total:>,.2f}")

print(f"Payment every month:       {monthlypayment:>,.f}")
      