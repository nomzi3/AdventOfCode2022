#file_to_check = "test_input1.txt"
#file_to_check = "test_input2.txt"
#file_to_check = "test_input3.txt"
#file_to_check = "test_input4.txt"
#file_to_check = "test_input5.txt"
file_to_check = "input.txt"


#read 4 characters at the time from the list
#send for check - if all unique, return the current

#Check if char is unique within the list
#Returns true if it is, else false
def checkIfCharIsUnique(check_value, lst):
    check = 0
    for item in lst:
        if item == check_value:
            check += 1
    if check == 1:
        return True
    else:
        return False

#Check if marker is found in the list
#Returns False if not found, otherwise True if found
def checkIfMarkerFound(input_list):
    for item in input_list:
        return_bool = checkIfCharIsUnique(item, input_list)
        if return_bool == False:
            return False
    return True




with open(file_to_check, "r") as f:
    lines = f.read().splitlines()

    for line in lines:
        split_list = [x for x in line]

        print(split_list)

        #Check 4 characters at the time - starting from the 4th value

        #if found, print the answer and exit
        for i in range(0,len(split_list)):
            if i > 2:
                #print(split_list[i])
                temp_list = []
                temp_list.append(split_list[i-3])
                temp_list.append(split_list[i-2])
                temp_list.append(split_list[i-1])
                temp_list.append(split_list[i])
                print(temp_list)
                return_bool = checkIfMarkerFound(temp_list)
                if return_bool == True:
                    print("Found it")
                    print("Answer_-->" + str(i+1))
                    break
                else:
                    print("Still trying")
                