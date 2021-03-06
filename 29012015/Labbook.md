## 29.01.2015

### Simulation with new 2x heptad created in Pymol

* Creat a new 2x CTD-heptad in Pymol 


```
for aa in "YSPTSPSYSPTSPS": cmd._alt(string.lower(aa))

```

* Set up a fresh folder for simulation

```
mkdir 29012015_CTD_Pymol
cp -R CTD_template/. 29012015_CTD_Pymol/
```

* Create pdb2gmx, box, add ions 
    * neutral termini NH2 and COOH
    * 15 NA and CL ions were added

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
cp topol.top em/
cp ions.gro em/
grompp -f em.mdp -p topol.top -c ions.gro -o em.tpr
mdrun -v -deffnm em

```

* Error presumeably due to missing acetyl and methyl ends → Create a new peptide that has these modifications

### Simulation with 2x heptad that has CT-Ac and NT-Me Modification

* Create a New peptide in pymol
    * Select Build → Residue → Acetylgroup
    * run the command denoted
    * Select Build → Residue → Methylgroup

```
for aa in "YSPTSPSYSPTSPS": cmd._alt(string.lower(aa))
```

* Modify the topology
    * Change the N-ternal End from NME to CT3
    * Add with USCF Chimera Hydrogens
        * Tools → Structure Editing → AddH then click ok
        * Save new pdb
    * Again change the PDB File from 
    
```
HETATM  201  H   CT3    16       3.414 -14.547  18.567  1.00  0.00           H
HETATM  202 1HH3 CT3    16       1.206 -14.149  16.533  1.00  0.00           H
HETATM  203 2HH3 CT3    16       1.010 -15.486  17.657  1.00  0.00           H
HETATM  204 3HH3 CT3    16       1.033 -13.832  18.253  1.00  0.00           H
CONECT    4    3
CONECT    5    3
CONECT    6    3
CONECT    1    2    7    3
CONECT    3    1    6    4    5
CONECT    2    1
CONECT    7    8    1   19
CONECT  190  189  191  199
CONECT  202  200
CONECT  203  200
CONECT  204  200
CONECT  200  199  202  203  204
CONECT  201  199
CONECT  199  190  200  201
END

```

* to

```
HETATM  201  HN  CT3    16       3.414 -14.547  18.567  1.00  0.00           H
HETATM  202 HH31 CT3    16       1.206 -14.149  16.533  1.00  0.00           H
HETATM  203 HH32 CT3    16       1.010 -15.486  17.657  1.00  0.00           H
HETATM  204 HH33 CT3    16       1.033 -13.832  18.253  1.00  0.00           H
END

```

* Create a new folder (...)
* Preprocess the gro-file
    * WITH CHARMM27
    * For Termini select None 

```
pdb2gmx -f AcCTDME_Water.pdb -ter -ignh -v

```

* Process again with Charmm22*

```
pdb2gmx -f conf.gro -vsite hydrogens -ter -v
```

* Create box, water, ions


```
editconf -f conf.gro -o box.gro -bt dodecahedron -d 1.5 -center 0 0 0
genbox -cp box.gro -cs spc216.gro -p topol.top -o solvated.gro
touch ions.mdp
```

* Again error → try to fix it 
* Start with PDB with hydrogens and rename the
    * Change Nm
* preprocess with amber99sb-ildn

(....)

* Not successful 


### Run Simulation with CTD Pymol, vSites and charged Termini   

* Try to use CTD created with Pymol earlier this morning
    * use NH3+ and COO-

```
pdb2gmx -f CTD_pymol.pdb -ignh -ter -vsite hydrogens -v
editconf -f conf.gro -o box.gro -bt dodecahedron -d 1.5 -center 0 0 0
genbox -cp box.gro -cs spc216.gro -p topol.top -o solvated.gro
touch ions.mdp
grompp -f ions.mdp -p topol.top -c solvated.gro -o ions.tpr
genion -s ions.tpr -neutral -conc 0.15 -p topol.top -o ions.gro
```

* Run EM

```
cp topol.top em/
cp ions.gro em/
grompp -f em.mdp -p topol.top -c ions.gro -o em.tpr
mdrun -v -deffnm em

```

* Check EM

![EM](https://github.com/sagar87/MD/raw/master/29012015/potential_pym.png)

* Run equilibration (same mdp as yesterday)
    * copy eq.mdp over 
    * copy em.part0001.gro and topology.top into eq/ folder

```
grompp -f eq.mdp -p topol.top -c em.part0001.gro -o eq.tpr
ssh owl3
g_submit -s eq.tpr

```

* Check EQ

```
               Core t (s)   Wall t (s)        (%)
       Time:    29608.680     9872.508      299.9
                         2h44:32
                 (ns/day)    (hour/ns)
Performance:        8.752        2.742
Finished mdrun on node 0 Thu Jan 29 17:53:43 2015
```

![After EQ CTD (Pymol)](https://github.com/sagar87/MD/raw/master/29012015/temp_pym_VT_CT.xvg_.png)

![After EQ CTD (Pymol)](https://github.com/sagar87/MD/blob/master/29012015/press_pym_VT_CT.xvg_.png)

![After EQ CTD (Pymol)](https://github.com/sagar87/MD/blob/master/29012015/dens_pym_VT_CT.xvg_.png)

### Run Simulation with original CTD, vSites and charged Termini   

* Create dir *290115_CTD_VS_CT*
    * *CT* → Charged Termini
    * *VS* → Virtual sites
* Copy template folder over
* Set everything up
    * NH3+ and COO-


```
pdb2gmx -f CTD.pdb -ignh -ter -vsite hydrogens -v
editconf -f conf.gro -o box.gro -bt dodecahedron -center 0 0 0 -d 1.5
genbox -cp box.gro -cs spc216.gro -p topol.top -o solvated.gro
touch ions.mdp
grompp -f ions.mdp -p topol.top -c solvated.gro -o ions.tpr
genion -s ions.tpr -neutral -conc 0.15 -p topol.top -o ions.gro
cp topol.top ions.gro em/
```

* Run EM

```
grompp -f em.mdp -p topol.top -c ions.gro -o em.tpr
mdrun -v -deffnm em

```

* Check EM

![EM](https://github.com/sagar87/MD/raw/master/29012015/potential_org.png)

* Run EQ

```
cp em/em.part0001.gro em/topol.top eq/
cp ~/290115_CTD_Pymol/eq/eq.mdp ./
grompp -f eq.mdp -p topol.top -c em.part0001.gro -o eq.tpr
ssh owl3
g_submit -s eq.tpr
```

* Run finished in 1h


```
       Time:    38287.880     3829.646      999.8
                         1h03:49
                 (ns/day)    (hour/ns)
Performance:       22.561        1.064
Finished mdrun on node 0 Thu Jan 29 16:17:36 2015
```

* Check Equilibration

```
g_energy -f ener.part0001.edr -o temp.xvg
g_energy -f ener.part0001.edr -o press.xvg
g_energy -f ener.part0001.edr -o dens.xvg
```

![After EQ](https://github.com/sagar87/MD/raw/master/29012015/temp_CTD_VS_CT.xvg_.png)

![After EQ](https://github.com/sagar87/MD/raw/master/29012015/press_CTD_VS_CT.xvg_.png)

![After EQ](https://github.com/sagar87/MD/raw/master/29012015/dens_CTD_VS_CT.xvg_.png)


* Prepare Simulation (copy from eq to sim folder)

```
cp eq/confout.part0001.gro eq/topol.top sim/
```

* Run Simulation

```
grompp -f sim.mdp -p topol.top -c confout.part0001.gro -o sim.tpr
g_submit -s sim.tpr 
```

### Run Simulation with original CTD, no vSites and uncharged Termini

* Create dir *290115_CTD_NVT_NCT* 
* Copy template folder into this folder
* Change options in sim.mdp and eq.mdp
    * dt = 0.0002 so it is appropriate for simulation that do not use vsites
    * hbonds instead of allbonds constraints 
* Set everything up
    * NH2 and COOH


```
pdb2gmx -f CTD.pdb -ignh -ter -v
editconf -f conf.gro -o box.gro -bt dodecahedron -center 0 0 0 -d 1.5
genbox -cp box.gro -cs spc216.gro -p topol.top -o solvated.gro
touch ions.mdp
grompp -f ions.mdp -p topol.top -c solvated.gro -o ions.tpr
genion -s ions.tpr -neutral -conc 0.15 -p topol.top -o ions.gro
cp topol.top ions.gro em/
```

* Run EM

```
grompp -f em.mdp -p topol.top -c ions.gro -o em.tpr
mdrun -v -deffnm em
```

* Check EM

![EM](https://github.com/sagar87/MD/raw/master/29012015/potential_CTD_ORG_NVT_NCT.png)

* Run EQ

```
cp em/em.part0001.gro em/topol.top eq/
grompp -f eq.mdp -p topol.top -c em.part0001.gro -o eq.tpr
ssh owl3
g_submit -s eq.tpr
```





