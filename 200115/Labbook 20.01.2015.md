## 20.01.2015

### Usefull stuff

* add folders to the .bashrc (located at the home folder)

```
cd 
vi .bashrc
```

* then add the path bash should load each time

### Simulation of two heptads

* 2 hepad long peptide was created using UCSF chimera
    * proline to ϕ = -80 and ψ = 160 (fixes prolines to trans configuration)
    * all other residues ϕ=-179 and ψ=179

* Verify that the angles are set correctly

```
g_chi -s CTD.pdb -f CDT.pdb -omega
xmgrace histo-omegaPro.xvg
```

* run pdb2gmx, put protein into a dodecahedral box and add water 

```
pdb2gmx -f CTD.pdb -o init.gro -p init.top -ignh -ter -vsite hydrogens -v #CHARMM22STAR
editcomf -f init.gro -o editconf.gro -bt dodecahedron -d 1.5 -center 0 0 0
genbox -cp -editconf.gro -cs spc216 -o genbox.gro -p init.top
```

* Run first energy minimization 

```
grompp -f em.md -c genbox.gro -p init.top -o em.tpr
mdrun -v -s em.tpr
```

* add ions

```
genion -s em.tpr -conc 0.15 -o genbox_genion.pdb -neutral -p init.top
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