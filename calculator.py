from operator import eq, truediv
import re;
print("our mgical calculator")
print("type quit to exit\n")
previous  = 0
run = True
def performMath():
    global run
    global previous
    equation = ""
    if previous == 0:
        equation  = input("enter equation: ")
    else: 
        equation = input(str(previous))

    if equation == 'quit':
        run = False
    else:
        equation = re.sub('[a-zA-Z,.:()+" "]','',equation)
        
        if previous == 0:
            previous = eval(equation)
        else:
            previous = eval(str(previous) + equation)
        # print("you types", previous)
while run:
    performMath()
