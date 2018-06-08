# the lines below imports all the dependancies that required in this module
from matplotlib import pyplot as plt
import csv


# the methods below is for reading infromation from the csv file

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


def find_unique():
    '''
    Method for findin all the unique airports provided
    '''
    all_values = read_data()
    all_rows =[]
    all_years =[]
    for row in all_values:
        all_rows.append(row[0])
    unique_ports =  set(all_rows)
    # print(unique_ports)
    return unique_ports

def find_sum():
    '''
    Method that finds the sum of values for each of the totals
    '''
    list_of_airports = []
    all_value = []
    airports_dictionary = {}
    unique_aiports = find_unique()
    found_rows = read_data()
    airport_totals = {}
    total_ints =[]
    for item in unique_aiports:
        temporary_list = []
        for item2 in found_rows:
            if item == item2[0]:
                temporary_list.append(item2)
        airports_dictionary[str(item)]=temporary_list
    
    for item in airports_dictionary:
        int_total = 0
        test_list =[]
        for item2 in airports_dictionary[item]:
            if item2[11]!='Pax_Total':
                int_total += int(item2[11])
        total_ints.append(int_total)
        airport_totals[item]= int_total

    table_string =''
    for aiport in airport_totals:
        list_of_airports.append(aiport)
        table_string+= '<tr>'
        table_string+='<td>'+aiport+'</td>'
        table_string+='<td>&nbsp;&nbsp;&nbsp;&nbsp;'+str(airport_totals[aiport])+'</td>'
        table_string+='</tr>'
    # all_value.append({'x':list_of_years,'y':year_totals,'table':table_string} )
    return {'x':list_of_airports,'y':total_ints,'table':table_string}

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


# def table():
#     '''
#     Method that puts values in a table
#     '''
#     table_string = all_value[0]['table']
#     return table_string
    



# the code below is for creating the charts

def draw_bar():
    packed_list = find_sum()
    x= packed_list['x']
    y = packed_list['y']
    table = packed_list['table']
    # print(x)
    top_airports =[]
    bottom_airports =[]
   
    top_five = sorted(y, key=int, reverse=True)[1:6]
    bottom_five = sorted(y, key=int)[:5]
    for item in top_five:
        top_airports.append(x[y.index(item)]) 
    
    for item in bottom_five:
        bottom_airports.append(x[y.index(item)])

    
    combined_x = top_airports+bottom_airports
    combined_y = top_five+bottom_five
    for item in combined_y:
        plt.bar(combined_x[combined_y.index(item)],item,label = combined_x[combined_y.index(item)])
    
    plt.xlabel('Airports')
    plt.ylabel('Number of Passangers')
    plt.legend()
    plt.title('Number of Passangers per Airport')
    # plt.show()
    my_image = 'images/top_airports.png'
    plt.savefig(my_image)
    





