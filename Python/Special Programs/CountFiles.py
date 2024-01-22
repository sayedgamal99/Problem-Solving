import os


def count_files_in_folder(folder_path):
    # Dictionary to store counts of files in each subdirectory
    file_counts = {}

    # Recursive function to count files in a directory and its subdirectories
    def count_files_recursive(directory):
        total_files = 0
        for root, dirs, files in os.walk(directory):
            total_files += len(files)
        return total_files

    # Loop through each subdirectory and count files using the recursive function
    for root, dirs, files in os.walk(folder_path):
        subdirectory = os.path.relpath(root, folder_path)
        file_counts[subdirectory] = count_files_recursive(root)

    return file_counts


def main():
    # Specify the folder path
    folder_path = input("Enter the path of the folder: ")

    # Get file counts in each subdirectory
    file_counts = count_files_in_folder(folder_path)

    # Find the subdirectory with the maximum number of files
    max_subdirectory = max(file_counts, key=file_counts.get)

    # Print results
    print("\nFile counts in each subdirectory:")
    for subdirectory, count in file_counts.items():
        print(f"{subdirectory}: {count} files")

    print("\nThe subdirectory with the maximum number of files is:")
    print(f"{max_subdirectory}: {file_counts[max_subdirectory]} files")


if __name__ == "__main__":
    main()
