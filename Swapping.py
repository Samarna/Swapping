import os
import shutil

source = input("Enter file 1 : ")
destination = input("Enter file 2 : ")
source = source+'/'
destination = destination+'/'

listOfFiles = os.listdir(source)
for file in listOfFiles:
    shutil.copy(source+file,destination)