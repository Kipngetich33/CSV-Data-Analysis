#!/usr/bin/env python3
from matplotlib import pyplot as plt
from yearly import main_1,table
import cgi   # NEW

# generating bat and line graph chart images
main_1()
data_table = table()

def main(data_table): # NEW except for the call to processInput
    yearly_trend = 'images/yearly.png'
    yearly_bar = 'images/yearly_bar.png'
    contents = processInput(yearly_trend,yearly_bar,data_table)
    print(contents)
    
def processInput(image_file,image_file2,table):  
    '''Process input parameters and return the final page as a string.'''
    return fileToStr('yearly.html').format(**locals())
        

# standard code for future cgi scripts from here on
def fileToStr(fileName): 
    """Return a string containing the contents of the named file."""
    fin = open(fileName); 
    contents = fin.read();  
    fin.close() 
    return contents

try:   # NEW
    print("Content-type: text/html\n\n")   # say generating html
    main(data_table) 
except:
    cgi.print_exception()                 # catch and print errors