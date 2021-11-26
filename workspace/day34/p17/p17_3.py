#%% 은
class BankError(Exception):
    def __init__(self, message):
        super().__init__(message)
        
        
class BankAccount:
    def __init__(self, acc_no, balance):
        self.acc_no = acc_no
        self.balance = balance
        
    def deposit(self, money):
        if money <= 0:
            raise BankError("%d원 입금 불가" %money)
        self.balance += money   
            
    def withdraw(self, money):
        if money <= 0:
            raise BankError("%d원 출금 불가" %money)
        if money > self.balance:
            raise BankError("잔액 부족")
        self.balance -= money
        return money
    
    def transfer(self, your_acc, money):
        your_acc.deposit(self.withdraw(money))
        
    def inquiry(self):
        print("계좌번호 : %s" %self.acc_no)
        print("통장잔액 : %d원" %self.balance)
            
me = BankAccount("1234", 50000)      
you = BankAccount("1111", 50000)      
        
        
try:
    # me.deposit(-1000)    
    # me.withdraw(-1000)    
    # me.withdraw(100000)    
    me.transfer(you, 5000)
except BankError as e:
    print(e)
finally:
    me.inquiry()
    you.inquiry()    
        
        
        
        