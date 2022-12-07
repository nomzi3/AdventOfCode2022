#file_to_check = "test_input.txt"
file_to_check = "input.txt"

def checkIfWorkIsOverlapping(elf1_input, elf2_input):
    nr_of_elf1_in_elf2 = 0
    nr_of_elf2_in_elf1 = 0
    print("Checking elf1 in elf2")
    for x in elf1_input:
        if x in elf2_input:
            print(str(x) + " Exists in ")
            print(elf2_input)
            nr_of_elf1_in_elf2 += 1
    print("€€€€€€€€€€€€")
    print("Checking elf2 in elf1")
    for y in elf2_input:
        if y in elf1_input:
            print(str(y) + " Exists in ")
            print(elf1_input)
            nr_of_elf2_in_elf1 += 1
    print("€€€€€€€€€€€€€")

    print("Summary")
    print("nr of elf1 in elf2->" + str(nr_of_elf1_in_elf2))
    print("nr of elf2 in elf1->" + str(nr_of_elf2_in_elf1))

    print("Length of elf1->" + str(len(elf1_input)))
    print("Lenght of elf2->" + str(len(elf2_input)))

    if(len(elf1_input) == nr_of_elf1_in_elf2):
        print("elf1 fully contained in elf2")
        return True
    elif(len(elf2_input) == nr_of_elf2_in_elf1):
        print("elf2 fully contained in elf1")
        return True
    else:
        return False
section_list = []


total_overlapping = 0
with open(file_to_check, "r") as f:
    lines = f.read().splitlines()

    for line in lines:
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

        print("###################")
        isOverlapping = checkIfWorkIsOverlapping(elf1_range, elf2_range)
        if isOverlapping:
            total_overlapping += 1
        print("&&&&&&&&&&&&&&&&&&&")

print("Done calculating input")
print("Total overlapping:->" + str(total_overlapping))
