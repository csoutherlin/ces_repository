import os
import shutil

def main():
    # Introduction
    print("Welcome to the File Organizer!")
    print("This program will organize files in a directory based on their extensions.")

    # Get user input for the directory path
    directory_path = input("Enter the path to the directory you want to organize: ")

    # Validate the directory path
    if not os.path.isdir(directory_path):
        print("Error: Invalid directory path. Please provide a valid directory.")
        return

    # Mapping extensions to folder names
    mapping = {
        '.pdf': 'PDFs',
        '.jpg': 'Images',
        '.png': 'Images',
        # Add more mappings as needed
    }

    # Process the directory
    organize_files(directory_path, mapping)

    # Completion message
    print("File organization complete!")

def organize_files(directory_path, mapping):
    for filename in os.listdir(directory_path):
        file_path = os.path.join(directory_path, filename)
        if os.path.isfile(file_path):
            # Get the file extension
            _, extension = os.path.splitext(filename)
            extension = extension.lower()  # Normalize to lowercase

            # Check if extension exists in the mapping
            if extension in mapping:
                folder_name = mapping[extension]
                folder_path = os.path.join(directory_path, folder_name)

                # Create the folder if it doesn't exist
                if not os.path.exists(folder_path):
                    os.mkdir(folder_path)

                # Move the file to the corresponding folder
                new_file_path = os.path.join(folder_path, filename)
                shutil.move(file_path, new_file_path)
                print(f"Moved '{filename}' to '{folder_name}' folder.")

if __name__ == "__main__":
    main()
