# the lines below imports all the dependancies that required in this module
from matplotlib import pyplot as plt
import csv


# the methods below is for reading infromation from the csv file
all_airports= 'All Australian Airports'
all_value =[]

def read_data(first_col):
    '''
    Method that finds all records related to the first column
    '''
    found_rows =[]
    with open('airline-passenger-movements.csv','r') as csvfile:
        plots = csv.reader(csvfile)
        for row in plots:
            if row[0]==first_col:
                found_rows.append(row)
    return found_rows
    # print(found_rows)

def find_sum(found_rows):
    '''
    Method that finds the sum of values for each of the totals
    '''
    years_dictionary = {}
    list_of_years = [1985,1986,1987,1988,1989,1990,1991,1992,1993,1994,1995,1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018]
    year_totals = []
    for item in list_of_years:
        temporary_list = []
        for item2 in found_rows:
            if str(item) == item2[1]:
                temporary_list.append(item2)
        years_dictionary[str(item)]=temporary_list

    for k in years_dictionary:
        total_passagers = []
        int_total = 0
        yearly_list = years_dictionary[k]
        for item in yearly_list:
            total_passagers.append(item[11])
        for item in total_passagers:
            int_total += int(item)
        year_totals.append(int_total)

    table_string =''
    for year in list_of_years:
        table_string+= '<tr>'
        table_string+='<td>'+str(year)+'</td>'
        table_string+='<td>&nbsp;&nbsp;&nbsp;&nbsp;'+str(year_totals[list_of_years.index(year)])+'</td>'
        table_string+='</tr>'
    
    all_value.append({'x':list_of_years,'y':year_totals,'table':table_string} )
    return {'x':list_of_years,'y':year_totals,'table':table_string} 

    

def unpack(list_data):
    '''
    Method that gets all the data recieved and unpacks them to be used in a graph
    '''
    x = []
    y = []
    for item in list_data:
        x.append(item[1]) # appends the year of the item
        y.append(item[11]) # appends the pax_total of the record
    return {'x':x,'y':y}


def table():
    '''
    Method that puts values in a table
    '''
    table_string = all_value[0]['table']
    return table_string
    



# the code below is for creating the charts

def draw_chart(packed_list):
    '''
    Function that uses matplot lib to generate images of the
    generated plot and saves them to the images folder
    '''
    x= packed_list['x']
    y = packed_list['y']
    table = packed_list['table']

    # the code below produces a line graph

    plt.plot(x,y)
    # plt.plot(x2,y2, label = 'Second Line')
    plt.xlabel('Years')
    plt.ylabel('All Airports Passangers')
    # plt.legend()
    plt.title('Number of Passangers over the years')
    # plt.show()
    my_image = 'images/yearly.png'
    plt.savefig(my_image)

def draw_bar(packed_list):
    x= packed_list['x']
    y = packed_list['y']
    table = packed_list['table']
   
    # the code below produces a barchart
    plt.bar(x,y)
    plt.plot(x,y)
    plt.xlabel('Years')
    plt.ylabel('All Airports Passangers')
    plt.title('Number of Passangers over the years')
    # plt.show()
    my_image1 = 'images/yearly_bar.png'
    plt.savefig(my_image1)

# this is the main functions that calls all the other function
def main_1():
    print('ok')
    data_1 = read_data('All Australian Airports')
    draw_bar((find_sum(data_1)))


main_1()

# def main_2():
#     # function that generates the yearly bar graph
#     bar_data = read_data('All Australian Airports')
#     draw_bar((find_sum(bar_data)))

# main_2()






