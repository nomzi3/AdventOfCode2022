#file_to_check = "test_input.txt"
file_to_check = "input.txt"
score_dict = {
    "X" : 1,
    "Y" : 2,
    "Z" : 3
    }

def calculate_outcome(list):
    if (list[0] == "A" and list[1] == "X") or (list[0] == "B" and list[1] == "Y") or (list[0] == "C" and list[1] == "Z"):
        return 3
    elif (list[0] == "A" and list[1] == "Y") or (list[0] == "B" and list[1] == "Z") or (list[0] == "C" and list[1] == "X"):
        return 6
    elif (list[0] == "A" and list[1] == "Z") or (list[0] == "B" and list[1] == "X") or (list[0] == "C" and list[1] == "Y"):
        return 0
    
round_list = []
total_score = 0
with open(file_to_check, "r") as f:
    lines = f.read().splitlines()
    i = 0

    for line in lines:
        split_list = line.split(" ")

        round_score = calculate_outcome(split_list) + score_dict[split_list[1]]
        round_list.append(int(round_score))


print(round_list)
print(sum(round_list))



