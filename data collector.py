"""
Date:26/03/2021
Name: Aidan Whittaker
Description:
"""

# Imports
from appJar import gui
import json

# Variables
people_db = []  # for storing the people

# Functions


class Gui:
    """
    Class to set up and display gui
    Also manages the button events
    """

    def __init__(self):
        """
        Initialise the gui class in 2 columns including:
        - The top bar
        - the data collection frame
        - the data display window
        """
        self._people_index = 0
        # create a gui container

        app = gui("Awesome data collector", "400x400")

        self._app = app  # set the gui instance of _app to app

        app.addLabel("top_nav", "Collecting person data", 0, 0)
        app.addButton("top_nav_button", self.press, 0, 1)
        app.setButton("top_nav_button", "Show All")
        
        # shout to Callum
        
        read_from_file()

        # shout out Aidan
        with app.frameStack("stack"):
            with app.frame("data_collection"):
                app.addLabelEntry("First Name")
                app.addLabelNumericEntry("Age")
                app.addLabel("Do you have a mobile phone?")
                app.addRadioButton("question_1", "Yes")
                app.addRadioButton("question_1", "No")
                app.addButton("enter", self.press)

            with app.frame("data_display"):
                app.addLabel("first_name", "First name: ", 0, 0)
                app.addLabel("fname", "First_name_goes_here", 0, 1)
                app.addLabel("age_title", "Age: ", 1, 0)
                app.addLabel("age", "age_goes_here", 1, 1)
                app.addLabel("mobile_phone", "Mobile Phone: ", 2, 0)
                app.addLabel("mphone", "mobile_phone_goes_here", 2, 1)
                app.addButtons(["Prev", "Next"], self.press)

        app.firstFrame("stack")  # Sets the first frame added to stack to display first
        app.go()

    def fill(self, pos):
        """
        Changes the values of the labels in the frame to the new data for the person
        :param pos: Position of person object in array
        """
        for title, value in people_db[pos].get_person().items():
            # Need the name of the labels to be the same are the vars in person class
            new_title = title[1:len(title)]  # Removes the first character of the string
            # print(new_title)
            self._app.setLabel(new_title, value)

    def press(self, btn):

        if btn == "enter":
            people_db.append(Person(self._app.getEntry("First Name"), self._app.getEntry("Age"),
                                    self._app.getRadioButton("question_1")))
            write_to_file()
        if btn == "top_nav_button":
            if self._app.getButton("top_nav_button") == "Show All":
                self._app.nextFrame("stack")
                self._app.setButton("top_nav_button", "Add New")
                self.fill(self._people_index)
            else:
                self._app.prevFrame("stack")
                self._app.setButton("top_nav_button", "Show All")

        if btn == "Next":
            if self._people_index != len(people_db):
                self._people_index += 1
                self.fill(self._people_index - 1)

        if btn == "Prev":
            if self._people_index != 0:
                self._people_index -= 1
                self.fill(self._people_index)


class Person:
    def __init__(self, fname, age, mphone):
        """
        A object to hold information of a person
        :param fname: First name
        :param age: Persons age
        :param mphone: If they have a phone yes or no
        """
        self._fname = fname
        self._age = age
        self._mphone = mphone


    def get_person(self):
        """
        Gets variables
        :return: Dict of class variables
        """
        return vars(self)

def read_from_file():
    """gets data from file
       
    :returns array of data
    
    """
    global people_db
    
    with open('what.txt','r') as json_file:
        for object in json.load(json_file):
            people_db.append(Person(object["_fname"], object["_age"], object["_mphone"]))

def write_to_file():
    """ writes the name to the people_db
    
    :returns updated array
    """
    
    global people_db
    new_saving_way = []
    for person in people_db:
        new_saving_way.append(person.get_person())
        
    with open('what.txt','w') as json_file:
        json.dump(new_saving_way, json_file)
        


# main routine
data_collector = Gui()