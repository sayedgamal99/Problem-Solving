import os
import zipfile


def extract_zip_files(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".zip"):
                file_path = os.path.join(root, file)
                with zipfile.ZipFile(file_path, 'r') as zip_ref:
                    zip_ref.extractall(root)
                print(f"Extracted {file} in {root}")
                os.remove(file_path)
                print(f"{file_path =} Deleted")


def main():
    # Replace with your target path
    target_path = "E:\99\engineering\CCSE FIFTH SEMISTER\databases"
    extract_zip_files(target_path)


if __name__ == "__main__":
    main()
