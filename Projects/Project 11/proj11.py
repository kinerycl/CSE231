###########################################################
#  Computer Project #11
#
#  Algorithm
#    opens a csv file
#       minimize file
#       sets desired columns to desired special
#       sets width
#       writes data into text file
#       writes data into csv file
#       gets/prints the min/max act
#       gets/prints the min/max earnings
###########################################################
import csv 
class Cell(object):
    ''' This class creates a cell from csv_worker. It contains the csv_worker,
    value, column, and alignment. '''
    
    def __init__(self, csv_worker = None, value = '', column = 0, \
                 alignment = '^'):
        ''' Initalizes class with variables for csv data, value, column, and 
        alignment. '''
        self.__csv_worker = csv_worker
        self.__value = value
        self.__column = column
        self.__alignment = alignment
    
    def __str__(self):
        ''' Prints a formatted value by alignment and width. If the value is 
        special (currency/percentage), formats it based on it's speciality
        first. '''
        if self.__csv_worker.get_special(self.__column-1) == percentage: 
            val = percentage(self.__value)
        elif self.__csv_worker.get_special(self.__column-1) == currency: 
            val = currency(self.__value)
        else:
            val = self.__value
            
        w = self.__csv_worker.get_width(self.__column-1) 
        S = "{:{align}{width}}".format(val, align=self.__alignment, width=w)

        return S

    def __repr__(self):
        ''' Represents the value when called. '''
        return self.__str__()
    
    def set_align(self, align):
        ''' Alters the alignment based on the given alignment.'''
        if align == '^': 
            self.__alignment = align
        elif align == '<':
            self.__alignment = align
        elif align == '>':
            self.__alignment = align
        else:
            raise TypeError
        
    def get_align(self):
        ''' Returns alignment. '''
        return self.__alignment
    
    def set_value(self, value):
        ''' Alters value wanted value. '''
        self.__value = value
    
    def get_value(self):
        ''' Returns value.'''
        return self.__value

class CsvWorker(object):
    ''' This class reads a file and extracts/stores the data. '''
    
    def __init__(self, fp = None):
        ''' Initalizes class to contain columns, rows, data, widths, and 
        special. Reads file. '''
        self.__columns = 0
        self.__rows = 0
        self.__data = []
        self.__widths = []
        self.__special = []
        if fp:
            self.read_file(fp)
    
    def read_file(self, fp): 
        ''' Reads file and alters the classes variables so that it contains
        information from the file. '''
        row = 0
        w_dict = {}
        reader = csv.reader(fp)
        for line_list in reader:
            row += 1
            column = 0
            data = []
            for item in line_list:
                column += 1 
                
                # checks data for "NULL" and appends 
                if item == "Null":
                    item = ""
                c = Cell(self,item, column)
                data.append(c)
               
                # creates width dictionary
                if column in w_dict:
                    if len(item) > w_dict[column]:
                        w_dict[column] = len(item)
                else:
                    w_dict[column] = len(item)
            self.__data.append(data)
               

        # number of rows
        self.__rows = row
        
        # creats special placeholder (None) for every column
        for i in range(column+1): 
            self.__special.append(None)

        # appends the widths from w_dict to self.__withs(list)
        for val in w_dict.values():
            self.__widths.append(val)
            
        # number of columns
        self.__columns = len(self.__widths)
        
    def __getitem__(self, index):
        ''' Returns a value of the data list at the given index. '''
        return self.__data[index]
    
    def __setitem__(self, index, value):
        ''' Alters the value at given index of the data list. '''
        self.__data[index] = value
    
    def __str__(self): 
        ''' Prints the variable as a string. '''
        data  = ''
        for row in self.__data:
            for item in row:
                cha = str(item)
                data += cha
            data += '\n'
        return data
    
    def __repr__(self):
        ''' Represents the variable when called. '''
        return self.__str__()
    
    def limited_str(self, limit): 
        ''' Limits the data's rows to the given limit. '''
        data  = ''
        for i in range(limit):
            row = self.__data[i]
            for item in row:
                cha = str(item)
                data += cha
            data += '\n'
        return data

    def remove_row(self, index):
        ''' Removes the row. '''
        self.__data.pop(index)
    
    def set_width(self, index, width):
        ''' Alters the width value of the given column in the list.'''
        self.__widths[index] = width

    def get_width(self, index):
        ''' Returns the width.'''
        return self.__widths[index]

    def set_special(self, column, special):
        ''' Alters the special value of the given column in the list.'''
        self.__special[column] = special

    def get_special(self, column):
        ''' Returns the special value. '''
        return self.__special[column]

    def set_alignment(self, column, align): 
        ''' Sets the alignment for the data.'''
        for row in self.__data:
            row[column].set_align(align)
    
    def get_columns(self):
        ''' Returns the columns.'''
        return self.__columns
    
    def get_rows(self):
        ''' Returns the rows.'''
        return self.__rows
    
    def minimize_table(self, columns):
        ''' Creates/Returns a new CsvWorker object that is a minimized version 
        of the orginal based on the columns given.'''
        new_instance = CsvWorker()
        
        # initialize new data
        new_data = []
        for i in range(self.__rows):
            new_data.append([])
            
        # initialize widths of new_instance
        widths = []
        for i in columns:
            w = self.__widths[i] # get width from original worker
            widths.append(w)
        
        new_instance.__widths = widths
        
            
        for row in range(self.__rows):
            count = 0
            for col in columns:
                v = self.__data[row][col].get_value()
                a = self.__data[row][col].get_align()
                c = Cell(new_instance, v, count, a)
                new_data[row].append(c)
                count += 1
            
        new_instance.__data = new_data
        new_instance.__rows = self.__rows
        new_instance.__columns = len(columns)
        
        special = []
        for i in columns:
            special.append(self.__special[i])
        new_instance.__special = special
        
        return new_instance
    
    def write_csv(self, filename, limit = None):
        ''' Writes data into a csv file. '''
        name_file = open(filename, 'w')
                
        for i in range(limit):
            row = self.__data[i]
            s = ''
            for cell in row:
                val = cell.get_value()
                if val != 'NULL':
                    s += val + ','
                else:
                    s += ','
            name_file.write( s[:-1] + '\n')
               

        name_file.close()
        
    def write_table(self, filename, limit = None): 
        ''' Writes data into a text file. '''
        name_file = open(filename, 'w')
        name_file.write(self.limited_str(limit))        

        name_file.close()
        
    def minimum(self, column):
        '''Find the minimum value in the given column and returns.'''
        min_cell = None
        min_val = 99999999999999999999999
        for row in self.__data:
            try:
                item = float(row[column].get_value())
                if item < min_val:
                    
                    min_cell = row[column]
                    min_val = item
            except ValueError:
                    continue
        return min_cell
    
    def maximum(self, column): 
        ''' Finds the maximum value in the given column and returns. '''
        max_cell = None
        max_val = 0
        for row in self.__data:
            try:
                item = float(row[column].get_value())
                if item > max_val:
                    
                    max_cell = row[column]
                    max_val = item
            except ValueError:
                    continue
        return max_cell
        
def open_file():
    ''' Loops until vaild file is entered. Once vaild file is entered
    opens file and returns. '''
    while True:
        filename = input("Input a file name: ")
        try: 
            open_file = open(filename, encoding="utf-8") 
            return open_file
        except FileNotFoundError:
            print("File not found. Try again")
            
def percentage(value): 
    ''' Formats a float into a percent. If value is not a float, returns 
    unaltered value. '''
    try:
        value_float = float(value)
        value_percent = "{:.1f}%".format(value_float)
        return value_percent
        
    except ValueError:
        return value
        

def currency(value): 
    ''' Formats a float into a dollar amount. If value is not a float, returns 
    unaltered value. '''
    try:
        value_float = float(value)
        value_percent = "${:,.2f}".format(value_float)
        return value_percent
        
    except ValueError:
        return value

def main():
    ''' Opens file and minimizes the table based on given parameters. Sets given
    columns to special. Sets the width to previous width plus 4. Writes a table 
    and a csv. Prints the Max/Min ACT and the Max/Min Earnings. '''
    fp = open_file()
    
    master = CsvWorker(fp)
    
    csv_worker = master.minimize_table([3,5,40,55,116,118,122])
    
    csv_worker.set_special(3, percentage)
    csv_worker.set_special(6, percentage)
    csv_worker.set_special(4, currency) 
    csv_worker.set_special(5, currency)
    
    for i in range(len(csv_worker[0])):
        csv_worker.set_width(i, csv_worker.get_width(i) + 4)
    
    csv_worker.write_table("output.txt",10)
    csv_worker.write_csv("output.csv", 10)

    max_act = csv_worker.maximum(2)
    min_act = csv_worker.minimum(2)
    
    max_earn = csv_worker.maximum(4)
    min_earn = csv_worker.minimum(4)

    print("Maximum ACT:", str(max_act).strip()) 
    print("Minimum ACT:", str(min_act).strip()) 
    print("Maximum Earnings:", str(max_earn).strip()) 
    print("Minimum Earnings:", str(min_earn).strip()) 

if __name__ == "__main__":
    main()
