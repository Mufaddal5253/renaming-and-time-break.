import os
def rename_files():
    # 1. file name from folder
    file_list = os.listdir(r"prank pics")
    #print(file_list)
    saved_path = os.getcwd()
    print("Current Working Directory is "+saved_path)
    os.chdir(r"prank pics")
    # 2. for each file rename file name
    for file_name in file_list:
        os.rename(file_name, file_name.strip('0123456789'))
    os.chdir(saved_path)
rename_files()
