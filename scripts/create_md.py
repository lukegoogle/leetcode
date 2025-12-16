import os

def create_python_files(start,end,part) -> None:
    print(f"Attempting to create 1000 empty .md files in {os.getcwd()}...")

    for i in range(start, end + 1):
        filename = f"../python/{part}/docs/{i}.md"
        
        if not os.path.exists(filename):
            try:
                with open(filename, 'w') as f:
                    pass
            except IOError as e:
                print(f"Error creating file {filename}: {e}")
                continue
        else:
            print("File exists {filename}!")

    print("File creation process finished.")
    print(f"Check your current directory for the new files (e.g., file_0001.py, file_1000.py).")

# --- Execution ---
create_python_files(1,1000,"part1")
create_python_files(1001,2000,"part2")
create_python_files(2001,3000,"part3")
create_python_files(3001,3778,"part4")