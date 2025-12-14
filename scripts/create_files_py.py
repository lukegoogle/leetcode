import os

def create_python_files(start_num, end_num):
    if start_num > end_num:
        print("Error: The start number must be less than or equal to the end number.")
        return

    print(f"Starting to create files from {start_num}.md to {end_num}.md...")

    for i in range(start_num, end_num + 1):
        filename = f"../python/{i}.py"
        if not os.path.exists(filename):
            try:
                with open(filename, 'w') as f:
                    f.write(f"")
                pass
            except IOError as e:
                print(f"Error creating file {filename}: {e}")
                break
        else:
            print(f"File {i}.py exists!")

    print("---")
    print(f"✅ Finished! Created {end_num - start_num + 1} files.")
    print("Files were created in the current working directory.")

START_NUMBER = 1
END_NUMBER = 100 #1000 #3772

create_python_files(START_NUMBER, END_NUMBER)