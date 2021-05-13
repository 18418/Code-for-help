# 7/4/21
# Mul Kang
# TED 31 Assessment 
# V1.0
"""
Haven't started
Just the beginning template.
My project is making
‘An ordering system for a take-away food shop’
"""

# import the library
from appJar import gui

# variables

menu_list = ["da","e"]

orders = []

progress = 0

#class
'''class Menu:
    # initilise class
    def __init__(self, name, price, food):
        self._name = name
        self._price = price 
        self._food = food
           
    def get_name(self):
        return (self._name)
       
    def get_price(self):
        return (self._price)
        
    def get_food(self):
        return (self._food)
       

        
menu_list.append(Menu('Cheese',14,'burger'))  
menu_list.append(Menu('Chicken',14,'burger'))  
menu_list.append(Menu('Beef',12,'burger'))  
menu_list.append(Menu('Fish',14,'burger'))  
'''
for x in range(len(menu_list)):
    print (menu_list[x],)
    
    
class Gui:
    def __init__(self):
        app = gui("Fast food menu", "800x800")
        app.setBg("orange")
        app.setFont(18)
        app.addLabel("title","Fast food order menu",colspan=2)
        app.setLabelBg("title", "blue")
        app.setLabelFg("title", "orange")
        app.addButton("Start", self.push) 
        app.addButton("Exit",self.push,row=0, column=0)
        app.addButton("Next",self.push,row=6, column=2)
        app.addButton("Previous",self.push,row=6, column=0)
    
        with app.frame('Burger',row=3, column=0):
            app.addLabel('burger_label','Burger')
            
        with app.frame("Drink"):
            app.addLabel('Drink_label','Drink')
            
        with app.frame("Sides"):
            app.addLabel('Sides_label','Sides')
        
        app.hideFrame('Drink')
        app.hideFrame('Sides')
        
        self._app=app
        app.go()
        
    def push(self, rb):
        print(rb)
        if rb == "Start":
            self._app.removeButton("Start")
        if rb == "Exit":
            self._app.stop()
        if rb == "Next":
            print("wow")
            Next(self, rb)
        else:
            pass
             
    def Next(self, rb):
        print("wow")
        
        


#If start is pressed remove the start ."""

window = Gui()
