#file_to_check = "test_input.txt"
file_to_check = "input.txt"
score_dict = {
    "R" : 1,
    "P" : 2,
    "S" : 3
    }

def calculate_outcome(list):
    if (list[0] == "A" and list[1] == "R") or (list[0] == "B" and list[1] == "P") or (list[0] == "C" and list[1] == "S"):
        return 3
    elif (list[0] == "A" and list[1] == "P") or (list[0] == "B" and list[1] == "S") or (list[0] == "C" and list[1] == "R"):
        return 6
    elif (list[0] == "A" and list[1] == "S") or (list[0] == "B" and list[1] == "R") or (list[0] == "C" and list[1] == "P"):
        return 0

def set_our_pick(list):
    A_list = {
        "X" : "S",
        "Y" : "R",
        "Z" : "P"
    }
    B_list = {
        "X" : "R",
        "Y" : "P",
        "Z" : "S"
    }
    C_list = {
        "X" : "P",
        "Y" : "S",
        "Z" : "R"
    }

    if list[0] == "A":
        return A_list[list[1]]
    elif list[0] == "B":
        return B_list[list[1]]
    elif list[0] == "C":
        return C_list[list[1]]

round_list = []
total_score = 0
with open(file_to_check, "r") as f:
    lines = f.read().splitlines()
    i = 0

    for line in lines:
        split_list = line.split(" ")
        split_list[1] = set_our_pick(split_list)
        print(split_list)
        round_score = int(calculate_outcome(split_list)) + int(score_dict[split_list[1]])
        round_list.append(int(round_score))


print(round_list)
print(sum(round_list))



