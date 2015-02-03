## 02.02.2015

# Check if simulations were successful

```
# Simulation 01   
               Core t (s)   Wall t (s)        (%)
       Time:  1710280.210   171072.455      999.7
                         1d23h31:12
                 (ns/day)    (hour/ns)
Performance:       10.210        2.351
Finished mdrun on node 0 Sun Feb  1 17:13:47 2015

# Simulation 02

               Core t (s)   Wall t (s)        (%)
       Time:  1710309.910   171072.408      999.8
                         1d23h31:12
                 (ns/day)    (hour/ns)
Performance:       10.823        2.217
Finished mdrun on node 0 Sun Feb  1 17:18:28 2015

# Simulation 02

               Core t (s)   Wall t (s)        (%)
       Time:  1710142.690   171072.434      999.7
                         1d23h31:12
                 (ns/day)    (hour/ns)
Performance:        8.807        2.725
Finished mdrun on node 0 Sun Feb  1 17:18:29 2015

# Simulation 03

(....)

```

* Restart the simulations with 

```
g_submit g_submit -cpi state.cpt -s sim.tpr
```

### Create Mutant CTD structures

* Create Mutants, which has the following structure 

```
# CTD_pS2
01-02-03-04-05-06-07-08-09-10-11-12-13-14 # Residuenumber
Y  pS P  T  S  P  S  Y  pS P  T  S  P  S


# CTD_pS5
01-02-03-04-05-06-07-08-09-10-11-12-13-14 # Residuenumber
Y  S  P  T  pS P  S  Y  S  P  T  pS  P  S

# CTD_pS2_T4V
01-02-03-04-05-06-07-08-09-10-11-12-13-14 # Residuenumber
Y  pS P  V  S  P  S  Y  pS P  V  S  P  S

# CTD_pS2_Y1F
01-02-03-04-05-06-07-08-09-10-11-12-13-14 # Residuenumber
F  pS P  V  S  P  S  F  pS P  V  S  P  S

```

* 2 hepad long peptide was created using UCSF chimera
    * proline to ϕ = -80 and ψ = 160 (fixes prolines to trans configuration)
    * all other residues ϕ=-179 and ψ=179
    * Tools → Structure Editing → addH
    * To add P select hydroxyl H atom of Ser 02 and Ser 09 and change it to phosphate → Tool → Structure Editing → Build Structure → Modify Structure
        * Element P with 4 bonds and tetrahedral geometry
        * Set atoms name to P1
        * Connect to preexisting atoms yes
        * Color new atoms by element yes
        * Residue Name Leave unchanged      
    * To add the Oxygens select the hydrogens connected to the phosphate and modify the structure
        * Element O with 1 bond 
        * Set atom names to O1
        * Connect to pre-existing atoms if appropiate yes
        * Color new elements by element yes
        * Residue Name leave unchanged

* Create scripts that automate folder and initialize em
    * setupFolder.py sets the the folder structure for a simulation and copies all necessary files into the specified folder
    * initialize.py exceutes the all commands that are necessary to energy minimize the the system


```
/home/hvoehri/020215_CTD_p2S_T4V/CTD_pS2_T4V.pdb
/home/hvoehri/020215_CTD_pS2/CTD_pS2.pdb
/home/hvoehri/020215_CTD_pS2_Y1F/CTD_pS2_Y1F.pdb
/home/hvoehri/020215_CTD_pS5/CTD_pS5.pdb
/home/hvoehri/020215_CTD_T4V/CTD_T4V.pdb
/home/hvoehri/020215_CTD_Y1F/CTD_Y1F.pdb
```

