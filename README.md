# About this Project

This is the first big Python project I have taken unto myself to learn programming.

### Goal of this project:
Creating a Free to use Duplication Scanning application and Learning from the challenges of this project I faced.

### Program description:
This program takes 2 inputs: source_path, and sestination_path. source_path is required and destination_path is optional.
source_path would be an absolute path to where you want scanned example: D:/grand_parent/parent/child. destination_path is (Optional); Defaults to same Directory in a Folder called (Duplicates).
Sudo of sudocode of what program does with inputs:
  check_for_valid(source_path)
  for file in source_path:
    do some checks on file
    hash_the_file(file)
    if not in some_Dictionary.keys():
     continue
    else:
      move file to destination_path

### State of the project:
Complete

### Features
- Searching for Duplicates in a folder excluding Sub-directories
- Undo to move all files back to original Directory
- Cancel during action

### Plans for future
- May add more features later in the future
- Currently would like to create another project and learn more about programming
