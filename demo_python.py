import os
folders = input("Enter folder names: ").split()

for folder in folders:
    try:
     files = os.listdir(folder)
     print("Files in folder :", folder)
     for file in files:
      print("  -" + file)
    
    except FileNotFoundError:
     print("Folder not found: " , folder )