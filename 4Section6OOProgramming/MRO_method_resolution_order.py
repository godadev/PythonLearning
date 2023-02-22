class A():
    num = 10


class B(A):
    pass


class C(A):
    num = 10


class D(C, B):
    pass


print(D.mro())
D.num
