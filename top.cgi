#!/usr/bin/env python3
from matplotlib import pyplot as plt
from top import draw_bar
import cgi   # NEW

# generating bat and line graph chart images
draw_bar()

def main(): # NEW except for the call to processInput
    top_years = 'images/bottom_years.png'
    contents = processInput(top_years)
    print(contents)
    
def processInput(image_file):  
    '''Process input parameters and return the final page as a string.'''
    return fileToStr('top.html').format(**locals())
        

# standard code for future cgi scripts from here on
def fileToStr(fileName): 
    """Return a string containing the contents of the named file."""
    fin = open(fileName); 
    contents = fin.read();  
    fin.close() 
    return contents

try:   # NEW
    print("Content-type: text/html\n\n")   # say generating html
    main()
except:
    cgi.print_exception()                 # catch and print errors