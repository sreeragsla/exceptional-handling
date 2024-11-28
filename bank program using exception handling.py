class IncorrectpinError(BaseException):
    def __init__(self,msg):
        self.msg=msg

class InsufficientbalanceError(BaseException):
    def __init__(self,msg):
        self.msg=msg

class Bank:
    bank_name='SBI'
    bank_ifsc=1234
    bank_branch='Bangalore'
    bank_roi=7
    def __init__(self,cn,ca,cb,cacc,cp):
        self.customername=cn
        self.customerage=ca
        self.customerbalance=cb
        self.customeraccount=cacc
        self.customerpin=cp
    @staticmethod
    def get_int_value():
        val=int(input())
        return val
    def withdraw(self):
        pin=self.get_int_value()
        try:
            if pin==self.customerpin:
                amt=self.get_int_value()
                try:
                    if amt<=self.customerbalance:
                        self.customerbalance-=amt
                        print('Withdrawal Successfull')
                        print('Remaining Balance Is ',self.customerbalance)
                    else:
                        raise InsufficientbalanceError ('Insufficient Balance')
                except InsufficientbalanceError as IBE:
                    print(IBE)
            else:
                raise IncorrectpinError ('Incorrect Pin')
        except IncorrectpinError as IPE:
            print(IPE)
        finally:
            print('Thankyou')

RO=Bank('Ranbir',25,543210,12345,4321)
RO.withdraw()

        
