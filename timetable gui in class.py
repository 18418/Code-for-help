# Gui in Class
# Mul Kang
# 12/3/21

'''
Gui class and Question class combine to make a fun single question quiz
'''
# import the library
from appJar import gui
import random


# variables


# Classes
class Gui:
    def __init__(self):
        app = gui("Thing I don't know how to make it work", "800x800")
        app.setBg("orange")
        app.setFont(18)
        app.addLabel("question_text") # add question labels
        app.setLabelBg("question_text", "blue")
        app.setLabelFg("question_text", "orange") 
        app.addLabelEntry("answer:  ")
        app.addButton("Check",self.check_correct)
        app.addButton("Next",self.next) # button linked to next
        app.addLabel("Result","")
    
        self._app = app  # set app to self._app so you don't have to write self._ everytime for other widgets
        self._number1 = random.randint(1,9)
        self._number2 = random.randint(1,9)        
        app.setLabel("question_text",str(self._number1) + "*" + str(self._number2))
        
    def start_app(self):
        self._app.go()  # start_app method starts the app.
        
    def check_correct(self):
        result = self._app.getEntry("answer:  ") # user Entry is same as result
        print(result)
        if int(result) == (self._number1 * self._number2): # if result is the same as the multiple
            self._app.setLabel("Result","Correct") # show correct
        elif int(result) != (self._number1 * self._number2): 
            self._app.setLabel("Result","InCorrect") # Incorrect
        except ValueError:
            print("123123")
      
        
    def next(self): # randomly sets the number
        self._number1 = random.randint(1,9)
        self._number2 = random.randint(1,9)         
        self._app.setLabel("question_text",str(self._number1) + "*" + str(self._number2))
        

    
    
    
# main routine
times_table_quiz = Gui()
times_table_quiz.start_app() # start_app here