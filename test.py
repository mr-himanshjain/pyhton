# class Csd:
#     count = 1
#     def __init__(self):
#       self.count =self.count+1
#     @classmethod
#     def noOfobject(cls):
#         return cls.count
#     @staticmethod
#     def count1(count):
#         count = count+1
#     @classmethod
#     def count2(cls):
#         cls.count=cls.count+1

# c1=Csd()
# c2=Csd()
# c3=Csd()
# c1.count1(2)
# c1.count2()
# c2.count1(2)
# c2.count2()
# c3.count1(2)
# c3.count2()
# x=Csd.noOfobject()
# print(x)


# class csd:
#     x=10
#     def __init__(self):
#         self.y=20
# c1=csd()
# c2=csd()
# p=c1.x
# q=c1.y
# r=c2.x
# s=c2.y
# c1.x=100
# c2.y=1000
# print(c1.x+c1.y+c2.x+c2.y+p+q+r+s)


# class csd:
#     def m1(cls):
#         return 10,20,30,40
# c1=csd()
# x=c1.m1()
# for y in x[2:]:
#     print(y)

# import time
# class csd:
#     def __init__(self):
#         print(1,end="")
#     def __del__(sself):
#         print(2,end="")
# c1=csd()
# c2=csd()
# c3=c2
# del c1
# time.sleep(2)
# print(3,end="")
# del c3
# time.sleep(2)
# print(4,end="")
# print(5,end="")


# class csd:
#     x=10
#     def __init__(self):
#         self.y=100
#     def m1(self):
#         self.y=30

# c1=csd()
# c2=csd()
# c1.m1()
# print(c1.x+c1.y+c2.y)


# class csd:
#     x=10
#     def __init__(self):
#         self.y=20
    
# c1=csd()
# c2=csd()
# csd.x=100
# c2.y=1000
# print(c1.x+c1.y+c2.x+c2.y)

# def csd(*n1,n=100):
#     print(n)
#     print(n1)
# csd(10,20,30)

# def csd():
#     print("python fun")
# x=csd()
# y=csd
# y()
# x()

# import time
# class csd:
#     def __init__(self):
#         print("constructor")
#     def __del__(sself):
#         print("destructor")
# c1=csd()
# c2=c1
# c3=c2
# del c1
# time.sleep(2)
# print("cp")
# del c3
# time.sleep(2)
# print("cp1")
# print("end")

# class csd:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
#     def m1(self,z):
#         print(self.x+self.y-z)
# c=csd(10,20)
# csd.m1(30)

# class csd:
#     count=0
#     def __init__(self):
#         self.count=self.count+1
#     @classmethod
#     def noObjeft(cls):
#         return cls.count
# c1=csd()
# c2=csd()
# x=csd.noObjeft()
# c3=csd()
# c4=csd()
# c5=csd()
# y=csd.noObjeft()
# print(x+y)

# class csd:
#     x=100
#     def __init__(self):
#         self.y=200
    
# c1=csd()
# c2=csd()
# csd.x=500
# c1.x=600
# c2.y=700
# print(c1.x+c2.x+c1.y+c2.y+csd.x+csd.y)

# class csd:
#     a=10
#     def __init__(self):
#         self.b=30
    
# c1=csd()
# c2=csd()
# csd.a=1000
# c2.a=2000
# c1.b=3000
# print(c1.a+c1.b+c2.a+c2.b)