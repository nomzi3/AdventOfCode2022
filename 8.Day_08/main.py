file_to_check = "test_input.txt"


grid = []

with open(file_to_check, "r") as f:
    lines = f.read().splitlines()

    for line in lines:
        print(line)
        split_line = [x for x in line]
        print(split_line)
        grid.append(split_line)


#Grid [][]
print(grid)
y = 0
x = 0
for y in range(len(grid)):
    for x in range(len(grid[y])):
        print("y: " + str(y) + " x: " + str(x) + " " + grid[y][x])
        i = x
        j = y
        left_list = []
        right_list = []
        up_list = []
        down_list = []
        while i > 0:
            i -= 1
            left_list.append(grid[j][i])
            #print("Comparing: " + str(grid[y][x]) + " with: " + str(grid[j][i]))
            #if grid[y][x] > grid[j][i]:
            #   print("found a higher tree: " + "y: " + str(j) + " x: " + str(i))
        #print("sub_left_list: ")
        #print(left_list)
        
        i = x
        print("value of x:" + str(x))
        print("lenght: " + str(len(grid[y])))
        while i < len(grid[y]):
            
            print(i)
            #print(grid[j][i])
            right_list.append(grid[j][i])
            i += 1
        print("sub_right_list")
        print(right_list)


"""
for y in grid:
    for x in y:
        print("x: " + x + " y: " + y)

"""