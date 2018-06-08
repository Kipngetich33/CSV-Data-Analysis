#!/usr/bin/env python3
from matplotlib import pyplot as plt
from airports import draw_bar

import cgi   # NEW

draw_bar()

def main(): # NEW except for the call to processInput
    image_file = 'images/top_airports.png'
    contents = processInput(image_file)
    print(contents)

    
def processInput(image_file):  
    '''Process input parameters and return the aiports page as a string.'''
    return fileToStr('airports.html').format(**locals())
    # return fileToStr('airports.html')

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