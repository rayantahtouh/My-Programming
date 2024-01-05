import math

print("investment - to calculate the amount of interest you'll earn on your investment")
print("Brond      - to calculate the amount of interest you'll earn on your investment \n")

#User Choice and Calculation Proceedures:
cal=str(input("Enter either 'investment' or 'bond' from the menu above to proceed: "))

if(cal=='investment') or (cal=="Investment") or (cal=="INVESTMENT"):
    ammount_money=int(input("Please input the amount of money that you are depositing:"))
    interest_rate=8
    print(f"the ammount for the interest you have entered is: {interest_rate}")
    number_year=float(input("Please enter the number of years you plan on inveting: "))

#Type of interest for method calculation:
    interest=str(input("Please choose between simple or compound interest: "))
    if(interest.lower()=="simple"):
     r = interest_rate/100 # r is the interest entered above divided by 100, e.g. if 8% is entered, then r is 0.08.
     P=ammount_money # ‘P’ is the amount that the user deposits.
     t=number_year # t is the number of years that the money is being invested.
     A= P*(1 + r*t) # A is the total amount once the interest has been applied.
     print(f"The total amount once the interest has been applied is: {A}")

    elif(interest.lower()=="compound"):
       r = interest_rate/100
       P=ammount_money
       t=number_year
       A= P * math.pow((1+r),t)
       print(f"The total amount once the interest has been applied is: {A}")

 
elif(cal=='bond') or (cal=='Bond') or (cal=='BOND'):
   P1=int(input("Please enter the present value of the house: "))
   interest_rate1=float(input("Please enter the the interest rate: "))
   number_of_month=float(input("The number of months you plan to take to repay the bond: "))

   #Bond repayment calculation:
   P=P1 #‘P’ is the present value of the house.
   i=(interest_rate1/100)/12 #‘i’ is the monthly interest rate
   n=number_of_month #‘n’ is the number of months over which the bond will be repaid.

   #Bond Repayment Formula:
   repayment = (i * P)/(1 - (1 + i)**(-n))
   print(f"The amount of money you have to repay each month is: {repayment}")


   


