#!/usr/bin/env python3
from matplotlib import pyplot as plt
#!/usr/bin/env python3
from seasons import draw_chart
import cgi   # NEW

# generating bat and line graph chart images
table_string =draw_chart()

def main(): # NEW except for the call to processInput
    seasons_image = 'images/seasons_pie.png'
    contents = processInput(seasons_image,table_string)
    print(contents)
    
def processInput(image_file,table_string):  
    '''Process input parameters and return the final page as a string.'''
    return fileToStr('seasons.html').format(**locals())
        

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
    cgi.print_exception()