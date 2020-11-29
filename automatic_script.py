import os


folder_name = input("what do you want the folder name to be: ")
file_name = input("what do you want the file name to be: ")

os.system("mkdir " + folder_name)

os.system("touch ./" + folder_name + "/" + file_name + ".py")

os.system("nano ./" + folder_name + "/" + file_name + ".py")
