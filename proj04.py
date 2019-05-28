###########################################################
#  Computer Project #6
#
#  Algorithm
#   prompts for rotation (integer)
#       if not able to convert to an integer prompt again 
#   prompts for a command ('d','e','q')
#   loops while prompt not 'q'
#       if 'e', prompts for a string
#           encrypts string
#           prints cipher string and orginal string
#       if 'd', prompts for a string
#           decrypts string
#           prints orginal string and cipher string
#       if 'q', ends loop and ends program
#       prompts for a command('d','e','q')
############################################################

import string
PUNCTUATION = string.punctuation
ALPHA_NUM = string.ascii_lowercase + string.digits

def multiplicative_inverse(A,M):
    '''Return the multiplicative inverse for A given M.
       Find it by trying possibilities until one is found.'''
       
    for x in range(M):
        if (A*x)%M == 1:
            return x
  
def check_co_prime(num, M):
    '''Returns "True" if numbers are co-primes.
       Returns "False" if numbers and not co-primes.'''
    num_int = int(num)
    M_int = int(M)
    # Find divisors, besides "1", for "num" and check if "M" is divisible
    # If so, "M" and "N" are not co-primes
    for i in range(2, num_int+1):
        if num_int % i == 0:
            if M_int % i == 0:
                return False
    else:
        return True
    
def get_smallest_co_prime(M):
    '''Finds the smallest co-prime and returns value.
       Finds it by try possiblities until it is found.'''
    for i in range(2, M):
        if check_co_prime(i, M) == True:
            return(i)
            break
        
def caesar_cipher_encryption(ch,N,alphabet):
    '''Intakes a character, rotation value, and alphabet.
       Puts imputs in to the Ceaser Cipher for encryption.
       Returns the corresponding character. '''
    ch_int = alphabet.index(ch)
    ch_y = (ch_int + N)%len(alphabet) # Ceaser Cipher encryption
    return(alphabet[ch_y])

def caesar_cipher_decryption(ch,N,alphabet):
    '''Intakes a character, rotation value,and alphabet.
       Puts imputs in to the Ceaser Cipher for decryption
       Returns the corresponding character.'''
    ch_int = alphabet.index(ch)
    ch_y = (ch_int - N)%len(alphabet) # Ceaser Cipher decryption
    return(alphabet[ch_y])
        
def affine_cipher_encryption(ch,N,alphabet):
    '''Intakes a character, rotation value, and alphabet.
       Puts imputs in to the Affiine Cipher for encryption.
       Returns the corresponding character.'''
    A = get_smallest_co_prime(len(alphabet))
    ch_int = alphabet.index(ch)
    ch_y = (A*ch_int + N)%len(alphabet) # Affine Cipher encryption
    return(alphabet[ch_y])

def affine_cipher_decryption(ch,N,alphabet):
    '''Intakes a character, rotation value, and alphabet.
       Puts imputs in to the Affiine Cipher for decryption.
       Returns the corresponding character.'''
    A = get_smallest_co_prime(len(alphabet))
    A_inverse = multiplicative_inverse(A, len(alphabet))
    ch_int = alphabet.index(ch)
    ch_y = A_inverse*(ch_int - N)%len(alphabet) # Affine Cipher decryption
    return(alphabet[ch_y])
    
def main():    
    '''Prompts for N (rotation), a command, and a string.
    Decrypts/encrypts string based on command.'''
    
    # Prompts for rotation and checks to see if string is an integer. If not an 
    # integer, checks if string is only numbers and converts to an integer. If
    # string does not consist of numbers only, reprompts for new rotation.
    N = input("Input a rotation (int): ")
    while N is str(N):
        if N.isdigit():
            N = int(N)
        else:
            print("Error; rotation must be an integer.")
            N = input("Input a rotation (int): ")
   
    # Prompts for a command (e,d,q). "e" calls encryptiopn function, "d" calls
    # decryption fuction, "q" ends program.
    command = input("Input a command (e)ncrypt, (d)ecrypt, (q)uit: ")
    
    # While loop that continues asking for commands/strs
    while command != "q":
        
        # Runs iff input is "e", encrypt. If the character is a letter/number 
        # use affine cipher and ALPHA_NUM for alphabet. If the character 
        # is punctuation use caesar cipher and PUNCTUATION for alphabet.
        if command == 'e': 
            new_str = ""
            plain_str = input("Input a string to encrypt: ")
            if " " in plain_str:
                print("Error with character:")
                print("Cannot encrypt this string.")
            else:
                print("Plain text:", plain_str)
                plain_str = plain_str.lower()
                for i in plain_str:
                    if i in ALPHA_NUM:
                        i = affine_cipher_encryption(i, N, ALPHA_NUM)
                        new_str += i
                    else:
                        i = caesar_cipher_encryption(i, N, PUNCTUATION)
                        new_str += i 
                print("Cipher text:", new_str)
        
        # Runs if input is "d" decrypt. If the character is a lestter/number 
        # use affine cipher an ALPHA_NUM for alphabet. If the character is 
        # punctuation use caesar cipher and PUNCTUATION for alphabet.
        elif command == "d":
            new_str = ""
            plain_str = input("Input a string to decrypt: ")
            if " " in plain_str:
                print("Error with character:")
                print("Cannot encrypt this string.")
            else:
                plain_str = plain_str.lower()
                for i in plain_str:
                    if i in ALPHA_NUM:
                        i = affine_cipher_decryption(i, N, ALPHA_NUM)
                        new_str += i
                    else:
                        i = caesar_cipher_decryption(i, N, PUNCTUATION)
                        new_str += i
                print("Cipher text:", plain_str)
                print("Plain text:", new_str)
            
        # Runs if input is not "q".
        elif command != "q":
            print("Command not recognized.")
        
        # Prompts for a command (e,d,q). "e" calls encryptiopn function, "d" 
        # calls decryption fuction, "q" ends program.
        command = input("Input a command (e)ncrypt, (d)ecrypt, (q)uit: ")
    
if __name__ == "__main__":
    main()

