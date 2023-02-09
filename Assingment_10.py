

                                  ASSINGMENT - 10



1. How do you distinguish between shutil.copy() and shutil.copytree()?
ANS:-shutil.copy : Copies a single file
     shutil.copytree() : will copy an entire folder and every folder and file contained in it




2. What function is used to rename files??
ANS:-
   import os
   os.rename("text.txt","testnew.txt")




3. What is the difference between the delete functions in the send2trash and shutil modules?
ANS:-
    import shutil
    shutil.retree():
    The shutil module’s rmtree() function can be used to delete files or folders. But, this function delete the files
    permanently. 
    The operations cannot be undone if there were any accidental deletions performed 

    import send2trash
    send2trash.send2trash() : Using send2trash, we can send files to the Trash or Recycle Bin instead of permanently 
    deleting them.
    If the directory contains files or other folders, those are also deleted. A TrashPermissionError exception is raised, 
    in case a file could not be deleted due to permission error or any other unexpected reason.
    import shutil
    import send2trash
    shutil.rmtree("path")
    send2trash.send2trash("path")




4. ZipFile objects have a close() method just like File objects’ close() method. What ZipFile method is equivalent to File objects’ open() method?
ANS:-from zipfile import Zipfile
     with ZipFile(file_name, 'r') as zip: -> this code will open specified zipfile for us. we can use zip objext to preform oother operation the ziplife. like zip.read()
     from zipfile import Zipfile
     with ZipFile(file_name, 'r') as zip.




5. Create a programme that searches a folder tree for files with a certain file extension (such as .pdf or .jpg). Copy these files from whatever location they are in to a new folder.
ANS:- 
# Write a program that walks through a folder tree 
# and searches for files with a certain file extension (such as .pdf or .jpg).
# Copy these files from whatever location they are in to a new folder.

import os, shutil

def selectiveCopy(source, extensions, destFolder):
    folder = os.path.abspath(source)
    destFolder = os.path.abspath(destFolder)
    print('Looking in', source, 'for files with extensions of', ', '.join(extensions))
    for foldername, subfolders, filenames in os.walk(source):
        for filename in filenames:
            name, extension = os.path.splitext(filename)
            if extension in extensions:
                fileAbsPath = foldername + os.path.sep + filename
                print('Coping', fileAbsPath, 'to', destFolder)
                shutil.copy(fileAbsPath, destFolder)

extensions = ['.mp4', '.pdf','.jpg']
source = "C:\\Users\\bhanu\\Desktop\\source"
destFolder = "C:\\Users\\bhanu\\Desktop\\dest"
selectiveCopy(source, extensions, destFolder)
