# photo_slideshow
# Mul Kang

"""
show pics
Arrow navigation
buttons are disabled at either end

http://appjar.info/pythonImages?/#add-images
"""

# imports

from appJar import gui 

# variable
image_list = ["resized Whale.GIF","shock.GIF","akmu-background.GIF"]

# class

class Gui:
    def __init__(self):
        self._progress = 0 
        app = gui("I don't know how to make it happen", "900x700")
        app.setBg("orange")
        app.setFont(17)
        app.setImageLocation("Image")
        app.addButton("Exit",self.press)
    
        with app.frame('image'):
            app.addLabel('title','My fav pics')
            app.setLabelBg("title", "blue")
            app.setLabelFg("title", "orange")
            app.addImage("slide",image_list[self._progress])
            app.addButton(">>>",self.press)
            app.addButton("<<<",self.press)
            app.hideButton("<<<")

    
        self._app = app
    def start_app(self):
        self._app.go()
    
    def press(self,button):
        if button == "Exit":
            self._app.stop()   
        if button == ">>>":
            print(self._progress)
            self._progress += 1
            self._app.setImage("slide",image_list[self._progress])
            if self._progress == 0:
                self._app.hideButton("<<<")
            elif 2 > self._progress > 0:
                self._app.showButton("<<<")
            elif self._progress == 2:
                self._app.hideButton(">>>")
            else:
                print("sellss")
            
        if button == "<<<":
            print(self._progress)
            self._progress -= 1
            self._app.setImage("slide",image_list[self._progress])
            if self._progress == 0:
                self._app.hideButton("<<<")
            elif self._progress > 0:
                self._app.showButton("<<<")
                self._app.showButton(">>>")

# main routine




anything = Gui()
anything.start_app()
