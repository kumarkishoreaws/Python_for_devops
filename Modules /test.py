import os
folders = input("Enter folder names: ").split
for folder in folders:
    print(folder)

    files = os.listdir(folder)
    print(files)