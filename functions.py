import email
from operator import eq


def hello():
    print("hello",a)
def information():
    print("we have collect your information \n")
    print("your age is :",age)
    print("your gender is: ",gen)
    print("your email address is: ",email)
def check():
    print("if the information are correct write yes and if the information are wrong write no")
    c=str(input("yes/no : "))
    if c == "yes":
        print("wow welcome ",a)
    else:
        print("better to try later")
a=str(input("enter your name: "))
hello()
age=int(input("enter your age: "))
gen=str(input("enter your gender: "))
email=str(input("enter your email: "))
information()
check()