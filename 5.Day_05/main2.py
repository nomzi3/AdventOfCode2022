#file_to_check = "test_input.txt"
file_to_check = "input.txt"
import re

#This is the second most stupid way of doing it
#updated to handle the new way of moving crates given in part2
#Starting crates are still hardcoded.

#Test data - used for test_input.txt
"""
Test Data
    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 
"""

#Prod data - used for input.txt
"""
Prod Data
        [M]     [B]             [N]
[T]     [H]     [V] [Q]         [H]
[Q]     [N]     [H] [W] [T]     [Q]
[V]     [P] [F] [Q] [P] [C]     [R]
[C]     [D] [T] [N] [N] [L] [S] [J]
[D] [V] [W] [R] [M] [G] [R] [N] [D]
[S] [F] [Q] [Q] [F] [F] [F] [Z] [S]
[N] [M] [F] [D] [R] [C] [W] [T] [M]
 1   2   3   4   5   6   7   8   9 

"""

#Function used in part1 for moving containers - one at the time
#Returns - two lists, one showing the new from_stack
#the other showing the new to_stack
def moveContainers(move_amount, move_from_stack, move_to_stack):
    from_stack = move_from_stack
    to_stack = move_to_stack
    for i in range(move_amount):
        popped_container = from_stack.pop()
        print("Popped->" + popped_container)
        to_stack.append(popped_container)
        print("Added to move stack->" + popped_container)
    return from_stack, to_stack

#New function for part2 - moves crates for cratemover9001
#Updated functionality - all containers moved in the session
#is moved onto the new pile in the same order as previous stack
def moveContainersCratemove9001(move_amount,move_from_stack,move_to_stack):
    from_stack = move_from_stack
    to_stack = move_to_stack
    temp_stack = []
    for i in range(move_amount):
        popped_container = from_stack.pop()
        print("Popped->" + popped_container)
        temp_stack.append(popped_container)
    for x in range(0, len(temp_stack)):
        move_again = temp_stack.pop()
        to_stack.append(move_again)
    return from_stack, to_stack
    
with open(file_to_check, "r") as f:
    lines = f.read().splitlines()
    check_if_move_line = '^move'
    
    #change here to set to test data
    """
    stacks = {
        "1" : ["Z", "N"],
        "2" : ["M", "C", "D"],
        "3" : ["P"]
    }
    """
    #Change here to set to prod data
    stacks = {
        "1" : ["N", "S", "D", "C", "V", "Q", "T"],
        "2" : ["M", "F", "V"],
        "3" : ["F", "Q", "W", "D", "P", "N", "H", "M"],
        "4" : ["D", "Q", "R", "T", "F"],
        "5" : ["R", "F", "M", "N", "Q", "H", "V", "B"],
        "6" : ["C", "F", "G", "N", "P", "W", "Q"],
        "7" : ["W", "F", "R", "L", "C", "T"],
        "8" : ["T", "Z", "N", "S"],
        "9" : ["M", "S", "D", "J", "R", "Q", "H", "N"]
    }
    
    for line in lines:
        
        result = re.match(check_if_move_line, line)
        
        if result:
            print(line)

            #split into working pieces
            split_line = line.split(" ")
            
            #call the function with the input - how many to move, and to where
            move_from_pile, move_to_pile = moveContainersCratemove9001(int(split_line[1]),stacks[split_line[3]],stacks[split_line[5]])
            
            stacks[split_line[3]] = move_from_pile
            stacks[split_line[5]] = move_to_pile
    

    print("################################")
    
    #print the output as requested - change here to get output based on if your running for prod or test
    print("answer to the question")
    final_output = stacks["1"][-1] + stacks["2"][-1] + stacks["3"][-1] + stacks["4"][-1] + stacks["5"][-1] + stacks["6"][-1] + stacks["7"][-1] + stacks["8"][-1] + stacks["9"][-1]
    #final_output = stacks["1"][-1] + stacks["2"][-1] + stacks["3"][-1]
    print(final_output)

