########################################################################
#  Computer Project #5
#
#  Algorithm
#    prompt for a file name
#        open file
#           prompt for an input for either country or region to search
#           prompt for a keyword input to search
#           search file for keyword
#              display search results
#        close file
#########################################################################

def open_file():
    '''Loops until vaild file is entered. Once vaild file is entered
    opens file and returns '''
    while True:
        fp = input("Input a file name: ")
        try: 
            open_file = open(fp, 'r')
            return open_file
        except FileNotFoundError:
            print("Unable to open the file. Please try again.")
        
def read_data(fp, input_str, search_str):
    ''' Finds the country, region, and happiness score with in the data based 
    on user input. Prints each. Finds and prints the average of the happiness 
    scores printed. '''
    avg_denom = 0 # denominator for average calculation counter
    avg_numer = 0 # numerator for average calculation counter
    
    # Uses input to determine what index to search keyword in 
    if input_str == 1:
        input_index = 0
    elif input_str == 2:
        input_index = 1
    
    # Searches for keywords within index given. Finds and prints country,
    # region, happiness score, and average happiness score.
    for line in fp:
        line = line.split(',')
        if search_str in line[input_index]:
            line = line[:3]
            display_line(line[0], line[1], float(line[2]))
            avg_denom += 1
            avg_numer += float('{:.2f}'.format(float(line[2])))
    print('-'*71)
    print("{:24s}{:<32s}{:<17.2f}".\
          format("Average Happiness Score", " ", avg_numer/avg_denom))
        
        
def display_line(country_name, region_name, happiness_score):
    ''' Formats the country name, region name, and happiness score '''
    print("{:24s}{:<32s}{:<17.2f}".format(country_name, region_name,\
         happiness_score))


def main():
    ''' Prompts for file input and repeats until vaild file is entered. 
    Prompts for a number '1', country, or '2', region. Prompts for search 
    input, a keyword in either a country or a region. Capitalizes the first 
    letter in the search input. Searches for matches based on keyword and 
    prints the names of the countries, their regions, happiness scores, and 
    average happiness. Closes file. '''
    fp = open_file()
   
    # Varifies that input is either '1' or '2'. If not, displays an error 
    # message and asks for a new input.
    while True:
        input_str = \
        input("Input 1 to search in country names, 2 to search in regions: ")
        if input_str != "1" and input_str != "2":
            print("Invalid choice, please try again!")
        else:
            input_str = int(input_str)
            break
            
        
    search_str = input("What do you want to search for? ")
    
    # Takes the input search_str and capitalizes first letter
    search_list = list(search_str)
    search_list = [ch for ch in search_str]
    search_list[0] = search_str[0].upper()
    search_str = search_list[0] + search_str[1:]
    
    # Prints a table of data. Does so by printing a header, line, data, line, 
    # and average.
    print("{:24s}{:<32s}{:<17s}".format('Country', "Region", "Happiness Score"))
    print('-'*71)
    read_data(fp, input_str, search_str)
    
    fp.close()
    
    
    

if __name__ == '__main__':
   main()
