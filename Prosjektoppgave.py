""" a) et program som leser inn filen support_uke_24.xlsx. og lagrer data i variabler"""

import pandas as pd #importeres for å kunne lese eller skrive excel
import numpy as np # trenger  ifølge  forelesning for å lage array, men  ikke  i bruk?

data = pd.read_excel("support_uke_24.xlsx")
u_dag = data['Ukedag'].values
kl_slett = data['Klokkeslett'].values
varighet = data['Varighet'].values
score = data['Tilfredshet'].values # omsetter kolloneverdiene i excel-arket  til rene  arrays

##print(type(u_dag[0]))
##print(type(varighet[0])) #sjekker hvordan det første elementet i listen blir tolket av  py.
##print(type(kl_slett[0])) 
##print(type(score[1])) # vet fra excel at det ikke er registrert score på plass  0..
 

##varighet og kl_slett tolkes som class str, streng, altså tekst. vi må konvertere for å kunne gjøre beregninger

# Konvertering av varighet (HH:MM:SS) til desimalminutter
varighet_i_minutter = [
    int(tid.split(":")[0]) * 60 + int(tid.split(":")[1]) + int(tid.split(":")[2]) / 60
    for tid in varighet
]

# Konvertering av klokkeslett (HH:MM:SS) til desimaltimer
kl_slett_i_timer = [
    int(tid.split(":")[0]) + int(tid.split(":")[1])/60 + int(tid.split(":")[2])/3600
    for tid in kl_slett
]


##print(kl_slett_i_timer) # for å sjekke at det blir riktig 
##print(varighet_i_minutter)

""" del b) skriv et program som finner  antall henvendelser for hver av de fem
ukedagene. Resultatet visualiseres ved hjelp  av et søylediagram """

from collections import Counter #importerer for å kunne telle antall dager under kollonnen ukedager
import matplotlib.pyplot as plt #importere for å kunne vise søylediagram

data = pd.read_excel("support_uke_24.xlsx")
u_dag = data['Ukedag'].values

ukedag_antall_unike = Counter(u_dag) #teller antall observasjoner  under hver nøkkel/klasse(ukedag)
print(ukedag_antall_unike)

# hva som  skal inn i  søylediagrammet, keys tilsvarer navn eller klasse(ukedag), 
# values er hvor mange observasjoner som  er  i hver  klasse

plt.bar(ukedag_antall_unike.keys(),ukedag_antall_unike.values())


# visuelt resultat i  søylediagram  
plt.title("Henvendelser per dag")
plt.xlabel("Ukedag")
plt.ylabel("antall henvendelser")
plt.show()



""" del c) Skriv et program som finner minste og lengste samtaletid 
som er loggført for uke 24. Svaret skrives til skjerm med informativ tekst."""

korteste_Samtale = min(varighet) # finner den minste verdien i arrayen varighet og oppretter variabel
lengste_samtale =  max(varighet) # finner den høyeste verdien i arrayen varighet og  oppretter variabel

print("Korteste loggførte samtaletid for uke 24 er:", korteste_Samtale)
print("Lengste loggførte samtaletidfor for uke 24 er:", lengste_samtale)

""" del d) gjennomsnittlig samtaletid loggført uke 24"""

Antall_samtaler = len(u_dag)
Total_samtaletid = sum(varighet_i_minutter)
Gjennomsnitt_samt  = Total_samtaletid/Antall_samtaler
print("Antall samtaler var:", Antall_samtaler)
print("Total samtaletid for uke 24 var:", Total_samtaletid, "minutter")
print("Gjennomsnittlig samtaletid for uke 24 var:", round(Gjennomsnitt_samt, 2),"minutter")

""" del e) Totalt antall henvendelser 
for hvert av tidsrommene: 08-10, 10-12, 12-14 og 14-16"""

import matplotlib.pyplot as plt



# Funksjon som klassifiserer samtalene/henvendelsene etter tidsrom
def klassifiser_tidsrom(liste):
    SenDag = 0
    Ettermiddag = 0
    Midtdag = 0
    Morgen = 0
    for element in liste:
        if 14 <= element <= 16:
            SenDag += 1
        elif 12 <= element < 14:
            Ettermiddag += 1
        elif 10 <= element < 12:
            Midtdag += 1
        elif 8 <= element < 10:
            Morgen += 1
    print("Sen Ettermiddag:", SenDag, "Ettermiddag:", Ettermiddag, "Morgen:", Midtdag, "Tidlig morgen:", Morgen)
    return [Morgen, Midtdag, Ettermiddag, SenDag]
    
    
#Kaller funksjonen
resultaterKlass = klassifiser_tidsrom(kl_slett_i_timer)
print(resultaterKlass)
Merkelapper = ["Tidlig Morgen (08-10)", "Morgen (10-12)", "Ettermiddag (12-14)", "Sen ettermiddag (14-16)"]
Sizes = resultaterKlass
plt.pie(Sizes,  labels=Merkelapper, autopct= "%1.1f%%", startangle= 90)

plt.title("Henvendelser og tidspunkt på dagen")
plt.show()

""" Deloppgave f) Et program sim regner ut supportavdelingens Net Promoter Score (NPS)
og skriver ut til skjerm. """

def finn_pos_noy_neg(arr):
    ant_pos = 0
    ant_neg = 0
    ant_noy = 0
    for element in arr:

        if element >= 9:
            ant_pos += 1
        elif 7 <= element <= 8:
            ant_noy += 1
        elif 1 <= element <= 6:
            ant_neg += 1
            
    print("Antall positive kunder:", ant_pos)
    print("Antall nøytrale kunder:", ant_noy)
    print("Antall negative kunder:", ant_neg)
    
    Prosent_PosKund = (ant_pos/(ant_pos + ant_noy + ant_neg))
    Prosent_NegKund = (ant_neg/(ant_pos + ant_noy + ant_neg))
    
    print("Prosent positive kunder i uke 24:", round(Prosent_PosKund*100))
    print("Prosent negative kunder i uke 24:", round(Prosent_NegKund*100))

    NPS = (Prosent_PosKund  - Prosent_NegKund)*100

    print("NPS for uke 24:", round(NPS))

    
finn_pos_noy_neg(score)


