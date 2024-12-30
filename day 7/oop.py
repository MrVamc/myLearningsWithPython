print("--- Example 1 : defining a class ---")
class Myclass:
    def myFun(self):
        pass
    def myFun1(self,name):
        print(name)

mc1 = Myclass()
mc1.myFun()
mc1.myFun1('vamshi')
print("=======================================")

print("--- Example 2 : defining static and non static methods ---")

class Myclass1:
    def myFun2(self):
        print("Instance method")

    @staticmethod
    def myFun3(self,name):
        print("My name is : ",name)

mc2 = Myclass1()
mc2.myFun2()
mc2.myFun3('Hi','Vamshi') # in static method self is considered as parameter
# we can call static method using class name as well
Myclass1.myFun3(100,'Varun')
print("===========================================")

print("--- Example 3 : class variables ---")
class Myclass2:
    a,b = 10,20 #class variables
    def add(self):
        print(self.a+self.b)

    def mul(self):
        print(self.a*self.b)

mc3 = Myclass2()
mc3.add()
mc3.mul()

print("===============================================")


print("--- Example 4 : Global, class and local variables ---")
i, j = 15,25 # global variable
class Myclass4:
    c,d = 30,35 # class variable
    def add1(self,x,y): # local variable
        print(x+y)
        print(self.c+self.d)
        print(i+j)

mc4 = Myclass4()
mc4.add1(5,10)

print("=================================================")

print("--- Example 5 : Global, local and class varibale with same reference name ---")
e,f = 40,45
class Myclass5():
    e,f = 50,55
    def add2(self,e,f):
        print(e+f)
        print(self.e+self.f)
        print(globals()['e']+globals()['f'])

mc5 = Myclass5()
mc5.add2(60,65)
print("=====================================================")

print("--- Example 6 : Creating Constructor ---")
class Myclass6:
    def __init__(self):
        print("Iam constructor")

    def clss4(self):
        print("Hello constructor")

mc6 = Myclass6()
mc6.clss4()

print("===========================================================")
