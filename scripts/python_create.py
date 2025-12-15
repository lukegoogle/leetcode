import os

def create_python_files(start_num, end_num, directory):
    if start_num > end_num:
        print("Error: The starting number must be less than or equal to the ending number.")
        return

    print(f"Starting to create files from ../{directory}/{start_num}.py to {end_num}.py...")
    
    for i in range(start_num, end_num + 1):
        filename = f"../{directory}/{i}.py"
        content = ""

        if not os.path.exists(filename):
            try:
                with open(filename, 'w') as f:
                    f.write(content + "\n")
            except IOError as e:
                print(f"An error occurred while creating {filename}: {e}")
        else:
            print(f"File ../{directory}/{i}.py exists!")

    print("File creation complete!")

# Create the files.
create_python_files(51, 1000, "python1_mod/part1")
create_python_files(1001, 2000, "python1_mod/part2")
create_python_files(2001, 3000, "python1_mod/part3")
create_python_files(3001, 3778, "python1_mod/part4")