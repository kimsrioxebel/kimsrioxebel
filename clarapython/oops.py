class Fruits:
    def __init__(self,name,price):
        self.name=name
        self.price=price

    def display(self):
        print(f"this is my favourite fruit{self.name}"
              f"and it cost{self.price}")

Myobj=Fruits("ORANGE",34)
Myobj1 = Fruits("Apple", 70)
Myobj2=Fruits("Mangoe",35)
Myobj3=Fruits("Banana",30)
Myobj4=Fruits("Watermelon",45)
Myobj1.display()
Myobj2.display()
Myobj3.display()
Myobj4.display()
Myobj.display()


