###########################################################
#  Computer Project #2
#
#  Algorithm
#    prompt for an integer
#    input an integer
#    loop while input is greater than or equal to zero
#       print inital int
#       compute 2017 tax and print
#       compute 2018 tax and print
#       compute tax difference and print
#       compute tax difference as a percent and print 
#       input an integer
#   Terminates once negitive integer/string is input
###########################################################

# input income
income_str = input("Enter income as an integer with no commas: ")
income_int = int(income_str) #income conversion to int

# 2017 tax (fixed) amounts
TAX_10_17 = 932.5
TAX_15_17 = 4293.75
TAX_25_17 = 13487.5
TAX_28_17 = 27930
TAX_33_17 = 74266.5
TAX_35_17 = 595

# 2018 tax (fixed) amounts
TAX_10_18 = 952.5
TAX_12_18 = 3501
TAX_22_18 = 9636
TAX_24_18 = 18000
TAX_32_18 = 13600
TAX_35_18 = 105000

# compute and print income, 2017 tax, 2018 tax, difference, and difference 
# percent -- rounding outputs to two decimal places -- while input int is 
# greater than or equal zero. 
while income_int >= 0:
    print("Income:", income_int)
    
    # 2017 taxes computation and printed
    if income_int > 0 and income_int <= 9325: # 1st 2017 tax bracket
        tax_10_17 = round((income_int * .1), 2) 
        total_tax_17= tax_10_17
        print("2017 tax:", total_tax_17)  
    elif income_int > 9325 and income_int <= 37950: # 2nd 2017 tax bracket
        tax_15 = (income_int - 9325) * .15 
        total_tax_17 = round((TAX_10_17 + tax_15), 2)
        print("2017 tax:", total_tax_17)
    elif income_int > 37950 and income_int <= 91900: # 3rd 2017 tax bracket
        tax_25 = (income_int - 37950) * .25 
        total_tax_17 = round((TAX_10_17 + TAX_15_17 + tax_25), 2) 
        print("2017 tax:", total_tax_17) 
    elif income_int > 91900 and income_int <= 191650: # 4th 2017 tax bracket
        tax_28 = (income_int - 91900) * .28 
        total_tax_17 = round((TAX_10_17 + TAX_15_17 + TAX_25_17 + tax_28), 2)
        print("2017 tax:", total_tax_17) 
    elif income_int > 191650 and income_int <= 416700: # 5th 2017 tax bracket
        tax_33 = (income_int - 191650) * .33 
        total_tax_17 = round((TAX_10_17 + TAX_15_17 + TAX_25_17 + TAX_28_17 + \
                              tax_33), 2)
        print("2017 tax:", total_tax_17)
    elif income_int > 416700 and income_int <= 418400: # 6th 2017 tax bracket
        tax_35 = (income_int - 416700) * .35 
        total_tax_17 = round((TAX_10_17 + TAX_15_17 + TAX_25_17 + TAX_28_17 \
                              + TAX_33_17 + tax_35), 2)
        print("2017 tax:", total_tax_17)
    else: # 7th 2017 tax bracket
        tax_39 = (income_int - 418400) * .396 
        total_tax_17 = round((TAX_10_17 + TAX_15_17 + TAX_25_17 + TAX_28_17 \
                              + TAX_33_17 + TAX_35_17 + tax_39), 2)
        print("2017 tax:", total_tax_17)
   
    # 2018 taxes computation and printed
    if income_int > 0 and income_int <= 9525: # 1st 2018 tax bracket
        tax_10_18 = round((income_int * .1), 2) 
        total_tax_18 = tax_10_18
        print("2018 tax:", total_tax_18)  
    elif income_int > 9525 and income_int <= 38700: # 2nd 2018 tax bracket
        tax_12_18 = (income_int - 9525) * .12 
        total_tax_18 = round((TAX_10_18 + tax_12_18), 2) 
        print("2018 tax:", total_tax_18)
    elif income_int > 38700 and income_int <= 82500: # 3rd 2018 tax bracket
        tax_22_18 = (income_int - 38700) * .22 
        total_tax_18 = round((TAX_10_18 + TAX_12_18 + tax_22_18), 2) 
        print("2018 tax:", total_tax_18) 
    elif income_int > 82500 and income_int <= 157500: # 4th 2018 tax bracket
        tax_24_18 = (income_int - 82500) * .24 
        total_tax_18 = round((TAX_10_18 + TAX_12_18 + TAX_22_18 + tax_24_18), 2)
        print("2018 tax:", total_tax_18) 
    elif income_int > 157500 and income_int <= 200000: # 5th 2018 tax bracket
        tax_32_18 = (income_int - 157500) * .32 
        total_tax_18 = round((TAX_10_18 + TAX_12_18 + TAX_22_18 + TAX_24_18 \
                              + tax_32_18), 2)
        print("2018 tax:", total_tax_18)
    elif income_int > 200000 and income_int <= 500000: # 6th 2018 tax bracket
        tax_35_18 = (income_int - 200000) * .35 
        total_tax_18 = round((TAX_10_18 + TAX_12_18 + TAX_22_18 + TAX_24_18 \
                              + TAX_32_18 + tax_35_18), 2)
        print("2018 tax:", total_tax_18)
    else: # 7th 2018 tax bracket
        tax_37_18 = (income_int - 500000) * .37 
        total_tax_18 = round((TAX_10_18 + TAX_12_18 + TAX_22_18 + TAX_24_18 \
                              + TAX_32_18 + TAX_35_18 + tax_37_18), 2)
        print("2018 tax:", total_tax_18)
    
    # compute differences and print    
    print("Difference:", round((total_tax_18 - total_tax_17), 2))
    print("Difference (percent):", round(((total_tax_17 - total_tax_18)\
                                         /total_tax_17) * 100, 2))
    # input income (contiues loop)  
    income_str = input("Enter income as an integer with no commas: ") 
    income_int = int(income_str) 