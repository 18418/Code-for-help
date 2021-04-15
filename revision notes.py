# year 11 revision
# Mul Kang

### imports = selection of python commands we need to import to use
import random # generates randomness in your code
import datetime # lets you use the computer time in your programs

### variables
number_one = 1 # int
number_two = 2.2 # float
true_or_false = False # boolean
test_string = 'A stored string'
my_list = ['Josh',12,56,'Blue',number_one, number_two, true_or_false]

### string stuff

print('Hi %s, python %s strings are formatted %s like this'%(test_string, number_one, true_or_false))
### %s = format as string, %d = format as int, %f = format as float, %.2f = 2 decimal places.

### user input = the input() function

#user_input = input('Ask your question here, it gets stored in the user_input variable you just made \n>>> ')
### remember input() gets input from the user as a STRING. You need to convert it to an int or float if you
### want to do maths with it. Like this:

#user_age = int(input('What is your age? '))
#print('In 10 years you will be %d'% (user_age + 10))

### list stuff

#print(my_list) # show the whole list
#print(my_list[3]) # print the fourth item (index starts at 0)
#my_list.remove(2.2) # remove the item False
#my_list.remove(my_list[2])
#print(my_list)
#my_list.append('Sunflower') # add an item to the list
#print(my_list)
#print(len(my_list)) # returns the number of items in a list
#print(my_list.index('Blue')) # tells you where 'Blue' is

### looping lists - sometimes we need to go through the list
'''
for list_item in my_list: # you can make up a nice name for your list items
    print(list_item)
'''
### displaying lists cool
'''
list_string = '' # make a blank list
for list_item in my_list:
    list_string += str(list_item)+'\t'
print(list_string)
'''

### displaying lists really cool
'''
list_string = '' # make a blank list
for list_item in my_list:
    if my_list.index(list_item) % 3 == 2:
        list_string += str(list_item)+'\n'
    else:
        list_string += str(list_item)+'\t'
print(list_string)
'''

### I probably got carried away on lists
### Selection = if elif else = choosing what to do.

'''
# checks the condition, does it if it's supposed to, moves on
if number_one > 7:
    print('do this')

# only runs if the 'if' before it didnt. Checks new condition. Possibly goes
elif number_one < 0:
    print('do that')

# only runs if the if and elifs before it didnt. 
else:
    print('None of those things happened')
'''

### nested ifs - you can go as many ifs deep as you want. Remember -
### = for setting a variable
### == for comparing - equal to
### != not equal to
### > greater than < less than

'''
if number_one == 1:
    if number_two == 2.2:
        if true_or_false == False:
            if my_list[3] == 'Blue':
                print('All those conditions were met')
        else:
            print('Only happens if the first two were and third wasnt')
    else:
        print('Second one cant have been what we thought')
else:
    print('number_one obviously wasnt one')
'''

### back to those imports

### basic time and date things
'''
now = datetime.datetime.now()
print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
'''

### basic random commands

#print(random.choice(my_list))
#print(random.randint(1,10)) # random number between 1 and 10


'''def sort_list(list):
        for list_item in num_list:
                
                if num_list.index(1) > num_list.index(2):
                        num_list[0], num_list[2] = num_list[2], num_list[0]
                        print(num_list)
                
                
        
sort_list(list)
        '''
                            
def sort(x):
    l=len(x)
    for i in range(l):
        for j in range((i+1),l):
            if x[i]>x[j]:
                l1=x[i]
                x[i]=x[j]
                x[j]=l1
    print(x)                
l=[15, 21, 4, 7, 13, 45, 78, 12]
sort(l)