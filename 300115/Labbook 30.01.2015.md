## 30.01.2015

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

![CTD Pymol VT CTD](https://github.com/sagar87/MD/blob/master/300115/rmsf_CTD_PYM_VT_CT.xvg_.png)