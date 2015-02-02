# Labbook 30.01.2015

### Simulation with original CTD, no vSites and uncharged Termini

* Equilibration was successful

```
               Core t (s)   Wall t (s)        (%)
       Time:   329876.580    33009.459      999.3
                         9h10:09
                 (ns/day)    (hour/ns)
Performance:       13.087        1.834
Finished mdrun on node 0 Fri Jan 30 01:16:25 2015

``` 

* Check Equilibration


```
g_energy -f ener.part0001.edr -o temp.xvg
g_energy -f ener.part0001.edr -o press.xvg
g_energy -f ener.part0001.edr -o dens.xvg

```


![After EQ](https://github.com/sagar87/MD/raw/master/300115/temp_CTD_NVT_NCT.xvg_.png)

![After EQ](https://github.com/sagar87/MD/raw/master/300115/press_CTD_NVT_NCT.xvg_.png)

![After EQ](https://github.com/sagar87/MD/raw/master/300115/dens_CTD_NVT_NCT.xvg_.png)

* Prepare and start simulation

```
cp eq/confout.part0001.gro eq/topol.top sim/
grompp -f sim.mdp -p topol.top -c confout.part0001.gro -o sim.tpr
ssh owl3
g_submit -s sim.tpr
```

### Analysis of CTD Pymol with vSites and charged Termini

* Simulation was successful


```
               Core t (s)   Wall t (s)        (%)
       Time:   217793.170    36387.224      598.5
                         10h06:27
                 (ns/day)    (hour/ns)
Performance:       23.745        1.011
Finished mdrun on node 0 Fri Jan 30 04:59:05 2015
```

* Check RMSD (compared to the structure before EM → long chain)
    * Protein-H
* Check Root Mean Square fluctuation (RMSF) → Cα 
    

```
g_rms -s ../em/em.tpr -f traj.part0001.xtc 
g_rmsf -s sim.tpr -f traj.part0001.xtc -o rmsf_CTD_PYM_VT_CT.xvg -oq bfac.pdb
```

![CTD Pymol VT CT](https://github.com/sagar87/MD/raw/master/300115/rmsd.xvg_.png)

![CTD Pymol VT CTD](https://github.com/sagar87/MD/raw/master/300115/rmsf_CTD_PYM_VT_CT.xvg_.png)

* Analyze secondary strucures

```
do_dssp -s sim.tpr -f traj.part0001.xtc -ver 1
xpm2ps -f ss.xpm
gv plot.eps
```

![Secondary Structures](https://github.com/sagar87/MD/raw/master/300115/plot.eps)

* Check Radius of Gyration and H-bonds

```
g_gyrate s sim.tpr -f traj.part0001.xtc
g_hbond -s sim.tpr -f traj.part0001.xtc -num hbond.xvg
```

![Radius of Gyration](https://github.com/sagar87/MD/raw/master/300115/gyrate_CTD_PYM_VT_CT.png)

![H-Bonds](https://github.com/sagar87/MD/raw/master/300115/hbond_CTD_PYM_CT_VT.xvg_.png)


### Analysis of original CTD with vSites and charged Termini


* Simulation was successful


```
               Core t (s)   Wall t (s)        (%)
       Time:   509136.450    51309.771      992.3
                         14h15:09
                 (ns/day)    (hour/ns)
Performance:       16.839        1.425
Finished mdrun on node 0 Fri Jan 30 08:08:28 2015
```

* Check RMSD (compared to the structure before EM → long chain)
    * Protein-H
* Check Root Mean Square fluctuation (RMSF) → Cα 
    
```
g_rms -s ../em/em.tpr -f traj.part0001.xtc 
g_rmsf -s sim.tpr -f traj.part0001.xtc -o rmsf_CTD_PYM_VT_CT.xvg -oq bfac.pdb
```

![RMSD](https://github.com/sagar87/MD/raw/master/300115/rmsd_CTD_VS_CT.xvg_.png)

![RMSF](https://github.com/sagar87/MD/raw/master/300115/rmsf_CTD_VS_CT.xvg_.png)

* Analyze secondary strucures

```
do_dssp -s sim.tpr -f traj.part0001.xtc -ver 1
xpm2ps -f ss.xpm
gv plot.eps
```

* Check Radius of Gyration and H-bonds

```
g_gyrate s sim.tpr -f traj.part0001.xtc
g_hbond -s sim.tpr -f traj.part0001.xtc -num hbond.xvg
```

![](https://github.com/sagar87/MD/raw/master/300115/gyrate_CTD_VS_CT.png)

![H-bonds](https://github.com/sagar87/MD/raw/master/300115/hbond_CTD_VS_CT.xvg_.png)

### Start Long Simulations with equilibrated original CTD NVT NCT

* Create a bash script that automates folder creation 
* Script takes three variables from command line
    * $1 the path to the folder where the simulation folders should be created
    * $2 the path to the equilibration folder where the topology and the gro file are 
    * $3 mdp file (which has to be in the folder of the script)

```
mkdir $1/03
cp -v $3 $1/03
cp -v $2/topol.top $2/confout.part0001.gro $1/03
cp -R -v $2/charmm22star.ff $1/03

mkdir $1/04
cp -v $3 $1/04
cp -v $2/topol.top $2/confout.part0001.gro $1/04
cp -R -v $2/charmm22star.ff $1/04

mkdir $1/05
cp -v $3 $1/05
cp -v $2/topol.top $2/confout.part0001.gro $1/05
cp -R -v $2/charmm22star.ff $1/05

mkdir $1/06
cp -v $3 $1/06
cp -v $2/topol.top $2/confout.part0001.gro $1/06
cp -R -v $2/charmm22star.ff $1/06

mkdir $1/07
cp -v $3 $1/07
cp -v $2/topol.top $2/confout.part0001.gro $1/07
cp -R -v $2/charmm22star.ff $1/07

mkdir $1/08
cp -v $3 $1/08
cp -v $2/topol.top $2/confout.part0001.gro $1/08
cp -R -v $2/charmm22star.ff $1/08

mkdir $1/09
cp -v $3 $1/09
cp -v $2/topol.top $2/confout.part0001.gro $1/09
cp -R -v $2/charmm22star.ff $1/09

mkdir $1/10
cp -v $3 $1/10
cp -v $2/topol.top $2/confout.part0001.gro $1/10
cp -R -v $2/charmm22star.ff $1/10

echo '##############################################'
echo '##############################################'
echo '##############################################'
echo 'Copying done'
echo 'Proceed with gromping'
pause 'Press [Enter] key to continue...'
echo '##############################################'
echo '##############################################'
echo '##############################################'


grompp -f $1/01/sim.mdp -p $1/01/topol.top -c $1/01/confout.part0001.gro -o $1/01/sim.tpr -maxwarn 1
grompp -f $1/02/sim.mdp -p $1/02/topol.top -c $1/02/confout.part0001.gro -o $1/02/sim.tpr -maxwarn 1
grompp -f $1/03/sim.mdp -p $1/03/topol.top -c $1/03/confout.part0001.gro -o $1/03/sim.tpr -maxwarn 1
grompp -f $1/04/sim.mdp -p $1/04/topol.top -c $1/04/confout.part0001.gro -o $1/04/sim.tpr -maxwarn 1
grompp -f $1/05/sim.mdp -p $1/04/topol.top -c $1/05/confout.part0001.gro -o $1/05/sim.tpr -maxwarn 1
grompp -f $1/06/sim.mdp -p $1/04/topol.top -c $1/06/confout.part0001.gro -o $1/06/sim.tpr -maxwarn 1
grompp -f $1/07/sim.mdp -p $1/04/topol.top -c $1/07/confout.part0001.gro -o $1/07/sim.tpr -maxwarn 1
grompp -f $1/08/sim.mdp -p $1/04/topol.top -c $1/08/confout.part0001.gro -o $1/08/sim.tpr -maxwarn 1
grompp -f $1/09/sim.mdp -p $1/04/topol.top -c $1/09/confout.part0001.gro -o $1/09/sim.tpr -maxwarn 1
grompp -f $1/10/sim.mdp -p $1/04/topol.top -c $1/10/confout.part0001.gro -o $1/10/sim.tpr -maxwarn 1
```

* Use the script to generate all folders

```
~/290115_CTD_NVT_NCT/sim
```