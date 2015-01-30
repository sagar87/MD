## 30.01.2015

## Simulation with original CTD, no vSites and uncharged Termini

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

