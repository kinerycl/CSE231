import string

value_int = input("How much do you want to convert (int)? ")

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

            

