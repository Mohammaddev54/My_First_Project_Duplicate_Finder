# About This Project

This is the first big Python project I have taken unto myself to learn programming.

## Goal Of This Project:
Creating a Free to use file duplicate detection application and finding a job

### Program description:
```python
"""
File_duplication_scanner is my first big project that I have worked on. I need
    all the feedback that I can get from it so I can improve upon my work and
    also become a better programmer.

Program terminology:
Destination = The directory to which all the duplicate files will be moved to.
Source = Directory user wants to scan.
Path = Absolute path.
Hashing = Mathematical formula that changes data to a string of nonsensical
    jumbled characters that differ in length according to which algorithm or
    function is used in the program.
Validate = Checking if it is valid.

How Program functions:

1 - [Obligatory] Takes source path and validates it.
2 - [Optional] Takes destination path and validates it.
3 - If the [Optional] destination path is not valid, creates a directory inside
    the source path called [Duplicates] and sets the destination path to it.
4 - Reads file data one by one in binary; hashes it and then stores it.
5 - Repeats and checks if the file that it read already exists in its memory;
    if not, stores it.
6 - If hashed file data exists in its memory, it moves that file to the
    destination.
"""
```

## State Of Project:
On Going

### Features
- Searching for Duplicates in a folder excluding Sub-directories
- Undo to move all files back to original Directory
- Cancel during action
- Menubar
- Showing Processed File names

### Plans for future:
- Adding more as I learn
- 
