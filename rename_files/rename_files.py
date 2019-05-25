import os    
def rename_files():
    file_list = os.listdir(r"D:\Learn\Python programs\udacity\alphabet")
    """r is row path and it tells python "hi.. take this string as it is and do not interpretet any other way" """ 
    print(file_list)
    saved_path = os.getcwd() # os.getcwd() give current working directory
    print("current working directory "+saved_path)
    os.chdir(r"D:\Learn\Python programs\udacity\alphabet")

    for file_name in file_list:
        print("old name -"+file_name)
        print("new name -"+file_name.translate(None,"0123456789"))
        os.rename(file_name,file_name.translate(None,"0123456789"))
rename_files()
