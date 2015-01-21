## 20.01.2015

### Usefull stuff

* add folders to the .bashrc (located at the home folder)

```
cd 
vi .bashrc
```

* then add the path bash should load each time

### protocoll

* 2 hepad long peptide was created using UCSF chimera
	* proline to ϕ = -80 and ψ = 160 (fixes prolines to trans configuration)
	* all other residues ϕ=-179 and ψ=179

* Verify that the angles are set correctly

```
g_chi -s CTD.pdb -f CDT.pdb -omega
xmgrace histo-omegaPro.xvg
```

* Energy minimization

```
grompp -f em.mdp -c genbox_genion.pdb -p init.top -o em.tpr
mdrun -v -s em.tpr -c em.pdb
```


* Grompp .tpr file with berendsen.mdp 

```
grompp -f berendsen.mdp -c em.part0001.pdb -p init.top -o md.tpr
```

* Connect to the owl3 and enter the password

```
ssh owl3
```

* copy the files already made into a folder energy minimization folder

```
cd CTD/
mkdir em/
mv * em/
cd ..
mkdir berendsen/
cd em/
cp md.tpr ../berendsen/
```

* then run the simulation

``



### 21.01.15

#### Tutorial from the Book

* Download the PDB file 6BPTI
* Preprocessing with grompp 
	* Force field: Amber99SB-ILDN
	* Water model: TIP3P


```
pdb2gmx -f 6BPTI.pdb -water tip3p
```

* error due to inorganic compounds → deleting the phosohate (line 459-464 and line 457)
* start simulation with the same command again
* create simulation box and sovalte

```
editconf -f conf.gro -d 0.75 -o box.gro
genbox -f box.gro -cs spc216 -p topol.top -o solvated.gro
```

* add an empty mdp file for grompp and then ions

```
touch ions.mdp
grompp -f ions.mdp -p topol.top -c sovated.gro -o ions.tpr
```

* neutralize the system with
	* 7 sodium ions were added
	* 13 chloride ions were added

```
genion -s ions.tpr -neutral -conc 0.1 -p topol.top -o ions.gro
```

* set up the mdp file 

```
integrator=steep
nsteps=500
nstlist=10
rlist=1.0
coulombtype=pme
rcoulomb=1.0
vdw-type=cut-off
rvdw=1.0
nstenergy=10
```

* copy that content into em.mdp

```
cp ions.mdp em.mdp
```

* regrompp it and run energy minimization

```
grompp -f em.mdp -p topol.top -c ions.gro -o em.tpr
mdrun -v -deffnm em
```

* created pr.mdp which will be used to run the simulation
* 




