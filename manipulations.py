#Ask the user to enter a sentence
str_manip=input("please enter your phrase:")
length_1=len(str_manip)
#Print the length
print(f"the length of str_manip is: {length_1}")

#Find the last letter in str_manip sentence and Replace every occurrence of this letter in str_manip with ‘@’.
new=str_manip[-1]
new1=str_manip.replace(new,"@")
#Print the output
print(f"the output would be: |{new1}")

#Print the last three characters
new2=str_manip[::-1]
new3=new2[0:3]
print(f"The last three characters are: {new3}")

#Create and print the first three characters and last two characters of str_manip and print the output
new4=str_manip[0:3]
new5=new2[0:2]
print("".join([new4,new5]))