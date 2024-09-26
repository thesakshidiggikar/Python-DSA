class A:
    def add(a, b):
        print(a + b)


class B(A):
    def add(self, a, b):
        super().add(a, b)

    def add(self, a, b, c):
        print(a + b + c)


ob1 = B()
ob1.add(1, 2)
ob1.add(1, 2, 3)
