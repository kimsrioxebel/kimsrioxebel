class Mpesa:
    def __init__(self,account_balance,Phone_number):
        self.account_balance=account_balance
        self.Phone_number=Phone_number
    def send_money(self,amount,receipient):
     if self.account_balance>=amount:
          self.account_balance -=amount
          print(f"{amount} Kes sent to{receipient}successful")
     else:
            print("insufficient amount to send")

class Personal_mpesa(Mpesa):
    def __init__(self,account_balance,Phone_number,id_no):
        super(). __init__(account_balance,Phone_number)
        self.id_no=id_no
    def buy_airtime(self,amount):
        self.account_balance-=amount
        print(f"{amount}kes airtime bought successful")

class bussiness_mpesa(Mpesa):
    def __init__(self,account_balance,Phone_number,bussiness_id):
        super().__init__(account_balance,Phone_number)
        self.bussiness_id=bussiness_id
    def receive_payment(self,amount):
        self.account_balance+=amount
        print(f"{amount}kes receive from a customer")
personal=Personal_mpesa(account_balance="2000",Phone_number="0789078567",id_no="4567890")
personal.send_money(amount="4500",receipient="1000")