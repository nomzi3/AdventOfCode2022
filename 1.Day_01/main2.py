calorie_list = [0]
elf_counting = 0
#file_to_check = "test_input.txt"
file_to_check = "input.txt"

with open(file_to_check, "r") as f:
    lines = f.read().splitlines()

    for line in lines:
        if line == "":
            elf_counting += 1
            calorie_list.append(0)
        else:
            calorie_list[elf_counting] += int(line)

print(calorie_list)


max1_pos = 0
max2_pos = 0
max3_pos = 0
max_list = []
for i in range(0,len(calorie_list)):
    if calorie_list[i] >= calorie_list[max1_pos]:
        max3_pos = max2_pos
        max2_pos = max1_pos
        max1_pos = i
    elif calorie_list[i] >= calorie_list[max2_pos]:
        max3_pos = max2_pos
        max2_pos = i
    elif calorie_list[i] >= calorie_list[max3_pos]:
        max3_pos = i

total_calorie = calorie_list[max3_pos] + calorie_list[max2_pos] + calorie_list[max1_pos]
print(total_calorie)   