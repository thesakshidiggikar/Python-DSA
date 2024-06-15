# class Methods:
#     @staticmethod # decorator= Function can run without "self" .
#     def welcome():
#         print("hello World!")

# s1=Methods()
# s1.welcome()

##Abstraction  = not showing the hidden items, only showing the function.

# class Cars:
#     def __init__(self):
#         self.clutch= False
#         self.acc=False
#         self.breek=False

#     def start(self):
#         self.acc=True #hidden ideam
#         self.clutch=True #hidden item
#         print("car Stared Brooooom!...")


#     def stop(self):
#         self.breek=True
#         print("car Stopped .......!!!!")

# s1=Cars()
# s1.start()
# s1.stop()


## Encapsulation = Making the data to be in one capsule  or in single unit(object)

# class Bankdetail:


#     def __init__(self, balance, acc):
#         self.balance=balance
#         self.acc=acc

#     def cr(self):
#         self.balance += amt
#         print("Money added")
#     def deb(self):
#         self.balance-= amt
#         print("money  Went away ! ")

#     def Bal(self):
#         return self.balance

# s1=Bankdetail(10000,2300)
# amt = 1000
# s1.cr()
# s1.deb()
# s1.Bal()


# OOps Concept
# del
## pvt attribute
# class Admission:
#     def __init__(self, name, prn):
#         self.name=name
#         self.__prn__=prn
#     def reset_passwd(self):
#         print(self.__prn__)

# s1=Admission("Sakshi","Anu")
# print(s1.name)
# # print(s1.prn)
# print(s1.reset_passwd())

# ______________________________________________________________________________
# private function
class Pvtfunc:
    __name="Ananymous"

    def __pvtattribute(self):
        print("Hello")


    def welcome(self):
        print(self.__pvtattribute)
        print("World!")

s1=Pvtfunc()
print(s1.welcome())
print(s1.welcome())
print(s1.welcome())
print(s1.welcome())
print(s1.welcome())
print(s1.welcome())
