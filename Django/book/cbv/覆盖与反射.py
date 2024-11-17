class Animals():
    xx = "=1"
    def __init__(self, name,age,func_str):
        self.name = name
        self.age = age
        self.sleep()
        print(self.xx)
        
        "反射"
        func = getattr(self,func_str)
        func()

    def sleep(self):
        self.sleep()
        print("sleep")
    
    def eat(self):
        print("eat")

class Dog(Animals):
    xx = "=2"
    def sleep(self):
        "父类会调用覆盖后的sleep"
        print("===sleep===")

dog = Dog("1","2","eat")


