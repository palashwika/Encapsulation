class Reverse:
    def __init__(self):
        self.__s=input("Enter a string ")

    
    def display(self):
       print("The reversed string is: ",self.__s[::-1])

user=Reverse()
user.display()