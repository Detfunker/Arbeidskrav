# -*- coding: utf-8 -*-
"""
Arbeidskrav 1,
et Python-program som beregner og presenterer (i konsollen) 
de årlige totalkostnadene for elbil og for bensinbil 
samt årlig kostnadsdifferanse 
"""
K = 10000  # Antall km i aaret

"""
Under følger utregning av totale Kostnader for Elbil som funksjon av antall
km kjort i aaret
"""
F = 5000 + (8.38*365) # Faste kostnader aarlig Elbil
C = 0.4 # stromforbruk i kr per km
B = 0.1 # bomavgift i kr per km
V = K*(C+B) # variable kostnader Elbil
T = V + F # Totale kostnader aarlig Elbil

print("Total kost Elbil =", T)

"""
Under følger utregning av totale kostnader for Bensinbil som funksjon av
antall km kjort i aaret
"""

F2 = 7500 + (8.38*365) # Faste kostnader aarlig Bensinbil
C2 = 1 # bensinforbruk i kr per km
B2 = 0.3 # bomavgift i kr per km
V2 = K*(C2+B2) # variable kostnader Elbil
T2 = V2 + F2 # Totale kostnader aarlig Elbil

print("Total kost Bensinbil =", T2)

"""
Under følger utregning av differansen mellom aarlige kostnader for Elbil og
Bensinsbil
"""

Diff = T-T2

print("Differanse i kr =", Diff)















