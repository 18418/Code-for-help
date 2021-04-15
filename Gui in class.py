# Gui in Class
# Mul Kang
# 10/3/21

'''
Gui class and Question class combine to make a fun single question quiz
'''
# import the library
from appJar import gui
import random

# one question quiz


# class definitions
class Question:
    # initilise class
    def __init__(self, question, answers, correct_answer):
        self.question = question
        self.answers = answers 
        self.correct_answer = correct_answer      
    # returns True if correct answer is selected
    def check_correct(self, selected_answer):
        if selected_answer == self.correct_answer:
            _correct = True
            return _correct
        else:
            _correct = False
            return _correct  
    # returns array of all possible answers
    def get_answer_array(self):
        _answer_array = self.answers
        _answer_array.append(self.correct_answer)
        return _answer_array
    # returns the answer text
    def get_question_text(self):
        return self.question



class Gui:
    def __init__(self):
        app = gui("Thing I don't know how to make it work", "800x800")
        app.setBg("orange")
        app.setFont(18)
        app.addLabel("title",colspan=2)
        app.setLabelBg("title", "blue")
        app.setLabelFg("title", "orange")
        app.setLabel("title", question.get_question_text())
        random.shuffle(question.get_answer_array()) # Randomise the questions
        
        app.addRadioButton("ans",question.get_answer_array()[0],1,1)
        app.addRadioButton("ans",question.get_answer_array()[1],2,1)   
        app.addRadioButton("ans",question.get_answer_array()[2],3,1)    
        app.addRadioButton("ans",question.get_answer_array()[3],4,1)        
        
        app.setRadioButtonChangeFunction('ans',self.push)
        
        
        
        app.addLabel("result",colspan=2)
        
        self._app=app
        
        app.go()
    
    def push(self, rb):
        print(rb)
        if self._app.getRadioButton(rb) == question.correct_answer:
            self._app.setLabel("result","Correct")
        else:
            self._app.setLabel("result","Wrong")
            
    
        
question = Question("What day is it today?",["Mon","Tue","Wed"],"Thurs")

        

anything = Gui()	