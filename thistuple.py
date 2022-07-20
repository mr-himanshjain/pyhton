thistuple=("banana",12,"cerry")
print(thistuple)
thislist = list(thistuple)
thislist[0]="strowberry"
print(thislist)
#################################
thislist.append("mango")
print(thislist)
###############################
thistuple = tuple(thislist)
print(thistuple)
##################################
z=("chocobar",)
thistuple += z
print(thistuple)
################################
#same process for removing a item from tuple make a tuple a list and then remove and then again make it tuple
################################
fruits = ("mango", "pineapple","banana")
(blue,red,green) = fruits
print(blue)
print(red)
print(green)
#######################################
fruits = ("mango", "pineapple","banana","cerry","kiwi","avacado")
(blue,*red,green) = fruits
print(blue)
print(red)
print(green)
#####################################
