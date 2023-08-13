import os
import sys
import shutil
filetypes = {".txt":"Text", 
             ".docx":"Word", 
             ".xlsx":"Excel",".csv":"Excel", 
             ".py":"Code", ".ipynb":"Code",".html":"Code", ".cpp":"Code",
             ".pdf":"PDF's", 
             ".png":"Pictures",".jpg":"Pictures",".gif":"Pictures",
             ".mp3":"Audio",
             ".mp4":"Videos",
             ".zip":"Zip",
             ".exe":"Executabels", ".sh":"Executabels"
             }

def main():
    filepath = check_input_and_get_all_files()
    print("Folderpath is valid")
    move_files_and_create_when_needed_folder(filepath)
    

def check_input_and_get_all_files():
    # check if filepath is valid
    if len(sys.argv) == 1:
        print("enter a filepath")
        raise FileNotFoundError
    try:
        return sys.argv[1]
    except:
        print("enter valid filepath")
        raise FileNotFoundError

def move_files_and_create_when_needed_folder(filepath):
    files = os.listdir(filepath)
    for file in files:
        name, extension = os.path.splitext(file)
        if file == "desktop.ini": continue
        if not os.path.isfile(os.path.join(filepath, file)): continue

        if extension in filetypes.keys():
            if not check_folder(filetypes[extension], filepath):
                os.makedirs(os.path.join(filepath, filetypes[extension]))
                print(f"created new folder: {filetypes[extension]}")
            else: standardize_folders(filepath,filetypes[extension])
            shutil.move(os.path.join(filepath,file),
                        os.path.join(filepath,filetypes[extension],file))
            print(f"moved {file} to {filetypes[extension]}")
            
        else:
            if not check_folder("Remnants", filepath):
                os.makedirs(os.path.join(filepath, "Remnants"))
                print("created new folder: Remnants")
            else: standardize_folders(filepath,"Remnants")
            shutil.move(os.path.join(filepath,file),
                        os.path.join(filepath,"Remnants",file))
            print(f"moved {file} to Remnants")




def check_folder(folder,filepath):
    for item in os.listdir(filepath):
        if item == folder: return True
        elif "_" in item and item[:item.index("_")] == folder: return True
    return False

def standardize_folders(filepath,extension):
    for item in os.listdir(filepath):
        if "_" in item and item[:item.index("_")] == extension: 
            os.rename(os.path.join(filepath,item),
                      os.path.join(filepath,extension))

main()