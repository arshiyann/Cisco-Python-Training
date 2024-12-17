import time
class organization:
    def __init__(self):
        self.name = input('Enter Vendor Name: ')
        self.GST = input('Enter Vendor GST Number: ')
    def billing(self):
        self.product = input('Enter Product Name: ')
        self.qty = input('Enter Quantity: ')
        self.Cost = input('Enter Cost Value: ')
    def purchase_Info(self):
        file = open('purchaseinfo.log','w')
        file.write(self.product+','+self.qty+','+self.Cost)
        file.close()
obj1 = organization
obj1.__init__(obj1)
obj1.billing(obj1)

obj2 = organization
obj2.purchase_Info(obj2)
