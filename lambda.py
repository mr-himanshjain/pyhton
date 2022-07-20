from ast import Lambda
import re


x = lambda a:a+5
print(x(5))

######################
y = lambda a,b : a * b
print(y(6,9))
#################

def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))
################################
def mysys(g):
    return lambda a : a * g
mysys2 = mysys(3)
print(mysys2(11))
####################################