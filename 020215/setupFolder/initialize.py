#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  2 16:48:11 2015

@author: Sagar
"""

import subprocess
path = subprocess.Popen("pwd", stdout=subprocess.PIPE, shell=True)
(output, err) = path.communicate()

FILES = [output[0:-1]+'/em.mdp', output[0:-1]+'/eq.mdp', output[0:-1]+'/sim.mdp', output[0:-1]+'/residuetypes.dat', output[0:-1]+'/charmm22star.ff']
FOLDER = None


def askFolder():
    """
    Asks the user to specify the folder where all subfolders for the simulation
    should be created.
    
    """
    print "Where is the project folder?"
    
    targetFolder = raw_input("Enter the absolute path:")
    return targetFolder
    
def askPdb():
    """
    Asks the user to specify the folder where all subfolders for the simulation
    should be created.
    
    """
    print "Where is the project folder?"
    
    targetFolder = raw_input("Enter the absolute path:")
    return targetFolder    
    
    
def initalizeSim(target):
    
    path = "/".join(target.split("/")[0:-1])

    print "###########################"
    print "Starting pdb2gmx"
    print "###########################"
    subprocess.call(["pdb2gmx", "-f", target, "-o", path+"/conf.gro", "-p", path+"/topol.top", "-i", path+"/posre.itp", "-ignh", "-ter", "-v"])
    #subprocess.call(["pdb2gmx", "-f", target, "-o", path+"/conf.gro" "-ignh", "-ter", "-v"])

    print "###########################"
    print "###########################"
    print "###########################"
    print "Create a Box"
    print "###########################"
    print "###########################"
    print "###########################"
    ans = raw_input("Press to Continue!")
    subprocess.call(["editconf", "-f", path+"/conf.gro", "-o", path+"/box.gro", "-bt", "dodecahedron", "-center", "0 0 0", "-d", "1.5"])
    print "###########################"    
    print "###########################"    
    print "###########################"
    print "Adding Water"
    print "###########################"
    print "###########################"
    print "###########################"
    ans = raw_input("Press to Continue!")
    subprocess.call(["genbox", "-cp", path+"/box.gro", "-cs", "spc216.gro", "-p", path+"/topol.top", "-o", path+"/solvated.gro"])
    print "###########################"    
    print "###########################"    
    print "###########################"
    print "Generate Ions"
    print "###########################"
    print "###########################"
    print "###########################"
    ans = raw_input("Press to Continue!")
    subprocess.call(["touch", path+"/ions.mdp"])
    subprocess.call(["grompp", "-f", path+"/ions.mdp", "-p", path+"/topol.top", "-c", path+"/solvated.gro", "-o", path+"/ions.tpr", "-po", path+"/mdout.mdp"])
    subprocess.call(["genion", "-s", path+"/ions.tpr", "-neutral", "-conc", "0.15", "-p", path+"/topol.top", "-o", path+"/ions.gro"])
    print "###########################"    
    print "###########################"    
    print "###########################"
    print "Preparing EM"
    print "###########################"
    print "###########################"
    print "###########################"
    ans = raw_input("Press to Continue!")
    subprocess.call(["cp", path+"/topol.top", path+"/ions.gro", path+"/em"])
    print "###########################"    
    print "###########################"    
    print "###########################"
    print "Starting EM"
    print "###########################"
    print "###########################"
    print "###########################"
    subprocess.call(["grompp", "-f", path+"/em/em.mdp", "-p", path+"/em/topol.top", "-c", path+"/em/ions.gro", "-o", path+"/em/em.tpr", "-po", path+"/mdout.mdp"])

destiny = askFolder()

print "Copy files over?"
ans = raw_input("Y/N:")

if ans == "y":
    initalizeSim(destiny)
