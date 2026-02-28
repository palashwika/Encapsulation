class Computer:

    def __init__(self):
        self.__maxprice=900

    def sell(self):
        print("Selling Price: {}".format(self.__maxprice))
    
    def setMaxPrice(self,price):
        self.__maxprice=price

c=Computer() #CALL CLASS WITH OBJECT
c.sell() #displays regular self.maxprice

c.__maxprice=1000
c.sell() #attempts to modify c.maxprice to 1000

#using setter function to modify price
c.setMaxPrice(1000)
c.sell()

