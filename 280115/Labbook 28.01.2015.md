## 28.012015

### Create a CTD template folder

* Create a template folder with all files necessary to start a simualtion

```
# Create a template folder with subfolders for em, eq, sim
CTD_template
cd CTD_template/
mkdir em
mkdir eq
mkdir sim
# Copy charmm22star.ff into folder and subfolders
cp -r 270115_CTD/charmm22star.ff/ CTD_template/
cd CTD_template/
cp -r charmm22star.ff/ em/
cp -r charmm22star.ff/ eq/
cp -r charmm22star.ff/ sim/
# Copy pdb file and mdp files into their respetive folders
cp 270115_CTD/CTD.pdb CTD_template/
cp 270115_CTD/em.mdp CTD_template/em/
cp 270115_CTD/berendsen.mdp CTD_template/eq/
cp 270115_CTD/sim.mdp CTD_template/sim/

``` 

### Run simulation again


* Copy content of CTD template folder into a new simulation folder 280115_CTD

```
cp -R CTD_template/. 280115_CTD/
```

* Run pdb2gmx using v-sites, 
    * From current directory 1: CHARMM22* all-atom force field
    * 4: TIPS3P CHARMM TIP 3-point with LJ on H's (note: twice as slow in GROMACS)
    * NH2
    * COOH
* generate box, water, ions
    * Replacing 40 solute molecules in topology file (topol.top)  by 20 NA and 20 CL ions   
```
pdb2gmx -f CTD.pdb -ignh -ter -vsite hydrogens -v
editconf -f conf.gro -o box.gro -bt dodecahedron -d 1.5 -center 0 0 0
genbox -cp box.gro -cs spc216.gro -p topol.top -o solvated.gro
touch ions.mdp
grompp -f ions.mdp -p topol.top -c solvated.gro -o ions.tpr
genion -s ions.tpr -neutral -conc 0.15 -p topol.top -o ions.gro

```

* Run EM

```
cd em/
grompp -f em.mdp -p ../topol.top -c ../ions.gro -o em.tpr
mdrun -v -deffnm em
```

* Check EM


```
g_energy -f em.part0001.edr -o potential.xvg
```

![EM](https://github.com/sagar87/MD/raw/master/280115/CTD/potential_.png)

* Copy the EM files to equilibration folder


```
cp em.part0001.gro ../eq
cp topol.top eq

```

* Run Equilibration with modified settings, so equilibration time is not so big

```
g_submit -s md.tpr -N short -nolaunch
vi jobscript.out.0001 
module add sge
qsub ./jobscript.out.0001
```

* Check system 

![Temperature](https://github.com/sagar87/MD/raw/master/280115/CTD/temperature_.png)

![Pressure](https://github.com/sagar87/MD/raw/master/280115/CTD/pressure_.png)

![Density](https://github.com/sagar87/MD/raw/master/280115/CTD/density_.png)

