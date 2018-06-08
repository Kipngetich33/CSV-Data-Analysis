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

def seasons():
    '''
    Functions that group all values as pers seasons from the csv
    '''
    spring =0
    summer = 0
    autumn =0
    winter = 0
    data_array = read_data()
    for row in data_array:
        if row[2] == '9' or row[2]== '10' or row[2] == '11':
            spring +=int(row[11])
        elif row[2] == '12' or row[2]== '1' or row[2] == '2':
            summer +=int(row[11])
        elif row[2] == '3' or row[2]== '4' or row[2] == '5':
            autumn +=int(row[11])
        elif row[2] == '6' or row[2]== '7' or row[2] == '8':
            winter +=int(row[11])
    return({'spring':spring,'summer':summer,'autumn':autumn,'winter':winter}) 


def draw_chart():
    season_values = seasons()

    slices =  [season_values['spring'],season_values['summer'],season_values['autumn'],season_values['winter']]
    activities = ['Spring','Summer','Autumn','Winter']

    plt.pie(slices,labels=activities,)

    plt.title('Title')
    plt.legend()
    # plt.show()
    my_image1 = 'images/seasons_pie.png'
    plt.savefig(my_image1)

    # crete table with passanger contents below
    string_table1 = '<tr><td><h5 id="table_data">'+activities[0]+'<h5></td>'+'<td><h5 id="table_data">'+str(slices[0])+'<h5></td></tr>'
    string_table2 = '<tr><td><h5 id="table_data">'+activities[1]+'<h5></td>'+'<td><h5 id="table_data">'+str(slices[1])+'<h5></td></tr>'
    string_table3 = '<tr><td><h5 id="table_data">'+activities[2]+'<h5></td>'+'<td><h5 id="table_data">'+str(slices[2])+'<h5></td></tr>'
    string_table4 = '<tr><td><h5 id="table_data">'+activities[3]+'<h5></td>'+'<td><h5 id="table_data">'+str(slices[3])+'<h5></td></tr>'
    
    # the code below creates the table for the data
    return string_table1 + string_table2 + string_table3 + string_table4
    

# draw_chart()