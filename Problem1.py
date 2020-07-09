##Problem 1:
##
##We have a string “input_str”, and input_str can be any alpha-numeric text with length of 10 to 10000. 
##
##Example of input_str:
##Input_str = “With the recent uptick to the COVID-19 positive cases and many states in various phases of restarting the economy; the food service industry and the restaurant sector have been strongly impacted. DMS Coalition is proud to announce the "Facemasks For Restaurants Donation Initiative.”
##
##We have another variable, an array of words called “validation_array”. It can have upto 1000 items. 
##
##Example of validation_array:
##Validation_array = [“food”, “face”, “donation”, “coalition”, “economy”, “sector”]
##
##We need to identify and print the output that the items in “validation_array” are occurring how many times in input_str. 
##
##Example:
##
##input_str = “With the recent uptick to the COVID-19 positive cases and many states in various phases of restarting the economy; the food service industry and the restaurant sector have been strongly impacted. DMS Coalition is proud to announce the "Facemasks For Restaurants Donation Initiative with a target of $2M in donation”
##
##validation_array = [“food”, “face”, “the”, “donation”, “coalition”, “economy”, “sector”]
##
##output:
##
##food: 1
##face: 1
##the: 6
##donation: 2
##coalition: 1
##economy: 1
##sector: 1

import re
Input_str = 'With the recent uptick to the COVID-19 positive cases and many states in various phases of restarting the economy; the food service industry and the restaurant sector have been strongly impacted. DMS Coalition is proud to announce the "Facemasks For Restaurants Donation Initiative with a target of $2M in donation'
validation_array = ["food", "face", "the", "donation", "coalition", "economy", "sector"]
def counter(Input,Validation):
    ins = Input.lower()
    if len(ins)>=10 and len(ins)<=10000 and len(Validation)<=1000:
        for i in Validation:
            num=sum(1 for j in range(len(ins)) if ins.startswith(i,j))
            print(i+':',num)
    else:
        print("Maximum Length Exceded")
##    clean = re.split(r'\W+',Input_str.lower())
##    print(clean)
##    for i in Validation:
##        print(i,clean.count(i))
    
counter(Input_str,validation_array)

