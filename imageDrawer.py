'''
Programmer: Jess Elliott

Description: This program draws pictures according to sequences of (x, y)
             coordinates read from an input file. 

Input: User input is the filename, a x_shift, a y_shift and a scaling factor.

Output: The program outputs the picture which is produced by drawing lines
        between pairs of consecutive (x, y) coordinates.
'''

#Importing the relevant libraries
from simplegraphics import *
import math

#This function draws a dotted line between two given coordinates
#Parameters: x1, y1, x2, y2 as integers 
#Returns: -
def draw_dotted_line(x1, y1, x2, y2):
    #Calculating the distance between two points
    distance = math.sqrt(((x2 - x1)**2) + ((y2 - y1))**2)

    #Calculating the number of gaps in the line 
    num_gaps = int(distance / 10)      

    #Calculating the distance between each dot in the x- and y-direction 
    total_change_x = x2 - x1   
    total_change_y = y2 - y1   
    x_step = total_change_x / num_gaps    
    y_step = total_change_y / num_gaps    

    #Setting the thickness and color of the line 
    set_line_thickness(2)
    set_color("black")

    #Drawing the line 
    draw_filled_circle(x1, y1, 2)
    x_val = x1    
    y_val = y1    
    for dots in range(num_gaps):
        x_val += x_step
        y_val += y_step
        draw_filled_circle(x_val, y_val, 2) 

#This function is the program for challenge 4 in the brief. It writes a
#program that allows the user to create their own drawing and saves it to
#a file
#Parameters: -
#Returns: -
def writing_file():   
    #Opening statement for the new program 
    print("Create the drawing of your dreams, and once you're done click within the block \nin the top left corner to save it to the file and again to close the canvas")

    #Creating the new file 
    new_file = open("drawing.txt", "w")

    open_canvas(500, 500)
    
    #Drawing a little block for the user to quit the program
    draw_line(10, 0, 10, 10)
    draw_line(0, 10, 10, 10)

    #Gathering user inputs 
    wait_for_click()
    x1 = get_last_click_x()
    y1 = get_last_click_y()

    draw_filled_circle(x1, y1, 2)
    new_file.write(str(x1) + " " + str(y1) + "\n")

    while x1 > 0:
        wait_for_click()
        x1 = get_last_click_x()
        y1 = get_last_click_y()
        
        #Allocating a little block to stop the loop once the user is
        #finished  
        if x1 <= 10 and y1 <= 10:
            break

        #Drawing the dot and writing it to the file
        draw_filled_circle(x1, y1, 2)
        new_file.write(str(x1) + " " + str(y1) + "\n")

    close_canvas_after_click()
    
def main():
    #Gathering user inputs 
    file_name = input("Enter the filename you wish to read (include .txt): ")
    print()
    x_shift = int(input("Enter the value of the x-shift you'd like (A negative integer to move left, \na positive integer to move right, or '0' for the original): "))
    print()
    y_shift = int(input("""Enter the value of the y-shift you'd like (A negative integer to move up, \na positive integer to move down, or '0' for the original): """))
    print()
    scaling_f = float(input("Enter the scaling factor of the drawing you'd like (e.g. Enter 2 for twice the \nsize, 1 for the original size or 0.5 for half the size): "))

    #Opening the file 
    file = open(file_name, "r")

    #Working with the first line of the file     
    prev_line = file.readline()
    prev_line = prev_line.rstrip()
    prev_command, prev_x1, prev_y1 = prev_line.split(" ")

    #Converting the string of x1 and y1 into an integer 
    prev_x1 = int(prev_x1)
    prev_y1 = int(prev_y1)

    #Opening the canvas
    if prev_command == "canvas":
        open_canvas(prev_x1, prev_y1)

    #Reading the lines in the file     
    for curr_line in file:
        curr_line = curr_line.rstrip()  
        curr_command, curr_x1, curr_y1 = curr_line.split(" ")
        curr_x1 = int(curr_x1)
        curr_y1 = int(curr_y1)
        
        #Working with the 'lineto' command 
        if curr_command == "lineto":
            set_line_thickness(2)
            set_color("black")
            draw_line((scaling_f * (prev_x1 + x_shift)), (scaling_f * (prev_y1 + y_shift)), (scaling_f * (curr_x1 + x_shift)), (scaling_f * (curr_y1 + y_shift)))     

        #Working with the 'dlineto' command 
        if curr_command == "dlineto":
            draw_dotted_line((scaling_f * (prev_x1 + x_shift)), (scaling_f * (prev_y1 + y_shift)), (scaling_f * (curr_x1 + x_shift)), (scaling_f * (curr_y1 + y_shift)))

        #Sliding window        
        prev_command = curr_command
        prev_x1 = curr_x1
        prev_y1 = curr_y1  

    print()
    print("Click the canvas to close it and end the program")
    
    close_canvas_after_click()

    file.close()

main()
print()
writing_file()

