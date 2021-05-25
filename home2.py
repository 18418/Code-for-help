# Mul Kang
# 17/2/21
# Movie create class

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

# create movies in database
        

food_list.append(Menu('Cheese',14,'burger'))  
food_list.append(Menu('Chicken',14,'burger'))  
food_list.append(Menu('Beef',12,'burger'))  
food_list.append(Menu('Fish',14,'burger'))  



class Gui:
    def __init__(self):
        app = gui("Fast food menu", "800x800")
        app.setBg("orange")
        app.setFont(17)
        
        # add & configure widgets - widgets get a name, to help referencing them later
        app.addLabel("title","Fast food order menu",colspan=30)
        app.setLabelBg("title", "blue")
        app.setLabelFg("title", "orange")
        
        app.addLabel("main", "Movies")
        app.setLabelBg("main", "white")
        
        def press(button):
            if button == 'Quit':
                app.stop()
            if button == '5':
                five_star()
            if button == '4':
                four_star()
            if button == 'action':
                action()  
            else:
                pass
        
        # link the buttons to the function called press
        
        def start(button):
            """If start is pressed remove the start button and show other buttons."""
            app.removeButton("Start")
            app.addButtons(['5', "4", "action","Quit"], press)
            app.showFrame("Table_frame")         
        
        
        def action():
            app.removeTable("movie table")
            movie_array.clear()
            movie_array.append(['Title','Genre','Release Date','Rating'])
            for movie in movies:
                if movie.get_genre() == 'Action':
                    movie_array.append([movie.get_title(),movie.get_genre(),movie.get_release_date(),movie.get_rating()])
            app.addTable("food table", food_array)
            # movie table = food table / movie_array = food_array
        
        def get_array(self):
            food_array = [['Name','Price','Type',]]
            for x in food_list:
                food_array.append([x.get_name(),x.get_price(),x.get_food_type()])
            return food_array
        

                    
        def endScreen():
            pass
        
        
 
            
        
        def five_star():
            movie_array.clear()
            movie_array.append(['Title','Genre','Release Date','Rating'])
            for movie in movies:
                if movie.get_rating() > 4:
                    movie_array.append([movie.get_title(),movie.get_genre(),movie.get_release_date(),movie.get_rating()])
        
        def four_star():
            app.removeAllWidgets()
            movie_array.clear()
            movie_array.append(['Title','Genre','Release Date','Rating'])
            for movie in movies:
                if movie.get_rating() > 3:
                    movie_array.append([movie.get_title(),movie.get_genre(),movie.get_release_date(),movie.get_rating()])
            app.addLabel("title", "Welcome to movie")
            app.setLabelFg("title", "white")
            app.addLabel("main", "Movies")
            app.setLabelBg("main", "white")         
            app.addTable("movie table", movie_array)
            app.addButtons(['5', "4", "action","Quit"], press)     
            
    
            # create a GUI variable called app    
        app.addButton('Start', start)
        food_array = get_array(self)
        with app.frame("Table_frame"):
            app.addTable("movie table", food_array,action=press,actionButton="Get")   
            
        app.hideFrame("Table_frame")

        # start the GUI
        app.go()
        self._app=app
    
            
    

        
        




window = Gui()    
    
    
    
    
    

