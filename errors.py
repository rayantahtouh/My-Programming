
#Type of errors fixed:
#Syntax errors: Indentation is incorrect in a few places. Python relies on indentation to define blocks of code.
#Assignment mistake: Using == for assignment instead of = for the variable age_Str.
#Concatenation issue: Trying to concatenate a string with an integer without converting the integer to a string.
#Undefined variables: total and answer_years are undefined variables.

print ("Welcome to the error program") #SyntaxError: Missing parentheses in call to 'print'. Did you mean print("Welcome to the error program")?
print ("\n") #SyntaxError: Missing parentheses and unexpected indent

# Variables declaring the user's age, casting the str to an int, and printing the result
age_Str = "24 years old" #SyntaxError and unexpected indent
age = str(age_Str[:2]) #ValueError: invalid literal for int() with base 10: '24 years old'
print("I'm " + age + " years old.") #TypeError: can only concatenate str (not "int") to str

# Variables declaring additional years and printing the total years of age
years_from_now = 3 #SyntaxError unexpected indent
total_years = int(age) + years_from_now #TypeError: can only concatenate str (not "int") to str

print (f"The total number of years:{total_years}") #SyntaxError: Missing parentheses in call to 'print'. Did you mean print("The total number of years:" + "answer_years")?

# Variable to calculate the total amount of months from the total amount of years and printing the result
total_months = (total_years * 12) + 6 # Logical Error/NameError: name 'total' is not defined
print ("In 3 years and 6 months, I'll be " + str(total_months) + " months old") #SyntaxError: Missing parentheses in call to 'print'. Did you mean print("The total number of years:" + "answer_years")?
#TypeError: can only concatenate str (not "int") to str

