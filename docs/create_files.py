import os

def create_markdown_files(start_num, end_num):
    if start_num > end_num:
        print("Error: The start number must be less than or equal to the end number.")
        return

    print(f"Starting to create files from {start_num}.md to {end_num}.md...")

    for i in range(start_num, end_num + 1):
        filename = f"{i}.md"
        try:
            with open(filename, 'w') as f:
                f.write(f"# File {i}\n\nThis is the content for {filename}.")
            pass
        except IOError as e:
            print(f"Error creating file {filename}: {e}")
            break

    print("---")
    print(f"✅ Finished! Created {end_num - start_num + 1} files.")
    print("Files were created in the current working directory.")

START_NUMBER = 51
END_NUMBER = 300

create_markdown_files(START_NUMBER, END_NUMBER)