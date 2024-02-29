class people:
    def __init__(self,name,course):
        self.name=name
        self.course=course

class Fruits:
    def __init__(self, name, price):
            self.name = name
            self.price = price

    def display(self):
            print(f"this is my favourite fruit{self.name}"
                  f"and it cost{self.price}")
            Myobj = Fruits("ORANGE", 34)
Myobj1 = Fruits("Apple", 70)

Myobj1.display()
Myobj.display()


  def onyesha(Self):
        print(f"my name is {self.name}"
              f"i take{self.course}")

Myobj=people("clara","computer science")
Myobj.onyesha()