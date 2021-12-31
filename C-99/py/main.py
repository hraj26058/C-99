import os
import shutil
source=input("Enter source folder name")
dest=input("Enter destination folder name")
source=source+ "/"
dest=dest+ "/"
listoffiles=os.listdir(source)
for files in listoffiles:
	shutil.move((source+files),dest)
