#-----Statement of Authorship----------------------------------------#
#
#  This is an individual assessment item.  By submitting this
#  code I agree that it represents my own work.  I am aware of
#  the University rule that a student must not act in a manner
#  which constitutes academic dishonesty as stated and explained
#  in QUT's Manual of Policies and Procedures, Section C/5.3
#  "Academic Integrity" and Section E/2.1 "Student Code of Conduct".
#
#    Student no: n10493298

#    Student name: Laku Jackson
#
#  NB: Files submitted without a completed copy of this statement
#  will not be marked.  All files submitted will be subjected to
#  software plagiarism analysis using the MoSS system
#  (http://theory.stanford.edu/~aiken/moss/).
#
#---------------------------------------------------
#----------------- 



#-----Assignment Description-----------------------------------------#
#
# PATIENCE
#
# This assignment tests your skills at processing data stored in
# lists, creating reusable code and following instructions to display
# a complex visual image.  The incomplete Python program below is
# missing a crucial function, "deal_cards".  You are required to
# complete this function so that when the program is run it draws a

# game of Patience (also called Solitaire in the US), consisting of
# multiple stacks of cards in four suits.  See the instruction sheet
# accompanying this file for full details.
#

# Note that this assignment is in two parts, the second of which
# will be released only just before the final deadline.  This
# template file will be used for both parts and you will submit
# your final solution as a single Python 3 file, whether or not you
# complete both parts of the assignment.
#
#--------------------------------------------------------------------#  



#-----Preamble-------------------------------------------------------#
#
# This section imports necessary functions and defines constant
# values used for creating the drawing canvas.  You should not change
# any of the code in this section.
#

# Import the functions needed to complete this assignment.  You
# should not need to use any other modules for your solution.  In
# particular, your solution must NOT rely on any non-standard Python
# modules that need to be installed separately, because the markers
# will not have access to such modules.

from turtle import *
from math import *
from random import *

# Define constant values used in the main program that sets up
# the drawing canvas.  Do not change any of these values.

# Constants defining the size of the card table
table_width = 1100 # width of the card table in pixels
table_height = 600 # height (actually depth) of the card table in pixels
canvas_border = 30 # border between playing area and window's edge in pixels
half_width = table_width // 2 # maximum x coordinate on table in either direction
half_height = table_height // 2 # maximum y coordinate on table in either direction

# Work out how wide some text is (in pixels)
def calculate_text_width(string, text_font = None):
    penup()
    home()
    write(string, align = 'left', move = True, font = text_font)
    text_width = xcor()
    undo() # write
    undo() # goto
    undo() # penup
    return text_width


# Constants used for drawing the coordinate axes
axis_font = ('Consolas', 10, 'normal') # font for drawing the axes
font_height = 14 # interline separation for text
tic_sep = 50 # gradations for the x and y scales shown on the screen
tics_width = calculate_text_width("-mmm -", axis_font) # width of y axis labels

# Constants defining the stacks of cards
stack_base = half_height - 25 # starting y coordinate for the stacks
num_stacks = 6 # how many locations there are for the stacks
stack_width = table_width / (num_stacks + 1) # max width of stacks
stack_gap = (table_width - num_stacks * stack_width) // (num_stacks + 1) # inter-stack gap
max_cards = 10 # maximum number of cards per stack

# Define the starting locations of each stack
stack_locations = [["Stack " + str(loc + 1),
                    [int(-half_width + (loc + 1) * stack_gap + loc * stack_width + stack_width / 2),
                     stack_base]] 
                    for loc in range(num_stacks)]

# Same as Turtle's write command, but writes upside down
def write_upside_down(string, **named_params):
    named_params['angle'] = 180
    tk_canvas = getscreen().cv
    tk_canvas.create_text(xcor(), -ycor(), named_params, text = string)

#
#--------------------------------------------------------------------#



#-----Functions for Creating the Drawing Canvas----------------------#
#
# The functions in this section are called by the main program to
# create the drawing canvas for your image.  You should not change
# any of the code in this section.
#

# Set up the canvas and draw the background for the overall image.
# By default the coordinate axes displayed - call the function
# with False as the argument to prevent this.
def create_drawing_canvas(show_axes = True):

    # Set up the drawing canvas
    setup(table_width + tics_width + canvas_border * 2,
          table_height + font_height + canvas_border * 2)

    # Draw as fast as possible
    tracer(False)

    # Make the background felt green and the pen a lighter colour
    bgcolor('green')
    pencolor('light green')


    # Lift the pen while drawing the axes
    penup()
    
    

    # Optionally draw x coordinates along the bottom of the table
    if show_axes:
        for x_coord in range(-half_width + tic_sep, half_width, tic_sep):
            goto(x_coord, -half_height - font_height)
            write('| ' + str(x_coord), align = 'left', font = axis_font)

    # Optionally draw y coordinates to the left of the table
    if show_axes:
        max_tic = int(stack_base / tic_sep) * tic_sep
        for y_coord in range(-max_tic, max_tic + tic_sep, tic_sep):
            goto(-half_width, y_coord - font_height / 2)
            write(str(y_coord).rjust(4) + ' -', font = axis_font, align = 'right')

    # Optionally mark each of the starting points for the stacks
    if show_axes:
        for name, location in stack_locations:
            # Draw the central dot
            goto(location)
            color('light green')
            dot(7)
            # Draw the horizontal line
            pensize(2)
            goto(location[0] - (stack_width // 2), location[1])
            setheading(0)
            pendown()
            forward(stack_width)
            penup()
            goto(location[0] -  (stack_width // 2), location[1] + 4)
            # Write the coordinate
            write(name + ': ' + str(location), font = axis_font)

    #Draw a border around the entire table
    penup()
    pensize(3)
    goto(-half_width, half_height) # top left
    pendown()
    goto(half_width, half_height) # top
    goto(half_width, -half_height) # right
    goto(-half_width, -half_height) # bottom
    goto(-half_width, half_height) # left

    # Reset everything, ready for the student's solution
    pencolor('black')
    width(1)
    penup()
    home()
    tracer(True)


# End the program and release the drawing canvas.

# By default the cursor (turtle) is hidden when the program
# ends - call the function with False as the argument to
# prevent this.
def release_drawing_canvas(hide_cursor = True):
    tracer(True) # ensure any partial drawing in progress is displayed
    if hide_cursor:
        hideturtle()
    done()
    
#
#--------------------------------------------------------------------#



#-----Test Data for Use During Code Development----------------------#
#
# The "fixed" data sets in this section are provided to help you
# develop and test your code.  You can use them as the argument to
# the deal_cards function while perfecting your solution.  However,
# they will NOT be used to assess your program.  Your solution will
# be assessed using the random_game function appearing below.  Your
# program must work correctly for any data set that can be generated
# by the random_game function.
#

# Each of these fixed games draws just one card
fixed_game_0 = [['Stack 1', 'Suit A', 2, 0]]
fixed_game_1 = [['Stack 2', 'Suit B', 1, 0]]
fixed_game_2 = [['Stack 3', 'Suit C', 1, 0]]
fixed_game_3 = [['Stack 4', 'Suit D', 1, 0]]

# Each of these fixed games draws several copies of just one card
fixed_game_4 = [['Stack 2', 'Suit A', 4, 0]]
fixed_game_5 = [['Stack 3', 'Suit B', 3, 0]]
fixed_game_6 = [['Stack 4', 'Suit C', 2, 0]]
fixed_game_7 = [['Stack 5', 'Suit D', 5, 0]]

# This fixed game draws each of the four cards once
fixed_game_8 = [['Stack 1', 'Suit A', 1, 0],
                ['Stack 2', 'Suit B', 1, 0],
                ['Stack 3', 'Suit C', 1, 0],
                ['Stack 4', 'Suit D', 1, 0]]

# These fixed games each contain a non-zero "extra" value
fixed_game_9 = [['Stack 3', 'Suit D', 4, 4]]
fixed_game_10 = [['Stack 4', 'Suit C', 3, 2]]
fixed_game_11 = [['Stack 5', 'Suit B', 2, 1]]
fixed_game_12 = [['Stack 6', 'Suit A', 5, 5]]

# These fixed games describe some "typical" layouts with multiple
# cards and suits. You can create more such data sets yourself
# by calling function random_game in the shell window

fixed_game_13 = \
 [['Stack 6', 'Suit D', 9, 6],
  ['Stack 4', 'Suit B', 5, 0],
  ['Stack 5', 'Suit B', 1, 1],
  ['Stack 2', 'Suit C', 4, 0]]
 
fixed_game_14 = \
 [['Stack 1', 'Suit C', 1, 0],
  ['Stack 5', 'Suit D', 2, 1],
  ['Stack 3', 'Suit A', 2, 0],
  ['Stack 2', 'Suit A', 8, 5],
  ['Stack 6', 'Suit C', 10, 0]]

fixed_game_15 = \
 [['Stack 3', 'Suit D', 0, 0],
  ['Stack 6', 'Suit B', 2, 0],
  ['Stack 2', 'Suit D', 6, 0],
  ['Stack 1', 'Suit C', 1, 0],
  ['Stack 4', 'Suit B', 1, 1],
  ['Stack 5', 'Suit A', 3, 0]]

fixed_game_16 = \
 [['Stack 6', 'Suit C', 8, 0],
  ['Stack 2', 'Suit C', 4, 4],
  ['Stack 5', 'Suit A', 9, 3],
  ['Stack 4', 'Suit C', 0, 0],
  ['Stack 1', 'Suit A', 5, 0],
  ['Stack 3', 'Suit B', 5, 0]]

fixed_game_17 = \
 [['Stack 4', 'Suit A', 6, 0],
  ['Stack 6', 'Suit C', 1, 1],
  ['Stack 5', 'Suit C', 4, 0],
  ['Stack 1', 'Suit D', 10, 0],
  ['Stack 3', 'Suit B', 9, 0],
  ['Stack 2', 'Suit D', 2, 2]]
 
# The "full_game" dataset describes a random game
# containing the maximum number of cards
stacks = ['Stack ' + str(stack_num+1) for stack_num in range(num_stacks)]
shuffle(stacks)
suits = ['Suit ' + chr(ord('A')+suit_num) for suit_num in range(4)]
shuffle(suits)
full_game = [[stacks[stack], suits[stack % 4], max_cards, randint(0, max_cards)]
             for stack in range(num_stacks)]

#
#--------------------------------------------------------------------#



#-----Function for Assessing Your Solution---------------------------#
#
# The function in this section will be used to mark your solution.
# Do not change any of the code in this section.
#
# The following function creates a random data set specifying a game
# of Patience to be drawn.  Your program must work for any data set 
# returned by this function.  The results returned by calling this 
# function will be used as the argument to your deal_cards function 
# during marking. For convenience during code development and marking 
# this function also prints the game data to the shell window.
#
# Each of the data sets generated is a list specifying a set of
# card stacks to be drawn. Each specification consists of the
# following parts:
#
# a) Which stack is being described, from Stack 1 to num_stacks.
# b) The suit of cards in the stack, from 'A' to 'D'.
# c) The number of cards in the stack, from 0 to max_cards
# d) An "extra" value, from 0 to max_cards, whose purpose will be
#    revealed only in Part B of the assignment.  You should
#    ignore it while completing Part A.
#
# There will be up to num_stacks specifications, but sometimes fewer
# stacks will be described, so your code must work for any number
# of stack specifications.
#
def random_game(print_game = True):

    # Percent chance of the extra value being non-zero
    extra_probability = 20

    # Generate all the stack and suit names playable
    game_stacks = ['Stack ' + str(stack_num+1)
                   for stack_num in range(num_stacks)]
    game_suits = ['Suit ' + chr(ord('A')+suit_num)
                  for suit_num in range(4)]

    # Create a list of stack specifications
    game = []

    # Randomly order the stacks
    shuffle(game_stacks)

    # Create the individual stack specifications 
    for stack in game_stacks:
        # Choose the suit and number of cards
        suit = choice(game_suits)
        num_cards = randint(0, max_cards)
        # Choose the extra value
        if num_cards > 0 and randint(1, 100) <= extra_probability: 
            option = randint(1,num_cards)
        else:
            option = 0
        # Add the stack to the game, but if the number of cards
        # is zero we will usually choose to omit it entirely
        if num_cards != 0 or randint(1, 4) == 4:
            game.append([stack, suit, num_cards, option])
        
    # Optionally print the result to the shell window
    if print_game:
        print('\nCards to draw ' +
              '(stack, suit, no. cards, option):\n\n',
              str(game).replace('],', '],\n '))
    
    # Return the result to the student's deal_cards function
    return game

#
#--------------------------------------------------------------------#



#-----Student's Solution---------------------------------------------#
#
#  Complete the assignment by replacing the dummy function below with
#  your own "deal_cards" function.
#

# Draw the card stacks as per the provided game specification
# Drop down 50pixels

#--------------------------------------------------------------------#



#-----Function for relating each card to its position -------------#
 
#Creating an function that relates to each card
def draw_card(cardNumber,x,y,):
    if cardNumber == "Suit A":
        return draw_card_1(x,y) 
    elif cardNumber == "Suit B":        
        return draw_card_2(x,y)    
    elif cardNumber == "Suit C":
        return draw_card_3(x, y) 
    elif cardNumber == "Suit D":
        return draw_card_4(x, y)
    
def draw_card2(Joker,x,y,):
    if Joker == "Suit A":
        return Joker_card(x,y)
    elif Joker == "Suit B":
        return Joker_card(x,y) 
    elif Joker == "Suit C":
        return Joker_card(x,y) 
    elif Joker == "Suit D":
        return Joker_card(x,y)
    
    

#Joker_card(x,y)
#insert parameter
#pass through the joker parameter through joker set
#then use that to check if the card is a joker first
#else check the suit and draw the card suit

                                               

#--------------------------------------------------------------------#



#-----Useful functions within the game-------------#
        
# Useful function below
#making it clear for user by making an function to draw an sqaure for reader
def square_card():
    begin_fill()
    forward(80)
    right(90)
    forward(200)
    right(90)
    forward(160)
    right(90)
    forward(200)
    right(90)
    forward(80)
    end_fill()
    pass

#repositions where the card number will go  
def num_in_cards(cardNumber):    
    penup()      
    write(cardNumber, font = ("Arial", 15, "normal"))
    setheading(0)
    pass

#repositions where the card number will go  
def num_in_cards_2(cardNumber):    
    penup()      
    write_upside_down(cardNumber, font = ("Arial", 15, "normal"))
    setheading(0)
    pass

#repositions where the card number will go  
def num_in_cards3(Joker):    
    penup()      
    write(Joker, font = ("Arial", 15, "normal"))
    setheading(0)
    pass

#repositions where the card number will go  
def num_in_cards4(Joker):
    pencolor('white')
    penup()      
    write_upside_down(Joker, font = ("Arial", 15, "normal"))
    setheading(0)
    pass



        

#--------------------------------------------------------------------#



#-----Functions for Creating the first card----------------------#
        
#Creating first card    
def draw_card_1(x,y):
    penup()
    pensize(3)
    x_position = x #x variable
    y_position = y #y variable
    goto(x_position, y_position)
    pendown()
    color('gold')
    fillcolor('olive')
    #Draws square 
    square_card()   
    rock_nation(x_position, y_position - 60)    
    pass

#--------------------------------------------------------------------#



#-----Functions for drawing rock nation onto card 1--------------------#

#Rock coin functions
#Square inside of the rock_nation coin
def square_me():
    penup()
    backward(25)
    left(90)
    backward(25)
    right(90)
    pendown()
    for square in range(4):        
        pensize(3)
        pencolor('gold')
        begin_fill()
        fillcolor('gold')
        forward(50)
        left(90)
        end_fill()
        pass

#Repositioning the cursor back to the middle    
def repos_rock():    
    penup()     
    forward(35)
    left(90)
    forward(55)
    setheading(0)
    #knowing where the number of the card will end up
    left(-90)
    backward(50)
    left(90)
    backward(65)
    pass
    
def rock_writing():
    #Constants
    diameter = 130
    radius = diameter // 1.2
    #Dot base of standard
    penup()
    left(-90)
    forward(35)
    left(-90)
    forward(35)           
    color('Dark green')
    write(str('Rock Nation'), font = ("Arial", 10, "normal"))
    setheading(0)
    #Back to the middle
    repos_rock()    
    pass


#RockNation coin
#Do not use goto
def rock_nation(x,y):
    #Constants
    diameter = 130
    radius = diameter // 1.2
    #Dot base of standard
    penup()
    goto(x,y - 30) 
    pendown()
    pencolor('Dark green')
    dot(diameter)
    pencolor('light green')
    dot(radius)
    forward(0)    
    #mini square
    square_me()
    pencolor('gold')
    #Spral
    spiral(2)
    setheading(0)
    #writing
    rock_writing()
    setheading(0)    
    pass

#--------------------------------------------------------------------#



#-----Functions for Creating the second card----------------------#



#Creating second card
def draw_card_2(x,y):
    penup()
    pensize(3)
    x_position = x #x variable
    y_position = y #y variable
    goto(x_position, y_position)
    pendown()
    color('white')
    fillcolor('aqua')
    square_card()
    air_nation(x_position, y_position - 60)
    pass

#--------------------------------------------------------------------#



#-----Functions for drawing air nation onto card 2--------------------#

#This is an constant that will be frequently used in the 
#First function of a spiral
def spiral(noCurve):
    for spiral in range(40):
        pendown()
        pensize(2)        
        forward(3)
        left(spiral)
        penup()
        pass
#Repositioning the curor back to the middle
def repos_air():    
    penup()    
    forward(45)
    left(90)
    forward(-5)
    setheading(0)
    #knowing where the number of the card will end up
    left(-90)
    backward(50)
    left(90)
    backward(65)
    pass

#Writing Air Nation and positioning the pen at where it should write/draw it 
#Do not use goto as they will complicate the turtle
def air_writing():
    penup()
    left(-90)
    forward(20)
    left(-90)
    forward(20)
    right(-90)
    backward(-10)
    pendown()
    color('Dark blue')
    write(str('Air Nation'), font = ("Arial", 10, "normal"))
    setheading(0)
    #Back to the middle
    repos_air()
    pass
    
#AirNation Coin
def air_nation(x,y):
    #Constants
    diameter = 130
    radius = diameter // 1.2
    #Dot base of standard
    penup()
    goto(x,y - 30)
    pendown()
    pencolor('Dark blue')
    dot(diameter)
    pencolor('light blue')
    dot(radius)
    pencolor('Dark blue')
    spiral(2)
    penup()
    #Going back to the start of the first circle to set up the second spiral 
    setheading(0)
    forward(-26)
    left(90)
    forward(-18)
    setheading(270)
    spiral(2)  
    #Going back to the start of the second circle to set up the third spiral
    setheading(0)
    forward(-16)
    left(-90)
    forward(-28)
    setheading(0)
    setheading(180)
    spiral(2)
    #Then it writes air nation to the function = air-writing  
    air_writing()
    setheading(0)
    pass


#--------------------------------------------------------------------#



#-----Functions for Creating the third card----------------------#

#3rd card
def draw_card_3(x,y):
    penup()
    pensize(3)
    x_position = x #x variable
    y_position = y #y variable
    goto(x_position, y_position)
    pendown()
    color('red')
    fillcolor('black')
    square_card()
    fire_nation(x_position, y_position - 60)
    pass

#--------------------------------------------------------------------#



#-----Functions for drawing fire nation onto card 3--------------------#

#going back to the middle therefore the numbers can be viewed /
#inside of the card instead of the outside or too far at the top
def repos_fire():
    penup()     
    forward(20)
    left(90)
    forward(5)
    setheading(0)
    #knowing where the number of the card will end up
    left(-90)
    backward(50)
    left(90)
    backward(65)
    pass

#Writing Fire Nation and positioning the pen at where it should write/draw it 
#Do not use goto as they will complicate the turtle
def fire_writing():
    #Constants
    diameter = 130
    radius = diameter // 1.2
    #repositioning the third circle in the centre of the design
    penup()
    pendown()
    left(-70)
    forward(18)
    left(-90)
    forward(48)
    setheading(0)
    
    #The 3rd inside circle
    pencolor('orange')
    dot(radius // 2)
    #position the writing text
    pendown()
    backward(25)
    #Writing fire nation
    color('Red')
    write(str('Fire Nation'), font = ("Arial", 10, "normal"))
    #Back to the middle     
    repos_fire()
    pass

#Fire Nation coin
def fire_nation(x,y):
    #Constants
    diameter = 130
    radius = diameter // 1.2
    #Dot base of standard
    penup()
    goto(x,y - 30)
    pencolor('Dark red')
    dot(diameter)
    pencolor('red')
    dot(radius)
    #repositioning the pen
    penup()
    left(90)
    forward(35)
    left(90)
    forward(-39)
    setheading(0)
    pendown()
    for fire in range(20):
        speed(False)
        pencolor('dark red')
        left(260)
        forward(80)   
    fire_writing()
    setheading(0)
    pass

#--------------------------------------------------------------------#



#-----Functions for Creating the fourth card----------------------#


#4th card
def draw_card_4(x,y):
    penup()
    pensize(3)
    x_position = x #x variable
    y_position = y #y variable
    goto(x_position, y_position)
    pendown()
    color('white')
    fillcolor('aqua')
    square_card()    
    water_nation(x_position, y_position - 60)
    pass

#--------------------------------------------------------------------#



#-----Functions for drawing Water nation onto card 4--------------------#

#Repositioning the cursor to the middle of the design therefore /
#The numbers can be drawn using the 
def repos_water():
    penup()     
    backward(35)
    left(-90)
    forward(20)
    setheading(0)
    #knowing where the number of the card will end up
    left(-90)
    backward(50)
    left(90)
    backward(65)
    pass

#creating mini spirals 
def mini_spirals():
    #but first position where i want the spirals to be
    penup()
    pensize(2)
    pencolor('Dark blue')    
    left(90)
    forward(20)
    right(90)
    forward(30)
    left(115)
    forward(5)
    spiral(2)
    #setheading(0)   
    #Next spiral in the centre
    penup()
    for minis in range(3):
        left(90)
        forward(13)
        left(90)
        forward(50)
        left(115)
        forward(5)
        spiral(2)
    setheading(0)
    repos_water()              
    pass

def water_writing():
    penup()
    #positioning where the tracer will draw 'water nation' 
    setheading(0)
    forward(108 // 2)
    left(90)
    forward(10)
    right(90)
    backward(38)
    color('Dark blue')
    write(str('Water Nation'), font = ("Arial", 9, "normal"))
    setheading(0)
    mini_spirals()
    pass
    
def water_nation(x,y):
    #Constants
    diameter = 130
    radius = diameter // 1.2
    #Dot base of standard
    penup()
    goto(x,y - 30)
    pencolor('Dark blue')
    dot(diameter)
    pencolor('white')
    dot(radius)    
    setheading(0)
    water_waves()
    second_waves()
    water_writing()    
    setheading(0)
    pass

def water_waves():
    pensize(3)
    color('Dark blue')
    penup()    
    backward(53)
    pendown()
    begin_fill()
    fillcolor('Dark blue')
    for waves in range(1):
        left(37)
        forward(10)
        left(280)
        forward(7)
        for waves in range(3):            
            #2
            left(80)
            forward(10)
            left(280)
            forward(10)
            #3
            left(80)
            forward(10)
            left(280)
            forward(10)
    pencolor('Dark blue')
    setheading(0)
    backward(108)
    end_fill()
    pass

def second_waves():
    #positioning second set of waves
    penup()
    forward(108 // 2)
    left(-90)
    forward(25)
    setheading(0)
    #drawing second set of waves
    pensize(3)
    color('Dark blue')
    penup()    
    backward(47)
    pendown()
    begin_fill()
    fillcolor('Dark blue')
    for waves in range(1):
        left(37)
        forward(10)
        left(280)
        forward(7)
        for waves in range(3):            
            #2
            left(80)
            forward(10)
            left(280)
            forward(10)
            #3
            left(80)
            forward(10)
            left(280)
            forward(10)
    pencolor('Dark blue')
    setheading(0)
    backward(108)
    end_fill()
    pass

#--------------------------------------------------------------------#



#-----Functions for Joker card----------------------#


#Joker card
def Joker_card(x,y):
    penup()
    pensize(3)
    x_position = x #x variable
    y_position = y #y variable
    goto(x_position, y_position)
    pendown()
    color('black')
    fillcolor('violet')
    square_card()    
    Joker_nation(x_position, y_position - 60)
    pass

#--------------------------------------------------------------------#



#-----Functions for drawing Joker card--------------------#

def square_Joker():
    penup()
    backward(25)
    left(90)
    backward(25)
    right(90)
    pendown()
    for square in range(4):        
        pensize(3)
        pencolor('gold')
        begin_fill()
        fillcolor('gold')
        forward(50)
        left(90)
        end_fill()
        pass

#Repositioning the cursor back to the middle    
def repos_Joker():    
    penup()     
    forward(35)
    left(90)
    forward(55)
    setheading(0)
    #knowing where the number of the card will end up
    left(-90)
    backward(50)
    left(90)
    backward(65)
    pass
    
def Joker_writing():
    #Constants
    diameter = 130
    radius = diameter // 1.2
    #Dot base of standard
    penup()
    left(-90)
    forward(35)
    left(-90)
    forward(35)           
    color('Aqua')
    write(str('Joker Nation'), font = ("Arial", 10, "normal"))
    setheading(0)
    #Back to the middle
    repos_Joker()    
    pass


#Joker coin
#Do not use goto
def Joker_nation(x,y):
    #Constants
    diameter = 130
    radius = diameter // 1.2
    #Dot base of standard
    penup()
    goto(x,y - 30) 
    pendown()
    pencolor('red')
    dot(diameter)
    pencolor('blue')
    dot(radius)
    forward(0)    
    #mini Joker square
    square_Joker()
    pencolor('gold')
    #Spral
    spiral(2)
    setheading(0)
    #writing
    Joker_writing()    
    setheading(0)    
    pass




#--------------------------------------------------------------------#



#-----Functions for deal card function----------------------#


def deal_cards(fixed_game_16):
    
    y_position = 275
    x_position = -449
    
#reads inside of the arrays for each row #checks the value of the array    
    for x in fixed_game_16: 
        if x[0] == 'Stack 6':
            x_pos = 446
        if x[0] == 'Stack 5':
            x_pos = 267
        elif x[0] == 'Stack 4':
            x_pos = 88            
        elif x[0] == 'Stack 3':
            x_pos = -91
        elif x[0] == 'Stack 2':
            x_pos = -270
        elif x[0] == 'Stack 1':
            x_pos = -449

#(x[2] tells me how many crads are being drawn in the 2 index i.e. 6th etc
        for cards in range(x[2]):
                       
#(x[1] reads the suites                
            draw_card(x[1], x_pos , y_position - 50 * cards)
            num_in_cards(cards)
            #second writing
            setheading(0)            
            penup()
            left(-90)            
            forward(150)
            left(90)
            forward(125)
            color('red')
            num_in_cards_2(cards)            
            home()

#joker
        #(x[2] tells me how many crads are being drawn in the 2 index i.e. 6th etc
        for part2 in range(x[3]):
                       
#(x[1] reads the suites                
            draw_card2(x[1], x_pos , y_position - 50 * cards)
            num_in_cards3(part2)
            #second writing for the joker card
            setheading(0)
            left(-90)            
            forward(150)
            left(90)
            forward(125)
            pencolor('red')
            num_in_cards4(part2)            
            home()
            
        


            


                
#--------------------------------------------------------------------#



#-----Main Program---------------------------------------------------#
#
# This main program sets up the background, ready for you to start
# drawing the card game.  Do not change any of this code except
# as indicated by the comments marked '*****'.
#

# Set up the drawing canvas
# ***** Change the default argument to False if you don't want to
# ***** display the coordinates and stack locations
create_drawing_canvas()

# Control the drawing speed
# ***** Modify the following argument if you want to adjust
# ***** the drawing speed
speed(False)


# Decide whether or not to show the drawing being done step-by-step
# ***** Set the following argument to False if you don't want to wait
# ***** while the cursor moves around the screen
tracer(False)

# Give the drawing canvas a title
# ***** Replace this title with a description of your cards' theme
title("The Four Nations Once lived in Harmony!")
 
### Call the student's function to draw the game
### ***** While developing your program you can call the deal_cards
### ***** function with one of the "fixed" data sets, but your
### ***** final solution must work with "random_game()" as the
### ***** argument to the deal_cards function.  Your program must
### ***** work for any data set that can be returned by the
### ***** random_game function.
#deal_cards(fixed_game_16) # <-- used for code development only, not marking
#deal_cards(full_game) # <-- used for code development only, not marking
deal_cards(random_game()) # <-- used for assessment

# Exit gracefully
# ***** Change the default argument to False if you want the
# ***** cursor (turtle) to remain visible at the end of the
# ***** program as a debugging aid
release_drawing_canvas()


#
#--------------------------------------------------------------------#

