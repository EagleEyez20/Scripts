#First I need to import the class that I want to use. Then I make the instance of the class usable by this chef.
from chef import Chef

class ChineseChef(Chef):    #<--Pay attention to the parenthesis, this is the inheritance with Chef.    
           
    def make_fried_rice(self):
        print("The chef makes fried rice")
        
    def make_specialer_dish(self):
        print("The chef makes orange chicken")
        
        
        
        #This goes with chef.py and Inheritance.py
        