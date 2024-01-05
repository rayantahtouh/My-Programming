#Assing each competition a time using float
t_1=float(input("Please give me how many minutes it took you to finish swimming:"))
t_2=float(input("Please give me how many minutes it took you to finish cycling: "))
t_3=float(input("Please give me how many minutes it took you to finish running: " ))

#Calculate and display the total time for the thriatlon
t=t_1+t_2+t_3
print(f"The total time taken to complete the triathlon is: {t}")

#Condition that determines which award category 
if(0<t<=100):
    print("The award that the participant will receive is: Provincial Colours")

elif(100<t<=105):
    print("The award that the participant will receive is: Provincial Half Colours")

elif(106<=t<=110):
    print("The award that the participant will receive is: Provincial Scroll")

else:
    print("No award")