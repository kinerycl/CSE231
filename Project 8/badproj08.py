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
    # does not ignore AQI
    pollution_dict = {}
    fp.readline()
    for line in fp:
        line_list = line.split('"')
        if len(line_list) > 1:
            s_str = line_list[2].strip(',')
            s_list = s_str.split(',')
            no2mean = float(s_list[5])
            o3mean = float(s_list[10]) *1000
            so2mean = float(s_list[15])
            comean = float(s_list[20]) *1000
            r_list = [s_list[2],s_list[3],no2mean,o3mean,so2mean,comean]
            
             # If key is already not created, makes key. Else, appends lists
            # with a different city and date from those already in key's value
            if s_list[0] not in pollution_dict:
                pollution_dict[s_list[0]]=[r_list]
            else:
                counter = 0 # Number of times city/date already in list
                for lst in pollution_dict[s_list[0]]:
                     if lst[0] == r_list[0] and lst[1] == r_list[1]:
                         counter+=1
                if counter == 0: # If not found in list, appends
                    pollution_dict[s_list[0]].append(r_list)
                    
        else:
            line_str = ''.join(line_list)
            line_list = line_str.split(',')
            s_list = line_list[5:]
            no2mean = float(s_list[5])
            o3mean = float(s_list[10]) *1000
            so2mean = float(s_list[15])
            comean = float(s_list[20]) *1000
            r_list = [s_list[2],s_list[3],no2mean,o3mean,so2mean,comean]
            
            # If key is already not created, makes key. Else, appends lists
            # with a different city and date from those already in key's value
            if s_list[0] not in pollution_dict:
                pollution_dict[s_list[0]]=[r_list]
            else:
                counter = 0 # Number of times city/date already in list
                for lst in pollution_dict[s_list[0]]:
                     if lst[0] == r_list[0] and lst[1] == r_list[1]:
                         counter+=1
                if counter == 0: # If not found in list, appends
                    pollution_dict[s_list[0]].append(r_list)

            
            


def total_years(D, state):
    pass

def cities(D, state, year):
    pass

def months(D,state,year):
    pass

def display(totals_list,maxval,minval,D_cities,top_months):
#    "\nMax and Min pollution"
#    "\n{:>10s}{:>10s}"
#    "\nPollution totals by year"
#    "\n{:<6s}{:>8s} {:>8s} {:>8s} {:>8s}"
#    "\nPollution by city")
#    "\n{:<16s}{:>8s} {:>8s} {:>8s} {:>8s}"
#    "\nTop Months")
#    "\n{:>8s} {:>8s} {:>8s} {:>8s}"
    pass
  
def plot_years(totals_list,maxval,minval):
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
#    "Enter a state ('quit' to quit): "
#    "Invalid state."
#    "Enter a year ('quit' to quit): "
#    "Do you want to plot (yes/no)? " 
    fp = open_file()
    reader = cvs.reader(fp)
    read = read_file(fp)
  
if __name__ == "__main__":
    main()          


