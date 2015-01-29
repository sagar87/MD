## 22.01.15

### Tutorial from the book

* Rerun the simulation from the beginning, this time using different folders for each step of the simulation
* simulation started

### Trajectory Analysis of simulation from 20.01.15

* Connect via ssh

```
ssh -XY hvoehri@hvoehri.mpibpc.intern
```


* RMSD calculation performed as follows, selecting two times 1 for protein

```
g_rms -s ../em.tpr -f traj.part0001.xtc
xmgrace rmsd.xvg
```

![RMSD](https://raw.githubusercontent.com/sagar87/MD/master/220115/rmsd_berendsen.png)

* Comparing fluctuations of Cα-atoms with g_rmsf tool

```
g_rmsf -s md.tpr -f traj.part0001.xtc -o rmsf.xvg -oq bfaq.pdb
xmgrace rmsf.xvg
```

![RMSF of Cα atoms](https://raw.githubusercontent.com/sagar87/MD/master/220115/rmsf_berendsen.png)

* Analysis of Secondary structures

```
do_dssp -s md.tpr -f traj.part0001.xtc -ver 1
xmp2ps -f ss.xpm
gv plot.eps
```

![Secondary Structures](https://raw.githubusercontent.com/sagar87/MD/master/220115/secondary_structure.png)

* Radius of Gyration

```
g_gyrate -s md.tpr -f traj.part0001.xtc 
```

![Radius of gyration](https://raw.githubusercontent.com/sagar87/MD/master/220115/gyrate_berendsen.png)

* Number of H-bonds between protein and protein itself

```
g_hbond -s md.tpr -f traj.part0001.xtc  -num hbnum.xvg
```

![](https://raw.githubusercontent.com/sagar87/MD/master/220115/hbond_protein_protein_berendsen.png)