#file_to_check = "test_input.txt"
file_to_check = "input.txt"
def findContainedItems(list):
    split_list = [x for x in list]
    #print(split_list)
    half_of_list = len(list) // 2
    
    part1 = split_list[:half_of_list]
    part2 = split_list[half_of_list:]

    #print(part1)
    #print(part2)

    for item in part1:
        if item in part2:
            return item
    return 0

totalValue = 0
with open(file_to_check, "r") as f:
    lines = f.read().splitlines()

    for line in lines:
        print(line)
        contained_in_both = findContainedItems(line)
        
        if contained_in_both != 0:
            priorityOfItem = ord(contained_in_both)
            #what is the value
            print(contained_in_both)
            #print("Value: " + str(ord(contained_in_both)))
            if priorityOfItem >= 97:
                priorityOfItem -= 96
            else:
                priorityOfItem -= 38
            totalValue += priorityOfItem
            print("Value of letter " + str(priorityOfItem))


print(totalValue)