import os

def create_md_files(start_num, end_num, directory):
    if start_num > end_num:
        print("Error: The starting number must be less than or equal to the ending number.")
        return

    print(f"Starting to create files from ../{directory}/{start_num}.md to {end_num}.md...")
    
    for i in range(start_num, end_num + 1):
        filename = f"../{directory}/{i}.md"
        content = '## Pyodide\n\
\n\
```pyodide height="10"\n\
# Type here\n\
\n\
\n\
```\n\
\n\
## Run\n\
\n\
```pyodide\n\
{% \n\
    include "../python_run/_'+f"{i}"+'.py" \n\
    preserve-includer-indent=false \n\
%}\n\
```\n\
\n\
## Solution\n\
\n\
```python\n\
{% \n\
    include "../python_mod/_'+f"{i}"+'.py" \n\
    preserve-includer-indent=false \n\
%}\n\
```\n\
\n\
<a target="__blank" href="https://leetcode.com/problems/powx-n/"><input class="verify-button" type="button" value="Verify"/></a>\n\
\n\
## Function Description\n\
\n\
::: _'+f"{i}"+'.Solution\n\
    handler: python\n\
    options:\n\
        #show_root_heading: true\n\
        members: true\n\
\n\
## Explanation'

        if not os.path.exists(filename):
            try:
                with open(filename, 'w') as f:
                    f.write(content + "\n")
            except IOError as e:
                print(f"An error occurred while creating {filename}: {e}")
        else:
            print(f"File {i}.md exists!")

    print("File creation complete!")

# Create the files.
create_md_files(51, 1000, "docs/part1")
create_md_files(1001, 2000, "docs/part2")
create_md_files(2001, 3000, "docs/part3")
create_md_files(3001, 3778, "docs/part4")