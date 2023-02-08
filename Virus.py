from turtle import *

color('green') #color of the virus
bgcolor('black') #background color
speed(11) #speed of the line of each spiral

hideturtle() #hiding the arrow head

count = 0 #initializng the count that will be used for each turn

while count < 1000: #can be changed but not lower than 200 since it will execute only half
    right(count) #making the lines move the right direction
    forward(count * 1) #how big or small the spiral should be
    count = count + 1 #simple incremention till the while is met

    # right() and forward() are important equally to make it go circular
    # left() and backward() can be used too