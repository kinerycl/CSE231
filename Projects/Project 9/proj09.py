#########################################################################
#  Computer Project #9
#
#  Algorithm
#    display opening banner and menu
#    prompts for a choice
#       loops until vaild choice is entered (1 or 2)
#    if choice is 1 
#       prompts for plaintext, ciphertext, bifurcation, and texttodecrypt
#       calls chosen_plaintext_attack to decipher
#    if choice is 2 
#       prompts for ciphertext
#       prompts for and opens a file
#           creates dicitonary 
#       calls bruteforce_shift_cipher to decipher
##########################################################################
from math import log10
import string

def open_file():
    ''' Loops until vaild file is entered. Once vaild file is entered
    opens file and returns. '''
    while True:
        fp = input("Input a file name: ")
        try: 
            open_file = open(fp, 'r')
            return open_file
        except FileNotFoundError:
            print("Unable to open the file. Please try again.")

def chosen_plaintext_attack(plaintext, ciphertext, bifurcation, texttodecrypt):
    ''' Using plaintext, corresponding ciphertext, and bifurcation a cipher
    is created and stored in a dictionary. Uses dictionary to decrypt the 
    texttodecrypt. If able to decrypt text, prints decryption. If not, prints
    which key was missing from the dicitonary. '''
    cipher_dict = {}
    decryption_str=[]
    orginal_texttodecrypt = texttodecrypt
    
    # Creates a dictionary with corresponding cipher values to letters
    # Keys are cipher values and values are letters
    for i in range(len(plaintext)):
        key = ciphertext[:bifurcation]
        ciphertext = ciphertext[bifurcation:]
        cipher_dict[key]=plaintext[i]
    
    # Decrypts text by going through dictionary and comparing keys to given 
    # characters combinations. If character combinations not in dicitonary, 
    # prints an error message. 
    for i in range(int(len(texttodecrypt)/bifurcation)):
        cipher_val = texttodecrypt[:bifurcation]
        texttodecrypt = texttodecrypt[bifurcation:]
        if cipher_val in cipher_dict:
            decryption_str.append(cipher_dict[cipher_val])
        else:
            print("Decryption interrupted. Key not found: {}".format(\
                  cipher_val))
            break
        
    # If decryption is complete prints decrypted text
    decryption = ''.join(decryption_str)
    if int(len(orginal_texttodecrypt)/bifurcation) == len(decryption_str):
        print("Decrypted text:", decryption)
        
def log_probability_dictionary(fp):
    ''' Intakes/reads a file and creates a dictionary where keys are quadgrams 
    and values are lists containing frequency and calculated log probability. 
    Finds top ten quadgrams based off of frequency and prints a table of the 
    top ten quadgrams, their counts, and log probilities. Returns dicitonary.
    '''
    # Creates dictionary      
    log_prob_dict = {}
    for line in fp:
        line = line.split()
        log_prob_dict[line[0]] = []
        log_prob_dict[line[0]].append(int(line[1]))
    
    # Creates Total Quadgrams
    total_quad = 0
    for val in log_prob_dict.values():
        num = int(val[0])
        total_quad += num
    
    # Creates and appends log probablitiy to dictionary value list
    for val in log_prob_dict.values():
        num = int(val[0])
        log_prob = log10(num/total_quad)
        val.append(log_prob)
        
    # Creates list of top ten
    freq_lst = [val[0] for val in log_prob_dict.values()]
    freq_lst.sort(reverse = True)
    top_ten = freq_lst[:10]
    
    # Prints top ten table
    print("\n{:<8s}{:>13s}{:>22s}".format('Quadgram','Count','Log Probability'))
    print("-------------------------------------------") 
    
    for freq in top_ten:
        for key, val in log_prob_dict.items():
            if freq in val:
                print("\n{:<8s}{:>13}{:>22.6f}".format(key, val[0],val[1]))

    return log_prob_dict

        
def bruteforce_shift_cipher(ciphertext, ngrams_dictionary):
    ''' Decrypts ciphertext by creating all possible ciphers and finding how 
    well they fit with the ciphertext. Prints the top 5 most fit ciphers' key, 
    plaintext, and fitness. Prompts to press any key and prints the most fit
    plaintext. '''
    print("{:<5s}{:^35s}   {:>10s}".format("\nKey", "Plaintext", "Fitness")) 
    print("------------------------------------------------------") 

    fitness_lst = []
    alpha = string.ascii_uppercase
    ciphertext = ciphertext.upper()
    
    # Creates all possible ciphers
    for i in range(25):
        key = i
        mapping_dict = {}
        ciphertext_lst = []
        rotating_str = string.ascii_uppercase[i:]+string.ascii_uppercase[:i]
        for i in range(26):
            mapping_dict[alpha[i]] = rotating_str[i]
        for cha in ciphertext: # Removes unwanted/appends wanted characters
            if cha != ' ' and cha not in string.punctuation:
                cipher_cha = mapping_dict[cha]
                ciphertext_lst.append(cipher_cha)
        plaintext = ''.join(ciphertext_lst)
        fit = fitness_calculator(plaintext, ngrams_dictionary)
        fitness_lst.append((fit, key, plaintext))
    fitness_lst.sort(reverse = True)
    
    # Prints top 5 in table
    for i in range(5):
        print("{:<5}{:^35s}   {:>10.4f}".format(fitness_lst[i][1],\
              fitness_lst[i][2][:35],fitness_lst[i][0]))
    
    resume = input("\npress any key to continue...")
    print("\nDecrypted ciphertext: ", fitness_lst[0][2])
    
def fitness_calculator(potential_plaintext, quadgram_dictionary):
    ''' Intakes potential plaintext and a quadgram dictionary. Finds quadgrams 
    for potential plaintext and compares them to quadgrams in dictionary. If 
    quadgram is in dicitonary, adds the probability to the fit value. Returns 
    fit value. '''
    # Creates a list of quadgrams from given word
    plain_quadgrams = []
    for i in range(len(potential_plaintext)):
        quadgram = potential_plaintext[i:i+4]
        if len(quadgram) == 4:
            plain_quadgrams.append(quadgram)

    # Finds the fit value by adding probablities if quadgram is in dictionary
    fit_val = 0
    for quad in plain_quadgrams:
        if quad in quadgram_dictionary:
           fit_val += quadgram_dictionary[quad][1]
            
    return fit_val

def main():
    ''' Prints a welcome banner and menu. Prompts for choice 1 or 2. Loops until 
    vaild choice is entered. If choice is 1, prompts for plaintext, 
    ciphertext, bifurcation, and texttodecrypt. Uses entered values to find the
    plaintext using chosen_plaintext_attack. If choice is 2, open a file and 
    create a dicitonary from that file. Prompt for a ciphertext to decrypt. 
    Decrypts ciphertext using bruteforce_shift_cipher. '''
    BANNER = """\
    ------------------------------------------------------------------------
    Welcome to the world of code breaking. This program is meant to help
    decipher encrypted ciphertext in absence of knowledge of algorithm/key.
    ------------------------------------------------------------------------
    """
    MENU = """\
    1. Chosen plaintext attack
    2. Ngram frequency analysis
    """
    print(BANNER)
    print(MENU)
    
    while True:
        choice = input("Choice: ") 
        try:
            choice = int(choice)
            if choice == 1:
                break
            elif choice == 2:
                break
        except ValueError:
            print("Invalid input.")
            continue
        print("Invalid input.")
    
    
    if int(choice) == 1:
        plaintext = input("Plaintext: ")
        ciphertext = input("Ciphertext: ")
        bifurcation = int(input("Bifurcation: "))
        texttodecrypt = input("Text to decrypt: ")
        plain = chosen_plaintext_attack(plaintext, ciphertext,\
                                        bifurcation, texttodecrypt)
    elif int(choice) == 2:
        fp = open_file()
        ngrams_dictionary = log_probability_dictionary(fp)
        ciphertext = input("Ciphertext:")
        plaintext = bruteforce_shift_cipher(ciphertext, ngrams_dictionary)
        
    
if __name__ == "__main__":
    main()
            

    
    
    
    


    
        
        
