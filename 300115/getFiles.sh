#!/bin/bash

sshpass -p "hvoehri@105" scp -r hvoehri@hvoehri.mpibpc.intern:~/$1rmsd_$2.xvg ./
sshpass -p "hvoehri@105" scp -r hvoehri@hvoehri.mpibpc.intern:~/$1rmsf_$2.xvg ./
sshpass -p "hvoehri@105" scp -r hvoehri@hvoehri.mpibpc.intern:~/$1plot.eps ./
sshpass -p "hvoehri@105" scp -r hvoehri@hvoehri.mpibpc.intern:~/$1hbond_$2.eps ./
sshpass -p "hvoehri@105" scp -r hvoehri@hvoehri.mpibpc.intern:~/$1gyrate_$2.xvg ./
