import csv

# This definition is to convert the input string of function into a csv file for finding the co-factors.
def function_to_csv (function, csv_file):
    function_cubes = function.split("+")

    with open(csv_file, 'w', newline='') as file:
        writer = csv.writer(file)
        for i in function_cubes:
            writer.writerow(i)
            
# This is the definition to find the shanon cofactors. var is the splitting variable and
# fn_loc is the location of the file containing the function.
# This definition returns a string which is a co-factor of function with respect to spliting variable.
def co_factor(var, fn_loc):
    #Finding the complement of the input splitting variable
    if var.isupper():                                        
        var_com = var.lower()
    else:
        var_com = var.upper()
    text_list = list()
# flag counts the number of cubes that are deleted from the list.
    flag = 0
    f = ""
    with open(fn_loc) as file_obj:
        reader_obj = csv.reader(file_obj)
        text_list = list(reader_obj)
        no_of_cubes = len(text_list)
        for cube in range(0, no_of_cubes):
# If the function has the spliting variable as a cube, then making the cofactor 1.
            if text_list[cube-flag] == [var]:
                text_list = ["1"]
                break
# If the cube of the function has the spliting variable, then it is removed from the cube
# leaving the other literals. This is equivalent to making the literal equal 1 in the cube. 
            elif var in text_list[cube-flag]:
                text_list[cube-flag].remove(var)
# If the cube of the function has the complement of spliting variable, then the entire cube is removed. 
# This is equivalent to making the complement of spliting variable equal to 1. 
            elif var_com in text_list[cube-flag]:
                text_list.remove(text_list[cube-flag])
                flag = flag + 1
# This statement is to remove the empty list, if any present.
            elif text_list[cube-flag] == []:
                text_list.remove(text_list[cube-flag])
                flag = flag + 1
# If the function is empty after all the operations, it has to be equated to 0.
        if text_list == []:
            text_list = [["0"]]
        
        text_list_upd = []
        no_of_cubes = len(text_list)
        flag = 0
        for cube in range(0, no_of_cubes):
            if text_list[cube-flag] not in text_list_upd:
                text_list_upd.append(text_list[cube-flag])
            else:
                continue
            #print(text_list)
# Converting the list into printable format of function        
        upd_no_of_cubes = len(text_list_upd)
        for cube in range(0, upd_no_of_cubes):
            for var in range(0, len(text_list_upd[cube])):
                f = f + text_list_upd[cube][var]
            if cube != upd_no_of_cubes - 1:
                f = f + "+"
    return f

# This definition is to find the Boolean difference and Smoothing function of the function with respect to
# a spliting variable (complemented or non complemented). 
def boolean_diff(var, fnc_loc):
    if var.isupper():                                        
        var_com = var.lower()
    else:
        var_com = var.upper()
    global pos_co_factor
    pos_co_factor = co_factor(var, fnc_loc)
    global neg_co_factor
    neg_co_factor = co_factor(var_com, fnc_loc)
    bool_diff = "(" + pos_co_factor + ")" + "^" + "(" + neg_co_factor + ")"
    return bool_diff

# This definition is to find the Consensus of the function with respect to a spliting variable 
# (complemented or non complemented)
def consensus():
    function_to_csv(pos_co_factor, "pos_fnc.csv")
    function_to_csv(neg_co_factor, "neg_fnc.csv")
    with open("pos_fnc.csv") as file_obj:
        reader_obj = csv.reader(file_obj)
        text_list_pos = list(reader_obj)
        no_of_cubes_pos = len(text_list_pos)

    with open("neg_fnc.csv") as file_obj:
        reader_obj = csv.reader(file_obj)
        text_list_neg = list(reader_obj)
        no_of_cubes_neg = len(text_list_neg)

    bool_cons = []
    if text_list_neg == [['1']]:
        bool_cons = text_list_pos
    elif text_list_pos == [['1']]:
        bool_cons = text_list_neg
    else:
        for cube_pos in range(0, no_of_cubes_pos):
            for cube_neg in range(0, no_of_cubes_neg):
                bool_cons_temp = list(set(text_list_pos[cube_pos]+text_list_neg[cube_neg]))
                if bool_cons_temp not in bool_cons:
                    bool_cons.append(list(set(text_list_pos[cube_pos]+text_list_neg[cube_neg])))
                else:
                    continue

        upd_no_of_cubes = len(bool_cons)
        flag = 0  
        for cube in range(0, upd_no_of_cubes):
            for lit in bool_cons[cube-flag]:
                if lit.isupper():
                    if lit.lower() in bool_cons[cube-flag]:
                        bool_cons.remove(bool_cons[cube-flag])
                        flag = flag + 1
                        break
                    else: continue
                else:
                    if lit.upper() in bool_cons[cube-flag]:
                        bool_cons.remove(bool_cons[cube-flag])
                        flag = flag + 1
                        break
                    else: continue
    if bool_cons == []:
        bool_cons = [["0"]]
    f = ""
    upd_no_of_cubes = len(bool_cons)
    for cube in range(0, upd_no_of_cubes):
        for var in range(0, len(bool_cons[cube])):
            f = f + bool_cons[cube][var]
        if cube != upd_no_of_cubes - 1:
            f = f + "+"
    return f

#This definition is to find the smoothing function. It give the output with no duplicate cubes.
def smooth_fnc():
    function_to_csv(pos_co_factor, "pos_fnc.csv")
    function_to_csv(neg_co_factor, "neg_fnc.csv")
    with open("pos_fnc.csv") as file_obj:
        reader_obj = csv.reader(file_obj)
        text_list_pos = list(reader_obj)
        no_of_cubes_pos = len(text_list_pos)

    with open("neg_fnc.csv") as file_obj:
        reader_obj = csv.reader(file_obj)
        text_list_neg = list(reader_obj)
        no_of_cubes_neg = len(text_list_neg)

    bool_smooth = []
    if text_list_neg == [['1']] or text_list_pos == [['1']]:
        bool_smooth = [['1']]
    elif(no_of_cubes_neg<=no_of_cubes_pos):
        bool_smooth = text_list_pos
        for i in range(0, no_of_cubes_neg):
            if text_list_neg[i] not in text_list_pos:
                bool_smooth.append(text_list_neg[i])
            else:
                continue
    elif(no_of_cubes_neg>no_of_cubes_pos):
        bool_smooth = text_list_neg
        for i in range(0, no_of_cubes_pos):
            if text_list_pos[i] not in text_list_neg:
                bool_smooth.append(text_list_pos[i])
            else:
                continue
    bool_smooth_fnc = ""    
    upd_no_of_cubes = len(bool_smooth)
    for cube in range(0, upd_no_of_cubes):
        for var in range(0, len(bool_smooth[cube])):
            bool_smooth_fnc = bool_smooth_fnc + bool_smooth[cube][var]
        if cube != upd_no_of_cubes - 1:
            bool_smooth_fnc = bool_smooth_fnc + "+"

    return bool_smooth_fnc

print("This program is to generate shanon co-factors of a given Boolean function.")
print("Boolean function is given as a CSV file with rows as cubes and coloumns as literals.")
print("For uncomplemented literal, represent using lower case and for complemented literal, represent using upper case.")
fnc = input("Enter the function: " )
split_var_1 = input("Enter splitting variable/cube: " ) 
csv_file_name = "fnc.csv"
function_to_csv(fnc, csv_file_name)
for i in range(0, len(split_var_1)):
    fnc_split_var = co_factor(split_var_1[i], csv_file_name)
    function_to_csv(fnc_split_var, csv_file_name)
print("f_" + split_var_1 + " = " + fnc_split_var)
split_var_2 = input("Continue with finding Boolean difference, Consensus and Smoothing function. Enter the splitting variable: " )
function_to_csv(fnc, csv_file_name)
fnc_bool_diff = boolean_diff(split_var_2, csv_file_name)
fnc_consensus = consensus()
fnc_smooth = smooth_fnc()
print("Boolean difference of the function with respect to " + split_var_2 + " is: " + fnc_bool_diff)
print("Consensus of the function with respect to " + split_var_2 + " is: " + fnc_consensus)
print("Smoothing function of the function with respect to " + split_var_2 + " is: " + fnc_smooth)  