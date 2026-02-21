#Class creation
class myClass:

    #private variable
    __privateVar=28

#private method
    def __privMeth(self):
        print("Im insiude class myclass")

    #Function to print valye fo private variablee
    def hello(self): #not private
        print("Private variable value: ", myClass.__privateVar) #store private attributes in a different method so it can be called 


#Object creation and method call
foo=myClass() #foo is object of my class
foo.hello() 
foo.__privMeth