import os
import shutil
path=input("Enter the name of directory to be shorted")
listoffiles=os.listdir(path)
for files in listoffiles:
	name,ext=os.path.splitext(files)
	ext=ext[1:]
	if ext == '':
		continue
	if os.path.exists(path + '/' + ext):
		shutil.move(path +'/' + files, path+'/' + ext + '/' + files)
	else:
		os.makedirs(path + '/' + ext)
		shutil.move(path +'/' + files, path+'/' + ext + '/' + files)
