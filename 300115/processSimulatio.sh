#!/bin/bash

g_energy -f ener.part0001.edr -o temp$1.xvg
g_energy -f ener.part0001.edr -o press$1.xvg
g_energy -f ener.part0001.edr -o dens$1.xvg
