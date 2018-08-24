class Person:
    def __init__(self,name,age,city,number):
        self.name=name
        self.age=age
        self.city=city
        self.number=number

    def __str__(self):
        return self.name+" is "+str(self.age)+", lives in "+self.city+", and their phone number is "+str(self.number)

def start():
    n=input("Name: ")
    a=input("Age: ")
    c=input("City: ")
    p=phone()
    p1=Person(n,a,c,p)
    print(p1)

def phone():
    while True:
        try:
            return int(input("Phone: "))
        except ValueError:
            print("Please enter numbers only")
start()
