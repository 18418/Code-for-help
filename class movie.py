# Mul Kang
# 17/2/21
# Movie create class

from appJar import gui

movies = []

class Movie:
    def __init__(self, title, release_date, genre, rating):
        self._title = title
        self._release_date = release_date
        self._genre = genre
        self._rating = rating
        
    def get_title(self):
        return (self._title)
    
    def get_release_date(self):
        return (self._release_date)
    
    def get_genre(self):
        return (self._genre)
   
    def get_rating(self):
        return (self._rating)
    
    def display_movie(self):
        print('**************************')
        print('Name: %s'%self._title)
        print('Release Date: %d'%self._release_date)
        print('Genre: %s'%self._genre)
        print('Rating: %d'%self._rating)
        
    def get_display_string(self):
        display_string = '**********************\nTitle: %s\nRelease Date: %s\nGenre: %s\nRating: %s'%(self._title, self._release_date, self._genre, self._rating)
        return display_string

# create movies in database
        
movies.append(Movie('The Shawshank Redemption',1994,'Thriller',5))     
movies.append(Movie('The Godfather',1972,'Crime',4))
movies.append(Movie('The Dark Knight',2008,'Action',4))
movies.append(Movie('12 Angry Men',1957,'Crime',3))
movies.append(Movie('Schindlers List',1993,'Thriller',5))
movies.append(Movie('The Lord of the Rings: The Return of the King',2003,'Fantasy',3))
movies.append(Movie('Pulp Fiction',1994,'Action',5))
movies.append(Movie('The Good, the Bad and the Ugly',1966,'Action',4))
movies.append(Movie('The Lord of the Rings: The Fellowship of the Ring',2001,'Fantasy',5))
movies.append(Movie('Fight club', 1999, 'Action',5))

def start(button):
    """If start is pressed remove the start button and show other buttons."""
    app.removeButton("Start")
    app.addButtons(['5', "4", "action","Quit"], press)
    app.addTable("movie table", movie_array)    
    

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


    
    
    
def action():
    app.removeTable("movie table")
    movie_array.clear()
    movie_array.append(['Title','Genre','Release Date','Rating'])
    for movie in movies:
        if movie.get_genre() == 'Action':
            movie_array.append([movie.get_title(),movie.get_genre(),movie.get_release_date(),movie.get_rating()])
    app.addTable("movie table", movie_array)

def get_array():
    movie_array = [['Title','Genre','Release Date','Rating']]
    for movie in movies:
        movie_array.append([movie.get_title(),movie.get_genre(),movie.get_release_date(),movie.get_rating()])
    return movie_array

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
            
def endScreen():
    pass


# create a GUI variable called app
app = gui("Movie", "800x800")
app.setBg("orange")
app.setFont(17)

# add & configure widgets - widgets get a name, to help referencing them later
app.addLabel("title", "Welcome to movie")
app.setLabelBg("title", "pink")
app.setLabelFg("title", "white")

app.addLabel("main", "Movies")
app.setLabelBg("main", "white")

movie_array = get_array()

# link the buttons to the function called press

app.addButton('Start', start)

# start the GUI
app.go()


