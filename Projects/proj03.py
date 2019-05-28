########################################################################
#  Computer Project #3
#
#  Algorithm
#    input orginal currency
#    input target currency
#    input an amount (must be an interger)
#       Loop while amount is not an interger
#           if not an interger, input another amount
#    convert orginal currency amount to target currency amount
#    prompt for further conversions
#       if "yes" continues to compute conversions
#########################################################################

import urllib.request
import string

# Asks user for the orginal currency, currency to convert to, and the amount
# for conversion. Stores these input values. Converts orginal currency string 
# and new currency string to uppercase.
org_curr_str = input("What is the original currency? ")
new_curr_str = input("What currency do you want to convert to? ")
value_int = input("How much do you want to convert (int)? ")
org_curr_str = org_curr_str.upper()
new_curr_str = new_curr_str.upper()

# Variables to count the number of wanted/unwanted characters in  value_int
# and to define kinds of unwanted characters. 
counter_good = 0
counter_bad = 0
bad_char = string.punctuation + string.ascii_letters

# Loop counts the number of wanted characters verses unwanted.
for char in value_int:
    if char in bad_char:
        counter_bad += 1
    else:
        counter_good += 1

# Loop runs if any unwanted characters are present. If so, it will print a 
# statement that will let the user know, then ask for a new input and evaluate.
while counter_good != len(value_int):
    counter_good = 0
    counter_bad = 0
    print("The value you input must be an integer. Please try again.")
    value_int = input("How much do you want to convert (int)? ")
    for char in value_int:
        if char in bad_char:
            counter_bad += 1
        else:
            counter_good += 1

# Uses imput values to change url. Allowing any conversion to be possible based
# off of users input.
url = "https://finance.google.com/finance/converter?a={}&from={}&to={}"\
.format(value_int, org_curr_str, new_curr_str)
response = urllib.request.urlopen(url)
result = str(response.read())

#Find resulting conversion number in url.
index_span = result.find("span")
num_str = result[index_span + 15:]
index_end = num_str.find(new_curr_str)
conversion_float = float(num_str[:index_end])
print("{} {} is {:.2f} {}".format(value_int, org_curr_str, conversion_float,\
new_curr_str))

# Asks if another conversion is wanted which continues loop
ans_str = input("Do you want to convert another currency? ")

# Loop to continue conversions
while ans_str.lower() == "yes":

    # Asks user for the orginal currency, currency to convert to, and the amount
    # for conversion. Stores these input values. Cinverts orginal currency 
    # string and new currency string to uppercase.
    org_curr_str = input("What is the original currency? ")
    new_curr_str = input("What currency do you want to convert to? ")
    value_int = input("How much do you want to convert (int)? ")
    org_curr_str = org_curr_str.upper()
    new_curr_str = new_curr_str.upper()
    
    # Variables to count the number of wanted/unwanted characters in  value_int
    # and to define kinds of unwanted characters. 
    counter_good = 0
    counter_bad = 0
    bad_char = string.punctuation + string.ascii_letters
    
    # Loop counts the number of wanted characters verses unwanted.
    for char in value_int:
        if char in bad_char:
            counter_bad += 1
        else:
            counter_good += 1
    
    # Loop runs if any unwanted characters are present. If so, it will print a 
    # statement that will let the user know, then ask for a new input and 
    #evaluate.
    while counter_good != len(value_int):
        counter_good = 0
        counter_bad = 0
        print("The value you input must be an integer. Please try again.")
        value_int = input("How much do you want to convert (int)? ")
        for char in value_int:
            if char in bad_char:
                counter_bad += 1
            else:
                counter_good += 1

    # Uses imput values to change url. Allowing any conversion to be possible
    # based off of users input.
    url = "https://finance.google.com/finance/converter?a={}&from={}&to={}"\
    .format(value_int, org_curr_str, new_curr_str)
    response = urllib.request.urlopen(url)
    result = str(response.read())
    
    #Find resulting conversion number in url.
    index_span = result.find("span")
    num_str = result[index_span + 15:]
    index_end = num_str.find(new_curr_str)
    conversion_float = float(num_str[:index_end])
    print("{} {} is {:.2f} {}".format(value_int, org_curr_str,\
    conversion_float, new_curr_str))

    
    # Asks if another conversion is wanted which continues loop
    ans_str = input("Do you want to convert another currency? ")

