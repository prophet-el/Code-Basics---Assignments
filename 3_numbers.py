# 1. You have a football field that is 92 metres long and 48.8 meter wide. Find out the total area using python and print it.
l = 92
w = 48.8
area = l * w
t_area = round(area)
print("The total area of the football field is:", t_area, " ","metres")

#2.You bought 9 packets of potato chips from store. Eachi packet cost 1.49 dollars.
#and you gave shopkeeper 20 dollar. Find out using python, how many dollars is the
#shopkeeper giving you back?

qty = 9
price = 1.49
t_price = qty * price
rec = 20 - t_price
print("The shopkeeper would give me", rec,"$ back")

#3. You want to replace the tiles in your bathroom which is exactly square and
#5.5 feet is its length. If tiles cost 500 rupees per square feet, how much
#will be the total cost to replace all tiles. Calculate and print cost using python

l = 5.5
t_area = 5.5**2
t_cost = t_area * 500
print("The total cost to replace all tiles is:",t_cost)

#4 put binary representation of number 17

ask = input("Enter the number:")
ask = int(ask)
print("The binary of the number",ask,"is", bin(ask)[2: ])



