# Mul Kang
# 8/3/21
# variables

""" 
Program that combines verbs
"""

# import the library
from appJar import gui




def update_button(rb): # parameter is radioButton
    verb = app.getRadioButton("Verb_1")   # verb is what the app.getRadioButton clicked
    adjective = app.getRadioButton("adj_1")
    app.setLabel("result","Fox say "+ verb + " Cat "+ adjective) 
    

# gui set up
app = gui("Thing I don't know how to make it work", "800x800")
app.setBg("orange")
app.setFont(18)

# title labe
app.addLabel("title",colspan=4)
app.setLabelBg("title", "blue")
app.setLabelFg("title", "orange")
app.setLabel("title", "cat")

# link the buttons to the function called update_button
app.addRadioButton("Verb_1","why.....",1,0)
app.addRadioButton("Verb_1","Ring-ding-ding-ding-dingeringeding!",2,0)  
app.setRadioButtonChangeFunction('Verb_1',update_button)


# is linked to adj_1 in the def function
app.addRadioButton("adj_1","cry",1,1)
app.addRadioButton("adj_1","meow",2,1)
app.setRadioButtonChangeFunction('adj_1',update_button) 

app.addRadioButton("ddd","cry",1,3)
app.addRadioButton("ddd","meow",2,3)
app.setRadioButtonChangeFunction('ddd',update_button) 

app.addLabel("result",colspan=1)
app.setLabelBg("result", "blue")
app.setLabelFg("result", "orange")
app.setLabel("result","I will stroke the cute cat")



app.go()
