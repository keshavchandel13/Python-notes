class base1:
    def show1(self):
        print("i am first base class")
class base2:
    def show2(self):
        print("I am second base class")
class multi(base1, base2):
    def show3(self):
        print("I am multilevel class consist of methods of base1 and base2")
object1 = multi()
object1.show1()
object1.show2()
object1.show3()