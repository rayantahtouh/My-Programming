#Intial Condintions:
i = 0
total = 0 

#Conditions and iteration / Ask the user to enter a number:
while i >= 0:
    number = int(input("Please enter your number (if you entered -1 the program will stop):"))
    i += 1
    total += number

    #Average Calculation:
    if number == -1:
        break

if total>0:
    i-=1
    total1 = total+1
    average = total1/i
    print(f"The average of the numbers is:{average}")
else:
    print("No valid numbers entered.")
     


