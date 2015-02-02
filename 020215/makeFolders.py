# -*- coding: utf-8 -*-
"""
Created on Mon Feb  2 10:51:37 2015

@author: Sagar
"""

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
mpl.style.available
mpl.style.use('ggplot')

#import os
#os.system('makedir test')

import subprocess
#subprocess.call(["ls", "-l"])
#subprocess.call(["mkdir", "test"])
#subprocess.call(["touch","myfile.txt"]) 

path = subprocess.Popen("pwd", stdout=subprocess.PIPE, shell=True)
(output, err) = path.communicate()

## Files and folders that should be copied over can be speciefied here
FILES = [output[0:-1]+'/myfile.txt', output[0:-1]+'/test/']
FOLDER = None


def askUser():
    """
    Asks the user to specify the folder where all subfolders for the simulation
    should be created.
    
    """
    
    print "Where is the project folder?"
    targetFolder = raw_input("Enter the absolute path:")
    return targetFolder
    
def createFolders(targetFolder):
    """
    Creates subproject folders where simulations can be performed.
    
    Input: path to the project folder
    Output: all created paths  
    """
    createdFolders = []
    # Create Folders to prepare simulations
    for i in range(0, 10):
        print "Do you want to create folder 0"+ str(i)
        userinput = raw_input("Y or N:")
        if userinput == "y" or userinput =="y":
            subprocess.call(["mkdir", targetFolder+"/0"+str(i)])
            createdFolders.append(targetFolder+"/0"+str(i)+"/")
        elif userinput == "N" or userinput == "n":
            pass
        else:
            print "Either Y or N! Breaking"
            return createdFolders
    
    return createdFolders

def copyFiles(createFolders, files):
    """
    Takes a list of paths and copies all files present in a second list over
    
    Input: A list of folders and files
    Output: a list of all successfully copied files
    """

    copiedFiles = []
    # Copy needed files over
    for p in createdFolders:
        for f in files:
            print "Copying: " + f + " to " + p
            subprocess.call(['cp', '-R', f, p])  
            copiedFiles.append("Successfully copied " + f + " to " + p)
    
    return copiedFiles
    
    
target = askUser()
folders = createFolders(target)
print folders
copiedFiles = copyFiles(folders, FILES)
    
    
    
    
path = subprocess.Popen("pwd", stdout=subprocess.PIPE, shell=True)
(output, err) = path.communicate()

subprocess.call(["touch", output[0:-1]+"/test/myfile.txt"]) 


print "Today is", output