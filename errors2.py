# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

animal = 'Lion' #Logical Errors / NameError: name 'Lion' is not defined
animal_type = "cub"
number_of_teeth = 16

full_spec = "This is a {animal}. It is a {number_of_teeth} and it has {animal_type} teeth"

print (full_spec) #SyntaxError: Missing parentheses in call to 'print'. Did you mean print(full_spec)?