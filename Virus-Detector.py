import os
import hashlib

ROOT = "."
FILES = []
DEFECTED = []
VIRUSESTXT = "viruses.md5"

def crawl():
    for sub, dir, files in os.walk(ROOT):
        for file in files:
            path = sub + os.sep + file
            exe = os.access(path, os.X_OK)
            
            if exe: 
                FILES.append(path)
       

def scan():
    crawl()
    for file in FILES:
        viruses = open(VIRUSESTXT, 'r')
        hasher = hashlib.md5()
        with open(file, "rb") as binary_file:
            data = binary_file.read()
            hasher.update(data)
            hash = hasher.hexdigest()
            print("file {0} md5: {1}".format(file, hash))
            
            for virus in viruses:
                if hash == virus.strip():
                    print ("VIRUS DETECTED IN FILE {}".format(file))
                    DEFECTED.append(file)
                    act(file)
                    break

def delete(path):
    try:
        os.remove(path)  
        print("the file {} deleted successfully.".format(path.split('/')[-1]))                  
    except Exception as ex:
        print("ERROR : {}".format(ex))

def act(path):
    
    choice = ''
    while 1:
        choice = str(input("Do you want to delete this file or not? (y/n):\t"))
        if choice.upper().strip() == 'Y':
            delete(path)
            
        elif choice.upper().strip() != 'N':
            print("Wrong Choice.")

        if choice.upper().strip() == 'Y' or choice.upper().strip() == 'N':
            break        
        print(choice.upper())        

def exists(dir):
    if os.path.isdir(dir.strip()):
        return True
    return False
def get_root():
    directory = str(input("Enter the directory absolute path:\t"))             
    while not exists(directory):
        print("Sorry, wrong path.")
        directory = str(input("Enter the directory absolute path:\t"))
    return directory    

ROOT = get_root()    
scan()
print("\n\nYour directory had {} defected files.".format(len(DEFECTED)))