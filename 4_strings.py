# 1. Create 3 variables to store street, city and country, now create address
# variable to store entire address. Use two ways of creating this variable,
# one using + operator and the other using f-string. Now Print the address
# in such a way that the street, city and country prints in a separate line

street = "Divya Vihar"
city = "Dehradun"
country = "India"
address = street + " " + city + " " + country
print("In a single line:",address)

street = "Divya Vihar"
city = "Dehradun"
country = "India"
address = street + "\n" + city + "\n" +country
print("In multiple lines using + operator:",address)

street = "Divya Vihar"
city = "Dehradun"
country = "India"
address = f"{street}\n{city}\n{country}"
print("In mutiple lines using f string:","\n",address)
print(type(address))

# 2.create a variable to store "Earth revolves around the sun"
# (i) Print "revolve" using slice operator
# (ii) Print "sun" using negative index

str1 = "Earth revolves around the sun"
print(type(str1))
str2 = list(str1.split(" "))
print(type(str2))
print(str2)
print(str2[1:2])
print(str2[-1:])

#3. Create two variables to store how many fruits and vegetables you eat
# in a day. Now Print "I eat x veggies and y fruits daily" where x and y presents vegetables and fruits that you eat everyday.
# Use python f string for this.
num_f = 6
num_v = 4
print(f"I eat {num_v} vegetable and {num_f} fruits in a day ")

#4. I have a string variable called s='maine 200 banana khaye'.
# This of course is a wrong statement, the correct statement is 'maine 10 samosa khaye'.
# Replace incorrect words in original strong with new ones and print the new string.
# Also try to do this in one line.

s = "maine 200 banana khaye"
s = s.replace("200","10").replace("banana","samose")
print(s)