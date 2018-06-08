# the lines below imports all the dependancies that required in this module
from matplotlib import pyplot as plt
import csv


# the methods below is for reading infromation from the csv file
all_airports= 'All Australian Airports'
all_value =[]

def read_data():
    '''
    Method that finds all records related to the first column
    '''
    found_rows =[]
    with open('airline-passenger-movements.csv','r') as csvfile:
        plots = csv.reader(csvfile)
        for row in plots:
            found_rows.append(row)
    return found_rows
    # print(found_rows)

def yearly_data():
    '''
    Method that process total number of passagers based on the years from the pax_total column
    '''
    found_rows = read_data()
    list_of_years = [1985,1986,1987,1988,1989,1990,1991,1992,1993,1994,1995,1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018]
    yearly_totals = []
    top_years =[]
    bottom_years = []
    for year in list_of_years:
        yearly_total = 0
        for row in found_rows:
            if str(year) == row[1]:
                yearly_total += int(row[11])
        yearly_totals.append(yearly_total)

    top_five = sorted(yearly_totals, key=int, reverse=True)[:5]
    bottom_five = sorted(yearly_totals, key=int)[:5]
    for item in top_five:
        top_years.append(list_of_years[yearly_totals.index(item)])
    
    for item in bottom_five:
        bottom_years.append(list_of_years[yearly_totals.index(item)])
    # print(bottom_five)

    return {'top':{'x':top_years,'y':top_five},'bottom':{'x':bottom_years,'y':bottom_five}}


def draw_bar():
    packed_list = yearly_data()
    x= packed_list['top']['x']
    y = packed_list['top']['y']

    x1= packed_list['bottom']['x']
    y2 = packed_list['bottom']['y']
    # table = packed_list['table']
   
    # the code below produces a barchart
    plt.bar(x,y, label ="Top 5 years")
    # plt.plot(x1,y2)
    plt.xlabel('Years')
    plt.ylabel('All Airports Passangers')
    plt.title('Number of Passangers over the years')
    
    plt.bar(x1,y2, label= "Bottom Five Years")
    plt.xlabel('Years')
    plt.ylabel('All Airports Passangers')
    plt.title('Number of Passangers over the years')
    plt.legend()
    # plt.show()
    my_image1 = 'images/bottom_years.png'
    plt.savefig(my_image1)


