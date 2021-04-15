# Secret Gui
# Mul Kang
# 24/2/21

'''
doesn't work

'''
# import the library
from appJar import gui


# Python 3 code to demonstrate the  
# working of MD5 (byte - byte) 
  
import hashlib 
  
# encoding secret using md5 hash   

# variables
result = hashlib.md5(b'admin') 
result2 = hashlib.md5(b'josh')   

# printing the equivalent byte value. 
print("The byte equivalent of hash is : ", end ="") 
print(result.hexdigest()) 
print("The byte equivalent of hash is : ", end ="") 
print(result2.hexdigest()) 



password_db = [
    ['josh','f94adcc3ddda04a8f34928d862f404b4'],
    ['admin','21232f297a57a5a743894a0e4a801fc3']
]

print(password_db[1][1])

# handle button events
def press(button):
    if button == "Cancel":
        app.stop()
    else:
        user_name = app.getEntry("Username")
        password = app.getEntry("Password")
        for x in password_db:
            if x[0] == user_name: # check if the username entered is in the list
                print('Username is same as stored username')
                saved_password = user_name
        print(saved_password)    
        hashed_password = hashlib.md5(password.encode('utf-8'))
        print(hashed_password.hexdigest())
        saved_password = hashlib.md5(saved_password.encode('utf-8'))
        print(saved_password.hexdigest())
        if hashed_password.hexdigest() == saved_password.hexdigest():
            print("Correct password entered")
            app.hideFrame('login')
            app.showFrame('secret')

# create a GUI variable called app
app = gui("Login Window", "400x200")
app.setBg("orange")
app.setFont(18)

# add & configure widgets - widgets get a name, to help referencing them later
with app.frame('login'):
    app.addLabel('title','hahaha')
    app.setLabelBg("title", "blue")
    app.setLabelFg("title", "orange")
    
    app.addLabelEntry("Username")
    app.addLabelSecretEntry("Password")
    
    # link the buttons to the function called press
    app.addButtons(["Submit", "Cancel"], press)
    
    app.setFocus("Username")

with app.frame('secret'):
    app.addLabel('secret','gamer')
    app.setLabelBg("secret", "blue")
    app.setLabelFg("secret", "orange")   
app.hideFrame('secret')
    
# start the GUI
app.go()

