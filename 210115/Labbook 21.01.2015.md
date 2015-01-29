## 21.01.15

### Tutorial from the Book

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
* grompp the file and run simulation with settings defined in pr.mdp


```
grompp -f pr.mdp -p topol.top -c ions.gro -o pr.tpr
mdrun -v deffnm pr
```

* commands did not work, presumably because something with the deffnm flag did not work properly
* rerun mdrun this time using the following settings

```
mdrun -v -s em.tpr -c em.pdb
grompp -f pr.mdp -p topol.top -c em.gro -o pr.tpr
mdrun -v -s pr.tpr -c ions.pdb
``` 

* error in the simulation


```
Off! I just backed up step5b.pdb to ./#step5b.pdb.1#

Back Off! I just backed up step5c.pdb to ./#step5c.pdb.1#
Wrote pdb files with previous and current coordinates

WARNING: Listed nonbonded interaction between particles 143 and 164
at distance 3f which is larger than the table limit 3f nm.

This is likely either a 1,4 interaction, or a listed interaction inside
a smaller molecule you are decoupling during a free energy calculation.
Since interactions at distances beyond the table cannot be computed,
they are skipped until they are inside the table limit again. You will
only see this message once, even if it occurs for several interactions.

IMPORTANT: This should not happen in a stable simulation, so there is
probably something wrong with your system. Only change the table-extension
distance in the mdp file if you are really sure that is the reason.



WARNING: Listed nonbonded interaction between particles 532 and 548
at distance 3f which is larger than the table limit 3f nm.

This is likely either a 1,4 interaction, or a listed interaction inside
a smaller molecule you are decoupling during a free energy calculation.
Since interactions at distances beyond the table cannot be computed,
they are skipped until they are inside the table limit again. You will
only see this message once, even if it occurs for several interactions.

IMPORTANT: This should not happen in a stable simulation, so there is
probably something wrong with your system. Only change the table-extension
distance in the mdp file if you are really sure that is the reason.
```