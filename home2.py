# 7/4/21
# Mul Kang
# TED 31 Assessment 
# V1.0
"""
My project is making
An ordering system for a take-away food shop
"""

# import the library
from appJar import gui

food_list = []

# movies = food_list

class Menu: # Movie = Menu
    def __init__(self, name, price, food_type):
        self._name = name
        self._price = price 
        self._food_type = food_type
           
    def get_name(self):
        return (self._name)
       
    def get_price(self):
        return (self._price)
        
    def get_food_type(self):
        return (self._food_type)
        
    '''def get_title(self):
        return (self._title)
    
    def get_release_date(self):
        return (self._release_date)
    
    def get_genre(self):
        return (self._genre)
   
    def get_rating(self): # Delete get rating
        return (self._rating)
    
    def display_movie(self):
        print('**************************')
        print('Name: %s'%self._title)
        print('Release Date: %d'%self._release_date)
        print('Genre: %s'%self._genre)
        print('Rating: %d'%self._rating)
        
    def get_display_string(self):
        display_string = '**********************\nTitle: %s\nRelease Date: %s\nGenre: %s\nRating: %s'%(self._title, self._release_date, self._genre, self._rating)
        return display_string'''

# create food in database
        

food_list.append(Menu('Cheese',14,'Burger'))  
food_list.append(Menu('Chicken',14,'Burger'))  
food_list.append(Menu('Beef',12,'Burger'))  
food_list.append(Menu('Fish',14,'Burger')) 
food_list.append(Menu('Water',1,'Drink'))  
food_list.append(Menu('Milk',14,'Drink'))  
food_list.append(Menu('Coke',12,'Drink'))  
food_list.append(Menu('Orange',14,'Drink'))  
food_list.append(Menu('Chips',14,'Sides'))  
food_list.append(Menu('Orange',14,'Sides'))  
food_list.append(Menu('Salad',12,'Sides'))  
food_list.append(Menu('Nugget',14,'Sides'))  



class Gui:
    def __init__(self):
        # create a GUI variable called app
        app = gui("Fast food menu", "800x800")
        app.setBg("orange")
        app.setFont(17)
        
        # add & configure widgets - widgets get a name, to help referencing them later
        app.addLabel("title","Fast food order menu",colspan=30)
        app.setLabelBg("title", "blue")
        app.setLabelFg("title", "orange")
        
        app.addLabel("main", "Menu")
        app.setLabelBg("main", "white")
        
        def press(button):
            if button == 'Quit':
                app.stop()
            if button == 'Drink':
                # app.hideButton("Drink")
                Drink1(self)
            if button == 'Sides':
                Sides(self)  
            if button == "Burger":
                Burger(self)
            if button == "Back":
                app.showFrame("Button_frame")
                app.hideFrame("Table_frame")
            else:
                pass
        
        # link the buttons to the function called press
        
        def start(button):
            """If start is pressed remove the start button and show other buttons."""
            app.removeButton("Start")
            app.showFrame("Button_frame")    
            app.showLabel("LABEL")
        
        def get(actionButton):
            print(actionButton)
 
                   
        def Sides(self): 
            food_array.clear()
            for x in food_list:
                if x.get_food_type() == "Sides":
                    food_array.append([x.get_name(),x.get_price(),x.get_food_type()])            
            app.replaceAllTableRows("food table", food_array, )
            app.hideFrame("Button_frame")
            app.showFrame("Table_frame") 
        
                             
        def Drink1(self):
            
            food_array.clear()
            for x in food_list:
                if x.get_food_type() == "Drink":
                    food_array.append([x.get_name(),x.get_price(),x.get_food_type()])            
            app.replaceAllTableRows("food table", food_array, )
            app.hideFrame("Button_frame")
            app.showFrame("Table_frame")
         
        def Burger(self):
            food_array.clear()
            for x in food_list:
                if x.get_food_type() == "Burger":
                    food_array.append([x.get_name(),x.get_price(),x.get_food_type()])
            app.replaceAllTableRows("food table", food_array, )
            app.hideFrame("Button_frame")
            app.showFrame("Table_frame")         
         
            # movie table = food table / movie_array = food_array
        
        def get_array(self):
            food_array = [['Name','Price','Type',]]
            for x in food_list:
                if x.get_food_type() == "Burger":
                    food_array.append([x.get_name(),x.get_price(),x.get_food_type()])
            return food_array
        
 
        app.addLabel("LABEL", "lol")    
        app.addButton('Start', start) 
        
        food_array = get_array(self)
        with app.frame("Table_frame"):
            app.addTable("food table", food_array, action=get, actionButton="Get") 
            app.addButton("Back", press)
        
        
        with app.frame("Button_frame"):
            app.addButtons(["Drink", "Sides","Burger","Quit"], press)
        app.hideFrame("Table_frame")
        app.hideFrame("Button_frame")
        app.hideLabel("LABEL")
           
        # start the GUI
        app.go()
        self._app=app
    
            
    

        
        




window = Gui()    
