##############################################################################
#  Computer Project #7
#
#  Algorithm
#    prompt for a file name
#    open file
#    read file
#       prompt for a year
#       if year is vaild, display table of medications within year
#           prompt for a whether or not a table is wanted 
#               if table wanted, display table of top ten medications in year
#               else, continues program
#       if year is invaild reprompts
#       if year is 'q', terminates program
##############################################################################

from operator import itemgetter
import pylab

YEAR_LIST = [2011, 2012, 2013, 2014, 2015]
def open_file():
    ''' Loops until vaild file is entered. Once vaild file is entered
    opens file and returns. '''
    while True:
        fp = input("Input a file name: ")
        try: 
            open_file = open(fp, 'r')
            print("Medicaid drug spending 2011 - 2015")
            return open_file
        except FileNotFoundError:
            print("Unable to open the file. Please try again.")

def read_data(fp):
    '''Ignores first line of file and reads the rest. Creates
    a tuple for each medicine with year, brand, total spending,
    prescription fill count, unit count, average cost per prescription,
    and average cost per unit. Appends each tuple to a list and returns
    list.'''
    fp.readline()
    med_tup_list = []
    
    for line in fp:
        l_list = line.split(',')
        # Ignores medicines with missing information and doesn't make tuple
        try: 
            year = int(l_list[0])
        except ValueError:
            continue
        try:
            total = float(l_list[3])
        except ValueError:
            continue
        try: 
            prescr = int(l_list[4])
        except ValueError:
            continue
        try:
            units = int(l_list[5])
        except ValueError:
            continue
        avg_prescr = total/prescr
        avg_unit = total/units
        med_tup = (year, l_list[1], total, prescr, units, avg_prescr, avg_unit)
        med_tup_list.append(med_tup)
        
    med_tup_list.sort()
    return med_tup_list
        

def top_ten_list(column, year_list):
    ''' Finds the top ten medications based on the the column provided. 
    Creates two lists, one for brand name and another for values, for the top 
    ten. Creates a tuple containing the two lists and returns that tuple. '''
    top_ten_brands_list = []
    top_ten_values_list = []
    col_list = sorted(year_list, key=itemgetter(column-1), reverse=True)
    
    # Appends brands to top_ten_brands_list and values to top_ten_values_list
    for i in range(10):
        top_ten_brands_list.append(col_list[i][1])
        top_ten_values_list.append(col_list[i][column-1])
    
    top_ten_tup = (top_ten_brands_list, top_ten_values_list)
    return top_ten_tup
        
    
def get_year_list(year, data):
    ''' Intakes a year and list of tuples. Creates a new list and appends
    only those who contain the year specified. Sorts new list and returns.'''
    year_med_list = []
    
    for tup in data:
        if tup[0] == year:
            year_med_list.append(tup)
            
    year_med_list.sort()
    return year_med_list

def display_table(year, year_list):
    ''' Intakes a year and year_list. Prints a table including brand name, 
    prescriptions, prescription cost, and total for given year_list.'''
    title = "Drug spending by Medicaid in {}".format(year)
    print("{:^80}".format(title))
    print("{:<35}{:>15}{:>20}{:>15}".format("Medication", "Prescriptions", \
          "Prescription Cost", "Total"))
   
    for tup in year_list:
        brand = tup[1]
        prescr = tup[3]
        prescr_cost = tup[5]
        total = tup[2]/1000
        print("{:<35}{:>15,}{:>20,.2f}{:>15,.2f}".format(brand,\
              prescr, prescr_cost, total))
        

def plot_top_ten(x, y, title, xlabel, ylabel):
    '''
        This function plots the top 10 values from a list of medications.
        This function is provided to the students.
        
        Input:
            x (list) -> labels for the x-axis
            y (list) -> values for the y-axis
            title (string) -> Plot title
            xlabel (string) -> Label title for the x-axis
            ylabel (string) -> Label title for the y-axis
    '''
    
    pos = range(10)
    pylab.bar(pos, y)
    pylab.title(title)
    pylab.xlabel(xlabel)
    pylab.ylabel(ylabel)
    pylab.xticks(pos,x, rotation='90')
    pylab.show()
    

def main():
    ''' Prompts for a file and opens/reads file. Prompts for a year. If 'q' 
    is entered for year, program terminates. If the year is vaild, displays a 
    table of medications for the given year. Prompts for whether or not a graph 
    is wanted of the top ten medications within given year. If "yes" graph is 
    displayed. If "no" program continues. '''
    fp = open_file()
    data = read_data(fp)
    
    #Loops until a vaild year is entered. If invaild year entered,
    #prints a error statement. If 'q' is enetered, terminates program.
    while True:
        year = input("Enter a year to process ('q' to terminate): ")  
        try:
            year = int(year)
        except ValueError:
            if year == 'q':
                break
            else:
                print("Invalid Year. Try Again!")
                continue
        if year in YEAR_LIST:
            list_year = get_year_list(year,data)
            display_table(year, list_year)
            top_ten = top_ten_list(3, list_year) 
            graph = input("Do you want to plot the top 10 values (yes/no)? ")
            if graph == "yes":
                x = top_ten[0]
                y = top_ten[1]
                title = "Top 10 Medications prescribed in {}".format(year)
                x_axis = "Medication Name"
                y_axis = "Prescriptions"
                plot_top_ten(x, y, title, x_axis, y_axis)
        else:
            print("Invalid Year. Try Again!")
        
if __name__ == "__main__":
    main()