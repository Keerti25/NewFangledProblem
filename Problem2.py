##Problem 2:
##
##We have a variable input_array which can contain items with alphanumeric of upto 1000 characters. We have another array called rejected_items. We need a function which will filter input_array and exclude all the items from rejected_items. “Input_array” can contain upto 1000 items, and rejected_items can contain upto 100 items. 
##
##Example:
##Input_array = ["impolite", "cows", "undress", "rule", "illustrious", "beam", "helpless", "gold", "hair", "vacuous", "help", "guess", "squalid", "wonderful", "memorise", "present", "painful", "brake", "sand", "lip", "rainstorm", "talk", "abashed", "box", "partner", "chop", "tenuous", "robin", "trees", "moor", "hunt", "pack", "old-fashioned"]
##
##rejected_items=["cows", "partner", "wonderful", "rainstorm", "pack", "painful"]
##
##Example of output in above example:
##"impolite", "undress", "rule", "illustrious", "beam", "helpless", "gold", "hair", "vacuous", "help", "guess", "squalid", "memorise", "present", "brake", "sand", "lip", "talk", "abashed", "box", "chop", "tenuous", "robin", "trees", "moor", "hunt", "old-fashioned"


Input_array = ["impolite", "cows", "undress", "rule", "illustrious", "beam", "helpless",
               "gold", "hair", "vacuous", "help", "guess", "squalid", "wonderful", "memorise",
               "present","painful", "brake", "sand", "lip", "rainstorm", "talk", "abashed",
               "box", "partner", "chop", "tenuous", "robin", "trees", "moor", "hunt", "pack", "old-fashioned"]
rejected_items=["cows", "partner", "wonderful", "rainstorm", "pack", "painful"]
filtered_items=[]

def filters(inputs,reject):
    if len(inputs)<=1000 and len(reject)<=100:
        for i in Input_array:
            if i not in rejected_items:
                filtered_items.append(i)
        return filtered_items
    else:
        print("List length exceded maximum number")

a=filters(Input_array,rejected_items)

print(*('"{}"'.format(item) for item in a),sep=', ')
            
