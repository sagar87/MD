#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  2 16:48:11 2015

@author: Sagar
"""

import subprocess
path = subprocess.Popen("pwd", stdout=subprocess.PIPE, shell=True)
(output, err) = path.communicate()

FILES = [output[0:-1]+'/em.mdp', output[0:-1]+'/eq.mdp', output[0:-1]+'/sim.mdp', output[0:-1]+'/residuetypes.dat', output[0:-1]+'/charmm22star.ff/']
FOLDER = None


def askUser():
    """
    Asks the user to specify the folder where all subfolders for the simulation
    should be created.
    
    """
    print "Where is the project folder?"
    
    targetFolder = raw_input("Enter the absolute path:")
    return targetFolder
    
    
def setupFolder(targetFolder):
    # Create folders
    subprocess.call(["mkdir", targetFolder+"/em"])
    subprocess.call(["mkdir", targetFolder+"/eq"])
    subprocess.call(["mkdir", targetFolder+"/sim"])
    subprocess.call(["mkdir", targetFolder+"/charmm22star.ff"])
    print "Folders successfully created"
    # Create Subfolders

    subprocess.call(["mkdir", targetFolder+"/em/charmm22star.ff"])
    subprocess.call(["mkdir", targetFolder+"/eq/charmm22star.ff"])
    subprocess.call(["mkdir", targetFolder+"/sim/charmm22star.ff"])    
    print "Copied Forcefield successfully"

    # Create copy mdp and residue dat files over    
    subprocess.call(['cp', '-R', FILES[0], targetFolder+"/em"])
    subprocess.call(['cp', '-R', FILES[1], targetFolder+"/eq"])
    subprocess.call(['cp', '-R', FILES[2], targetFolder+"/sim"])
    subprocess.call(['cp', '-R', FILES[3], targetFolder+"/"])
        
    
    # Copy Charmm22star ff to the project folder
    subprocess.call(['cp', '-R', FILES[4], targetFolder+"/charmm22star.ff"])
    subprocess.call(['cp', '-R', FILES[4], targetFolder+"/em/charmm22star.ff"])
    subprocess.call(['cp', '-R', FILES[4], targetFolder+"/eq/charmm22star.ff"])
    subprocess.call(['cp', '-R', FILES[4], targetFolder+"/sim/charmm22star.ff"])
    
    # Copy residue.dat in em, eq and sim folder 
    subprocess.call(['cp', '-R', FILES[3], targetFolder+"/em"])
    subprocess.call(['cp', '-R', FILES[3], targetFolder+"/eq"])
    subprocess.call(['cp', '-R', FILES[3], targetFolder+"/sim"])
    print "All done!"

    
    
destiny = askUser()

print "Copy files over?"
ans = raw_input("Y/N:")

if ans == "y":
    setupFolder(destiny)