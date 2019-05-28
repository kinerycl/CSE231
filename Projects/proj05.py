def open_file():
    file_name = input("Input a file name: ")
    try:
        open_file = open(file_name, 'r')
        return open_file
    except FileNotFoundError:
        print("Unable to open the file. Please try again.")
        
def read_data(fp, input_str, search_str):
    pass
        
def display_line(country_name, region_name, happiness_score):
    pass
    #"{:24s}{:<32s}{:<17.2f}"

def main():
    pass
    #"Input 1 to search in country names, 2 to search in regions: "    
    #"Invalid choice, please try again!"
    #"What do you want to search for? "
    #"{:24s}{:<32s}{:<17s}"

if __name__ == '__main__':
   main()
