##############################################################################
#  Computer Project #6
#
#  Algorithm
#    prompt for a file name
#        open file
#        read file
#           prompt for an a chromsome, 'all', or 'quit'
#           if input is chromosome or 'all'
#               extract chromosome, extract genome, and compute gene length
#               print chromosome name, mean, and standard deviation
#           if input is 'quit'
#               end program
#           if input is neither
#               `print error message
#                reprompt
#        close file
##############################################################################

import math
CHROMOSOMES = ['chri','chrii','chriii','chriv','chrv','chrx']

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
    ''' Reads file line by line. Makes each line into a tuple containing
    only the chromosome name, gene start, and gene end. Appends each tuple to
    a new list. Sorts and returns list. '''
    gene_list = []
    for line in fp:
        if line[0] == 'c': # ignores lines without a chromosome name
            line = line.split()
            line_tup = tuple([line[0], int(line[3]), int(line[4])]) 
            gene_list.append(line_tup)
    gene_list.sort()
    return gene_list

def extract_chromosome(genes_list, chromosome):
    ''' Intakes a list of genes and a chromosome name. Searches gene list and 
    for given chromosome. For each set of data found, appends to a new list. 
    Sorts new list and returns. '''
    chrom_gene_list = []
    for i in genes_list:
        if i[0] == chromosome:
            chrom_gene_list.append(i)
    chrom_gene_list.sort()
    return(chrom_gene_list)

def extract_genome(genes_list):
    ''' Intakes a gene list. Creates a new list of list of tuples based on 
    the six different chromosomes. Returns the new list. '''
    genome_list = []
    for i in CHROMOSOMES:
        genome_list.append(extract_chromosome(genes_list, i))
    return genome_list
    
def compute_gene_length(chrom_gene_list):
    ''' Intakes a chromosome gene list and computes the gene mean and gene
    standard deviation. Returns both values'''
    chrom_length_list = []
    
    # Finds the gene mean
    for i in chrom_gene_list:
        length = i[2] - i[1] + 1 
        chrom_length_list.append(length)
    gene_mean = sum(chrom_length_list)/len(chrom_length_list) 
        
    # Finds the standard deviation
    stddev_num = 0
    for i in chrom_length_list:
        stddev_num += (i - gene_mean)**2
    gene_stddev = math.sqrt(stddev_num/len(chrom_length_list))
    return_tup = gene_mean, gene_stddev
    return return_tup
    
def display_data(gene_list, chrom):
    ''' Intakes a gene list and chromosome name. Formats the name of the 
    chromosome so that the roman numerals are capitalized. Formats the 
    chromosome name and items with in the gene list and prints. '''
    chrom = chrom[:3] + chrom[3:].upper() 
    print("{:<11s}{:9.2f}{:9.2f}".format(chrom, gene_list[0], gene_list[1]))
    
    
def main():
    ''' Opens and reads file. Prints message concerning programs function
    Prompts for an input (either a chromosome name, "all', or 'quit'. If
    not a vaild input prints an error message. If input is vaild, prints a 
    chart of the chromosome, mean, and standard deviation of the desired 
    chromosomes. Loops until input is 'quit'. '''
    fp = open_file()
    gene_list = read_file(fp)
    print("Gene length computation for C. elegans.")
     
    while True:
        chrom_name = input("\nEnter chromosome or 'all' or 'quit': ")
        chrom_name = chrom_name[:].lower()
        if chrom_name in CHROMOSOMES:
            print("Chromosome Length")
            print("{:<11s}{:>9s}{:>9s}".format("chromosome", "mean", "std-dev"))
            display_data(compute_gene_length(extract_chromosome(gene_list, chrom_name)), chrom_name)
        elif chrom_name.lower() == 'all':
            print("Chromosome Length")
            print("{:<11s}{:>9s}{:>9s}".format("chromosome", "mean", "std-dev"))
            for i in CHROMOSOMES:
                i = str(i)
                display_data(compute_gene_length(extract_chromosome(gene_list, i)), i)
        elif chrom_name.lower() == 'quit': 
            break
        else:
            print("Error in chromosome.  Please try again.")
    fp.close()


if __name__ == "__main__":
    main()
