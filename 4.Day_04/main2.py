#file_to_check = "test_input.txt"
file_to_check = "input.txt"

#Function checks if elf1's work-schedule is contained within elf2's at all
#Returns True if it does
#Returns False if else.
def checkIfWorkIsOverlapping(elf1_input, elf2_input):
    
    print("Checking elf1 in elf2")
    for x in elf1_input:
        if x in elf2_input:
            print(str(x) + " Exists in ")
            print(elf2_input)
            
            return True
    print("€€€€€€€€€€€€")
    print("Checking elf2 in elf1")
    for y in elf2_input:
        if y in elf1_input:
            print(str(y) + " Exists in ")
            print(elf1_input)
            return True
            
    print("€€€€€€€€€€€€€")
    return False
section_list = []


total_overlapping = 0
with open(file_to_check, "r") as f:
    lines = f.read().splitlines()

    for line in lines:
        #split and sort into ranges
        split_instructions = line.split(",")
        print(split_instructions)
        elf1 = split_instructions[0].split("-")
        elf2 = split_instructions[1].split("-")
        elf1_range = []
        elf2_range = []
        for x in range(int(elf1[0]), int(elf1[1])+1):
            elf1_range.append(x)
        for y in range(int(elf2[0]), int(elf2[1])+1):
            elf2_range.append(y)
        print(elf1_range)
        print(elf2_range)
        #for each elf's section, check if any part of it overlaps with eachother.
        print("###################")
        isOverlapping = checkIfWorkIsOverlapping(elf1_range, elf2_range)
        if isOverlapping:
            total_overlapping += 1
        print("&&&&&&&&&&&&&&&&&&&")

print("Done calculating input")
print("Total overlapping:->" + str(total_overlapping))
