file_to_check = "test_input.txt"
import re

#folder_structure = {
 #   }
folder_list = []

class Folder:
    def __init__(self, name, absolute_path) -> None:
        self.name = name
        self.absolute_path = absolute_path
        
        
    folderContent = {}
    def return_name(self):
        return self.name
    def return_absolutePath(self):
        #print(self.ab_path)
        return self.absolute_path
    def addFolderContent(self,itemToAdd):
        self.folderContent[itemToAdd[0]] = itemToAdd[1]
    
    
with open(file_to_check, "r") as f:
    lines = f.read().splitlines()

    check_if_command_line = "^\$"
    current_path = []
    for line in lines:
        
        print(line)
        result = re.match(check_if_command_line, line)
        split_line = line.split(" ")
        if result:
            #print("Command line")
            
            if split_line[1] == "cd":
                print("--->cd")
                if split_line[2] == "..":
                    print("Up one level")
                    current_path.pop()
                else:
                    print("Going down")
                    current_path.append(split_line[2])
                print("Current path")
                print(current_path)
            #elif split_line[1] == "ls":
            #   print("---->ls")
        else:
            if split_line[0] == "dir":
                print("Adding dir to dict")
                print("name: " + split_line[1])
                print("current path ")
                print(current_path)
                newFolder = Folder(split_line[1],current_path)
                folder_list.append(newFolder)
            else:
                print("Adding file to dict")
                
                
print("Done processing - current folder structure")       
for item in folder_list:
    print(item.return_name())
    #why is this returning nothing of what we set it to?
    print(item.return_absolutePath())