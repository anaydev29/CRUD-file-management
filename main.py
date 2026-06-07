from pathlib import Path
import os 


def createfile():
    try:
        name = input("tell your file name:-")
        path = Path(name)
        if not path.exists():
            with open(path,"w") as fs:
                data = input("what you wan to write:-")
                fs.write(data)
            print("file created successfully")  
        else:
            print("Error file name already exist")      
    except Exception as err:
        print(f"an error occoured {err}")
    

def readfile():
    try:
        name = input("tell your file name:-")
        path = Path(name)
        if path.exists():
            with open(path,"r") as fs:
                content = fs.read()
                print(f"your file content is \n {content}")
        else:
            print("no such file exists")
    except Exception as err:
        print(f"an error occured as {err}")


def updatefile():
    try:
        name = input("enter your file name:-")
        path = Path(name)
        if path.exists():
            print("operations ")
            print("1. Renaming the file ")
            print("2. Appending the content")
            print("3. overwriting the file")

            choice = int(input("enter your options:-"))
            if choice == 1:
                newname = input("enter new name:-")
                new_path = Path(newname)
                if not new_path.exists():
                    path.rename(new_path)
                    print("file renamed successfullly")
                else:
                    print("file already  exists")    

            elif choice == 2:        
                with open(path,"a") as fs:
                    data = input("write the data here :-")
                    fs.write("\n " + data)
                    print("file updated successfully")

            elif choice == 3:
                with open(path,"w") as fs:
                        data = input("write the data here :-")
                        fs.write("\n " + data)
                        print("file overwritten successfully")     
  
    except Exception as err:
        print(f"an error occured as {err}")             


def deletefile():
    try:
        name = input("tell your file name :-")
        path = Path(name)
        if path.exists():
            path.unlink()
            print("file deleted successfully")
        else:
            print("error no such file exists")    
    except Exception as err:
        print(f"An error occured as {err}")



print("press 1 for creating a file")
print("press 2 for reading a file")
print("press 3 for updating a file")
print("press 4 for deleting a file")


a = int(input("\n tell your response:-"))


if a == 1:
    createfile()
if a == 1:
    readfile()
if a == 1:
    updatefile()
if a == 1:
    deletefile()            