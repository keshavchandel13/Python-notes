import time
import threading
class Bank:
    def __init__(self, customer_name, pin,interest_rate = 0.05):
        print("######## WELCOME TO LAXMI CHIT FUND BANK ###########")
        self.customer_name = customer_name
        self.pin = pin
        self.balance = 0.00
        self.interest_rate = interest_rate
        self.lock = threading.Lock()
    def deposit(self,amount):
      with self.lock:  
        self.balance+=amount
        print(f"{amount} successfully deposited to your account!")
    def withdraw(self,amount):
      with self.lock:
        if(self.balance<amount):
            print("Unable to make trasaction you have {self.balance} amount in your account")
        else:
            self.balance-=amount
            print("Transaction successfull!")
    def checkBalance(self):
      with self.lock:
        print(f"Balance: {self.balance}")
    def compute_interest(self):
        while True:
            time.sleep(30) 
            with self.lock:
                interest = self.balance * self.interest_rate
                self.balance += interest
                print(f"Interest of {interest} added. New Balance: {self.balance}")

Anshul = Bank("Anshul",6345)

interest_thread = threading.Thread(target=Anshul.compute_interest)
interest_thread.daemon = True
interest_thread.start()

Anshul.balance = 69
Anshul.deposit(500)
Anshul.checkBalance();
Anshul.withdraw(69)

Anshul.checkBalance();
while True:
    time.sleep(1)

        