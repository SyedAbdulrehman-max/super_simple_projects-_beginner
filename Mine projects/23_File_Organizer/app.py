# File Organizer	Organize files by type in folders	OS module, file handling
import os   # Import the os module

# Ask the user to enter the folder path
folder_path = input("Enter the folder path: ")

# List all files and folders inside the given path
items = os.listdir(folder_path)

# Print each item one by one
print(f"\nFiles and folders inside {folder_path} :")
for item in items:
    print(item)
