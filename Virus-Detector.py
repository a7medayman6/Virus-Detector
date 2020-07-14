import os
import hashlib

ROOT = "."
FILES = []
DEFECTED_FILES = []
VIRUSESTXT = "viruses.md5"

def crawl():
    for sub, dir, files in os.walk(ROOT):
        for file in files:
            path = sub + os.sep + file
            exe = os.access(path, os.X_OK)
            
            if exe: 
                FILES.append(path)

def read(file_name):
    with open(file_name, 'r') as file:
        try:
            data = file.read()
            return data
        except Exception as ex:
            print("Couldn't read the file.\nERROR: {}".format(ex))
            return ""
    return ""        

def scan():
    crawl()
    for file in FILES:
        hasher = hashlib.md5()
        with open(file, "rb") as binary_file:
            data = binary_file.read()
            hasher.update(data)
            hash = hasher.hexdigest()
            print("file {0} md5: {1}".format(file, hash))
            viruses = read(VIRUSESTXT)
            for virus in viruses:
                if hash == virus.strip():
                    print ("VIRUS DETECTED IN FILE {}".format(file))
                    DEFECTED_FILES.append(file)
                    act(file)
                    break

def delete(path):
    try:
        #os.remove(path)  
        print("the file {} deleted successfully.")                  
    except Exception as ex:
        print("ERROR : {}".format(ex))

def act(path):
    choice = str(input("Do you want to delete this file or not? (y/n)"))
    if choice.upper() == 'Y':
        delete(path)


scan()
