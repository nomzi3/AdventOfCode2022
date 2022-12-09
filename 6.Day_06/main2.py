#file_to_check = "test_input1.txt"
#file_to_check = "test_input2.txt"
#file_to_check = "test_input3.txt"
#file_to_check = "test_input4.txt"
#file_to_check = "test_input5.txt"
file_to_check = "input.txt"

#Look for start of message
#Shows up after 14 distinct unique chars

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

        #Check 14 characters at the time - starting from the 14th value

        #if found, print the answer and exit
        for i in range(0,len(split_list)):
            
            if i > 12:
                temp_list = []
                x = 13
                while x > -1:
                    temp_list.append(split_list[i-x])
                    x -= 1
                return_bool = checkIfMarkerFound(temp_list)
                if return_bool == True:
                    print("Found the message marker")
                    print("Answer--->" + str(i+1))
                    break
                else:
                    print("Still trying")
                