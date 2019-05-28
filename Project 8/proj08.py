###########################################################
#  Computer Project #8
#
#  Algorithm
#    prompt for a file name
#    open file
#    read file
#       loop until 'quit' is entered
#           prompt for state name
#           prompt for year
#           display min and max values for pollution
#           display "pollution totals by year" table
#           display "pollution by city" table
#           display "top months" table
#           prompt for if graph is wanted
#               if 'yes', display graph      
###########################################################
import csv
import pylab

def open_file():
    ''' Loops until vaild file is entered. Once vaild file is entered
    opens file and returns. '''
    while True:
        fp = input("Input a file name: ")
        try: 
            open_file = open(fp, 'r')
            return open_file
        except FileNotFoundError:
            print("Unable to open file.")
            
def read_file(fp):
    ''' Creates/returns a dictionary from file given. Keys are the state and 
    values are the data. If AQI is missing from data, ignores line. Creates 
    lists from data. Adds list to dictionary value if city/date are not already 
    in dictionary value.'''
    pollution_dict = {}
    reader = csv.reader(fp)
    header = next(reader,None)
    previous_city, previous_date = "", ""
    
    for line_list in reader:
        s_list = line_list[5:]
        
        # Checks if AQI values are vaild
        NO2_AQI = s_list[8]
        if NO2_AQI == '':
            continue
        O3_AQI = s_list[13]
        if O3_AQI == '':
            continue
        SO2_AQI = s_list[18]
        if SO2_AQI == '':
            continue
        CO_AQI = s_list[23]
        if CO_AQI == '':
            continue
        
        # Creates list for dictionary value
        NO2mean = float(s_list[5])
        O3mean = float(s_list[10]) *1000
        SO2mean = float(s_list[15])
        COmean = float(s_list[20]) *1000
        r_list = [s_list[2],s_list[3],NO2mean,O3mean,SO2mean,COmean]
        
        # If key is already not created, makes key. Else, appends lists
        # with a different city and date from those already in key's value.
        if s_list[0] not in pollution_dict:
            pollution_dict[s_list[0]]=[r_list]
        elif previous_city != r_list[0] or previous_date != r_list[1]:
            pollution_dict[s_list[0]].append(r_list)
        elif previous_city != r_list[0] and previous_date != r_list[1]:
            pollution_dict[s_list[0]].append(r_list)

        previous_city = r_list[0]
        previous_date = r_list[1]
        
    return pollution_dict


def total_years(D, state):
    ''' Intakes a dictionary and state name and creates/returns a tuple 
    contianing each year's average total pollution for each pollutant and the
    max and min values of all average pollution values. '''
    year_means_lst = []
    year1 = int(D[state][1][1][-4:]) #inital year
    begin_empty_years = int(str(year1)[-2:]) #empty years at beginning of list
    
    # Adds years without data to beginning of list if necessary. Ensures
    # that years match correct index of year_means_lst
    for i in range(begin_empty_years):
        year_means_lst.append([0,0,0,0])
    
    # Creates lists and ensure yer_mean_lst has a total of 16 list with in it.
    # Each list represents one year with the first list representing 
    # the year 2000 and last representing 2015.
    for i in range(17-begin_empty_years):
        mean_lst = [0,0,0,0]
        
        # Adds each pollutant mean based on type and stores values in 
        # year_means_lst to get the average total pollution for given year.
        for lst in D[state]:
            year = int(lst[1][-4:])
            if year == year1:
                NO2mean = lst[2]
                O3mean = lst[3]
                SO2mean = lst[4]
                COmean = lst[5]
                mean_lst[0] = mean_lst[0] + NO2mean
                mean_lst[1] = mean_lst[1] + O3mean
                mean_lst[2] = mean_lst[2] + SO2mean
                mean_lst[3] = mean_lst[3] + COmean
        year_means_lst.append(mean_lst)
        year1+=1

    # Finds the min and max values out of all pollution values
    max_val = 0
    min_val = float("inf")
    for lst in year_means_lst:
        for val in lst:
            if val > max_val:
                max_val = val
            elif val < min_val:
                min_val = val
                
    final_means_tup = (year_means_lst, max_val, min_val)
    return final_means_tup
    
    
def cities(D, state, year):
    ''' Intakes a dictionary, state, and year. Creates/returns a new dictionary
    for given state where keys are cities and values are average pollutants
    for given year for that particular city.'''
    city_dict = {}
    for lst in D[state]:
        if int(lst[1][-4:]) == year: 
            
            # Creates key or alters key values if key already in dictionary
            if lst[0] not in city_dict:
                city_dict[lst[0]]= lst[2:]
            else:
                mean_lst = [lst[2],lst[3], lst[4], lst[5]]
                
                # Evaluates average pollutants for dictionary key's value
                for i in range(4):
                   pollutant_val = mean_lst[i]
                   city_dict[lst[0]][i] += pollutant_val
    return city_dict

def months(D,state,year):
    '''Intakes a dictionary, state, and year. Creates/returns a tuple containing
    four lists. Each list represents one pollutant and contains the top five 
    pollutant totals. The pollution totals are found by adding the pollution
    means of each month and comparing month totals.'''
    # Lists of pollutants, each item represents a month. Item at index 0 is
    # January, item at index 1 is Febuary, and so on.
    NO2_lst = [0,0,0,0,0,0,0,0,0,0,0,0]
    O3_lst = [0,0,0,0,0,0,0,0,0,0,0,0]
    SO2_lst = [0,0,0,0,0,0,0,0,0,0,0,0]
    CO_lst = [0,0,0,0,0,0,0,0,0,0,0,0]
    pollutant_lst = [NO2_lst, O3_lst, SO2_lst, CO_lst]
    top5_lst = []
    
    # Goes through dictionary and adds pollutant means within the same month
    for lst in D[state]:
        NO2mean = lst[2]
        O3mean = lst[3]
        SO2mean = lst[4]
        COmean = lst[5]
        pollution_dict_lst = [NO2mean, O3mean, SO2mean, COmean]
        if int(lst[1][-4:]) == year:
            month_index = lst[1].index("/")
            list_index = int(lst[1][:month_index])-1
            for i in range(4):
                pollutant_lst[i][list_index]+= pollution_dict_lst[i]
    
    # Sorts lists in decending order then slices to get top five
    for i in pollutant_lst:
        i.sort(reverse = True)
        top5_lst.append(i[:5])
        
    return tuple(top5_lst)

def display(totals_list,maxval,minval,D_cities,top_months):
    ''' Displays the data.'''
    # Max/Min table
    print("\nMax and Min pollution")
    print("\n{:>10s}{:>10s}".format("Minval", "Maxval"))
    print("{:>10.2f}{:>10.2f}".format(minval, maxval))
    
    # Pollution totals by year table
    print("\nPollution totals by year")
    print("\n{:<6s}{:>8s} {:>8s} {:>8s} {:>8s}".format("Year", "NO2", "O3", \
          "SO2", "CO"))
    for i in range(17):
        year = 2000 + i
        NO2 = totals_list[i][0]
        O3 = totals_list[i][1]
        SO2 = totals_list[i][2]
        CO = totals_list[i][3]
        if 0 not in totals_list[i]:
            print("{:<6}{:>8.2f} {:>8.2f} {:>8.2f} {:>8.2f}".format(year, NO2, \
                  O3, SO2, CO))
        
    # Pollution by city table
    print("\nPollution by city")
    print("\n{:<16s}{:>8s} {:>8s} {:>8s} {:>8s}".format("City", "NO2", "O3", \
          "SO2", "CO"))
    for key, val in D_cities.items():
        print("{:<16s}{:>8.2f} {:>8.2f} {:>8.2f} {:>8.2f}".format(key, val[0], \
              val[1], val[2], val[3]))
    
    # Top months table
    print("\nTop Months")
    print("\n{:>8s} {:>8s} {:>8s} {:>8s}".format("NO2", "O3", "SO2", "CO"))
    for i in range(5):
        print("{:>8.2f} {:>8.2f} {:>8.2f} {:>8.2f}".format(top_months[0][i], \
              top_months[1][i], top_months[2][i], top_months[3][i]))

  
def plot_years(totals_list,maxval,minval):
    '''Plots the total average concetrations for each pollution for particular
    state over 16 years.'''
    no2 = []
    so2 = []
    o3 = []
    co = []
    years = []

    for i in range(2000,2017):
        years.append(i)

    for i in totals_list:
        no2.append(i[0])
        o3.append(i[1])
        so2.append(i[2])
        co.append(i[3])

    fig, ax = pylab.subplots()
    pylab.ylabel('Average Concentration')
    pylab.xlabel('Year')
    pylab.title('Total Average Pollution Per Year')
    ax.plot(years,no2, 'ro')
    ax.plot(years,o3, 'bo')
    ax.plot(years,so2, 'go')
    ax.plot(years,co, 'yo')
    ax.plot(years,no2, 'ro', label='NO2')
    ax.plot(years,o3, 'bo', label='O3')
    ax.plot(years,so2, 'go', label='SO2')
    ax.plot(years,co, 'yo', label='CO')


    ax.legend(loc='upper right', shadow=True, fontsize='small')

    pylab.show()

def main():
    '''Opens/reads file. Prompts for a state name. Loops until vaild name or 
    'quit' is entered. Prompts for a year. If 'quit' is entered for state name
    or year input, quits program. Generates data from functions and displays 
    data. Prompts for whether a graph is wanted of the data. If 'yes' plots
    graph. If 'no', continues program. '''
    fp = open_file()
    read = read_file(fp)
    
    while True:
        while True:
            state_name = input("Enter a state ('quit' to quit): ")
            if state_name.lower() == 'quit':
                break
            elif state_name not in read:
                print("Invalid state.")
            else:
                break
        if state_name.lower() == 'quit':
            break
        year = int(input("Enter a year ('quit' to quit): "))  
        if year == 'quit':
            break
        
        years = total_years(read, state_name)
        city = cities(read, state_name, year)
        month = months(read, state_name, year)
        display(years[0], years[1], years[2], city, month)
        plot = input("Do you want to plot (yes/no)? ")
        if plot == "yes":
            plot_years(years[0],years[1],years[2])
  
if __name__ == "__main__":
    main()          