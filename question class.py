# Mul Kang
# 1/3/21
# Question class

'''
3 question quiz program 
Uses a Question class 
Gui display
Results window
Doesn't work.
Don't know how to set one of the buttons to answer
'''

from appJar import gui
import random

# variables
question_db = []
quiz_progress = 0

# class definition
class Question:
    def __init__(self, question, answers, correct_answer):
        self.question = question
        self.answers = answers
        self.correct_answer = correct_answer
    
    ####################I didn't know how to use the True False boolean in the quiz#####################   
    '''def check_correct(self, selected_answer):
        if selected_answer == self.correct_answer:
            _correct = True
            return _correct
        else:
            _correct = False
            return _correct'''   
     # returns True if correct answer is selected
    def check_correct(self):
        return self.correct_answer   
    
    # returns array of all possible answers
    def get_answer_array(self):
        _answer_array = self.answers
        return _answer_array
    
    # returns answer text
    def get_question_text(self):
        return self.question


question_db.append(
    Question("Who wrote war and peace?",
             ["Austin","Pratchett","Wells","Tolstoy"],
             "Tolstoy"))
question_db.append(
    Question("What is the capital of Russia?",
             ["Kiev","Minsk","Warsaw","Moscow"],
             "Moscow"))
question_db.append(
    Question("What is Russia's national animal?",
             ["heraldic Federal Eagle","Gallic rooster","Snow leopard","Eurasin brown bear"],
             "Eurasin brown bear"))

random.shuffle(question_db[quiz_progress].get_answer_array()) # random shuffle
print(question_db[quiz_progress].check_correct())

# functions
def press(button):
    global quiz_progress 
    if button == "start_quiz":
        app.hideFrame("Welcome")
        app.showFrame("questions")
        print(app.button(1),'loloo')
        print(question_db[quiz_progress].correct_answer)        
    elif button == 'Tolstoy': # I didn't know this part
        random.shuffle(question_db[quiz_progress].get_answer_array()) 
        app.hideFrame("questions")
        app.showFrame("Correct_frame")
    elif button != question_db[quiz_progress].correct_answer:
        next_question()
    elif button == "next":
        next_question()


def next_question():
    global quiz_progress 
    app.hideFrame("questions")
    app.hideFrame("Correct_frame")
    quiz_progress += 1
    print(quiz_progress)

# create a GUI variable called app
app = gui("Movie", "800x800")
app.setBg("orange")
app.setFont(17)

# add & configure widgets - widgets get a name, to help referencing them later
with app.frame("Welcome"):
    app.addLabel("title", "Welcome to movie")
    app.setLabelBg("title", "pink")
    app.setLabelFg("title", "white")
    app.addLabel("main", "Quiz")
    app.setLabelBg("main", "white")
    app.addButton("start_quiz",press)
    
with app.frame("questions"):
    app.addLabel("question_label","")
    app.setLabel("question_label",question_db[quiz_progress].get_question_text())    
    app.addButton(1,press) # random
    app.addButton(2,press) # random name
    app.addButton(3,press) # random name
    app.addButton(4,press) # random
    possible_answers = question_db[quiz_progress].get_answer_array()
    i = 1
    for x in possible_answers:
        app.setButton(i,x)
        i+=1
                                                                                                                                                                                                                                                          
        
with app.frame("Correct_frame"):
    app.addLabel("Correct_label","Correct")
    app.addButton("next",press)
    
     

    
    
app.hideFrame("questions")
app.hideFrame("Correct_frame")

# link the buttons to the function called press

# start the GUI
app.go()

