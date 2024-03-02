print("Hello, this is 1a experiment")
vr = str(input("enter input to store in string: "))
num = int(input("enter input to store in num: "))
flt = float(input("enter input to store in float: "))
bol = (input("input True or False: "))

if  bol== "True" or bol=="true" or bol == "1":
    bol=True
else: 
    bol =False 

print()
print(vr)
print (type(vr))
print()
print(num)
print (type (num))
print()
print(flt)
print (type (flt))
print()
print (bol)
print (type(bol))
print()