import re


def start(x):
    print(x)
    return
print("hello")
start(10)
###########################################
def second(a,b):
    print(a,b)
    return
a=40
second(a,55)
#######################################
def second(q,ty):
    print(q,ty)
    return
second(34,ty=55)
#########################################
def second(o,*t):
    print(o,t)
    return
second(23,55,54,66,23)
##########################################
def second(o,*t):
    print(o,t)
    for i in t:
        print(i)
    return
second(23,55,54,66,23)

######################################
#pass by refrence
n=[3,6,2,7]
def pbr(x):
    x[2]=44
    print(x)
    return
pbr(n)
print(n)

###########################
