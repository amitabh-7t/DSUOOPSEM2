""" 1B develop a program to calculate the bill amount for a item given its quantity sold ,its value , discount and tax """
def newline():
    print("")

newline()
maximum_retail_price = float(input("enter the MRP :- "))
newline()
quantity= int(input("enter the qnt:- "))
newline()
discount = float (input("enter the discount % :- "))/100
newline()
total = quantity * maximum_retail_price 
total = total - (total*discount)
tax = float(input("enter the tax % :-  "))/100 
total = total + (tax*total)
newline()
print("grand price is:- ",total)
newline()