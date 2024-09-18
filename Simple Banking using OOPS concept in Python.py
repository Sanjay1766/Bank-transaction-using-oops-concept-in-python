class Bank():
    
    def __init__(self,bal,accno):
        self.bal=bal
        self.accno=accno
        
    def credit(self,amount):
        self.bal+=amount
        print("the amount credited towars your acc is",amount)
        print("your balance is ,",self.fetch_bal())
    
    def debit(self,amount):
        self.bal-=amount
        print("the amount debited from your account is,",amount)
        print("your balance is ,",self.fetch_bal())
       
        
    def fetch_bal(self):
        return self.bal
        
c1=Bank(10000,1224)
c2=Bank(20000,3647)
c3=Bank(30000,3737)

c1.credit(2000)