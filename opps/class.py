# class Cars: #Class
#     car1="BMW"

# c1=Cars()  #object to call that function
# print(c1.car1)


# init constructor
# class instrutor1:
#     #comon attribute
#     brand_name="Brandzone" #class attribute
#     def __init__(self, BrandName): #parameters
#         self.name=BrandName
#         print("New Brand Added")

# s1 = instrutor1("BMW") #add parameters
# print(s1.name)

# s2 = instrutor1("Tesla") #object attribute
# print(s1.name)

# print(s1.brand_name, s1.name)

# Condition question.


class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def avgcal(self):
        sum = 0
        for i in self.marks:
            sum += i
        print("Hi!",self.name," your average score is ", sum / 3)


s1 = Student("Anu", [89, 90, 98])
s2 = Student("Sakshi", [94.91, 87])
s3 = Student("Shreyash", [99, 83, 98])
s3.avgcal()
