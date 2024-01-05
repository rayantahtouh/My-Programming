# The user's favorite restaurant name
string_fav=input("Please enter the name of your favorite restaurant: ")

# Taking the user's favorite number
int_fav=int(input("Enter your favorite number: "))

print(string_fav)
print(int_fav)

# Cast string_fav to int:

new=int(string_fav)
#ValueError
#if string_fav contains characters that cannot be converted to an integer (for example, if it's a string like Roadster"), it will raise a ValueError
#Strings that do not represent valid integers will cause this error when trying to cast them using int().