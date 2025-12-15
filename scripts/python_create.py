import os

def create_python_files(start_num, end_num, directory, content=None):
    if start_num > end_num:
        print("Error: The starting number must be less than or equal to the ending number.")
        return
    
    if content == None:
        content = ""

    print(f"Starting to create files from ../{directory}/_{start_num}.py to _{end_num}.py...")
    
    for i in range(start_num, end_num + 1):
        filename = f"../{directory}/_{i}.py"

        if not os.path.exists(filename):
            try:
                with open(filename, 'w') as f:
                    f.write(content + "\n")
            except IOError as e:
                print(f"An error occurred while creating {filename}: {e}")
        else:
            print(f"File ../{directory}/{i}.py exists!")

    print("File creation complete!")

# Create the python files/modules.
create_python_files(51, 500, "python1_mod/part1")
#create_python_files(1001, 2000, "python1_mod/part2")
#create_python_files(2001, 3000, "python1_mod/part3")
#create_python_files(3001, 3778, "python1_mod/part4")

create_python_files(51, 500, "python1_run/part1")
#create_python_files(1001, 2000, "python1_run/part2")
#create_python_files(2001, 3000, "python1_run/part3")
#create_python_files(3001, 3778, "python1_run/part4")

content = "class Solution:\n\
   pass"
create_python_files(51, 500, "python1/part1", content)
#create_python_files(1001, 2000, "python1/part2", content)
#create_python_files(2001, 3000, "python1/part3", content)
#create_python_files(3001, 3778, "python1/part4", content)