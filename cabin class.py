# Mul Kang
# 9/2/21
# Cabin

"""
Creates and manages cabin
"""



class Cabin: 
    def __init__(self, cabin_num, berths, cabin_type):
        self._cabin_num = cabin_num 
        self._berths = berths
        self._cabin_type = cabin_type
        self.occupied = False

    # def in class is method   
    def display_cabin(self): # <---
        print('**************************')
        print('Cabin Number: %s'% self._cabin_num)
        print('Berths: %s'%self._berths)
        print('Cabin Type: %s'%self._cabin_type)
        print('Occupied: %s'%self.occupied)
        
    
    def book_cabin(self):
        self.occupied = True
        
# create cabin

cabins = []
i = 1                     # i = iteration
while i < 6:
    cabins.append(Cabin(i,2,'Third Class')) 
    i += 1 
    

# user interface

def display_cabins():
    for cabin in cabins:
        cabin.display_cabin()
        
        
print('(d)isplay, (b)ook, (s)tats')
user_input = input()
if user_input == 'd':
    display_cabins()    
if user_input == 's':
    occupied_cabin = 0
    for cabin in cabins:
        if cabin._occupied == True:
            occupied_cabin += 1
    print('Occupied rate: ' +str(occupied_cabins/len(cabins)))
if user_input == 'b':
    user_input = input('cabin number >>> ')
    cabins[int(user_input)-1].book_cabin()
    
    
    
    
    