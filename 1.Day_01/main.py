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
print(max(calorie_list))