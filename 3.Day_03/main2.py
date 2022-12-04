#file_to_check = "test_input.txt"
file_to_check = "input.txt"
def findBadgeOfGroup(list):
    print(list)
    list1 = [x for x in list[0]]
    list2 = [x for x in list[1]]
    list3 = [x for x in list[2]]

    for item in list1:
        if item in list2 and item in list3:
            return item
    return 0    

with open(file_to_check, "r") as f:
    lines = f.read().splitlines()

    i = 1
    group_list = []
    badge_list = []
    totalValue = 0
    for line in lines:
        group_list.append(line)
        if len(group_list) == 3:
            badge_item = findBadgeOfGroup(group_list)
            group_list = []
            if badge_item != 0:
                print(badge_item)
                badge_list.append(badge_item)
                priorityOfItem = ord(badge_item)
                if priorityOfItem >= 97:
                    priorityOfItem -= 96
                else:
                    priorityOfItem -= 38
                totalValue += priorityOfItem
                print("Value of badge " + str(priorityOfItem))
"""
with open(file_to_check, "r") as f:
    lines = f.read().splitlines()

    i = 1
    group_list = []
    badge_list = []
    totalValue = 0
    for line in lines:
        
        if i <= 3:
            group_list.append(line)
            i += 1
            print(group_list)
            if i == 4:
                badge_item = findBadgeOfGroup(group_list)
                group_list = []
                #group_list.append(line)
                #print(group_list)
                if badge_item != 0:
                    print(badge_item)
                    badge_list.append(badge_item)
                    priorityOfItem = ord(badge_item)
                    if priorityOfItem >= 97:
                        priorityOfItem -= 96
                    else:
                        priorityOfItem -= 38
                    totalValue += priorityOfItem
                    print("Value of badge " + str(priorityOfItem))
        else:
            i = 1
            

print(totalValue)
"""
print("Total Value: " + str(totalValue))


