"""
Oppg.1
Et enkelt program som regner ut hvor gammel en person blir i løpet av år 2024
og skriver svaret til skjerm med passende tekst 
"""

alder = int(input("Hvilket år er du født?"))
Faktisk = 2024 - alder 
print(f"Du fyller {Faktisk} år i løpet av 2024")


"""
oppgave 1. alternativ løsning 
"""

alder = int(input("Hvilket år er du født?"))
print("Gratulerer! Du fyller",2024 - alder, "år i løpet av 2024")
print("og i 2025 vil du forhåpentligvis fylle",2025 - alder,"år")

"""
oppgave 2. Klassefest. Hvor mange pizzaer trenger vi?
"""

antall_elever = int(input('Skriv inn antall elever:'))
antall_pizza = antall_elever*1/4
import math
antall_pizza = math.ceil(antall_pizza)
print("Du bør kjøpe inn minimum", antall_pizza,"stykk pizza til klassefesten")

"""
Oppgave 2. alt.versjon som  runder av til heltall ved hjelp av int og sørger for å kjøpe nok
pizza ved å legge til desimalene 0.9999. Fordi int() alltid runder NED til
til nærmeste tall må vi bruke såpass høye desimaler
"""

antall_elever = int(input('Skriv inn antall elever:'))
antall_pizza = int(antall_elever*1/4 + 0.5)
print("Du bør kjøpe inn minimum", antall_pizza,"stykk pizza til klassefesten")

"""
Oppgave 3. Lag et program med en funksjon som regner
om fra grader til radianer (her glemte jeg å faktisk bruke funksjon..)
"""

import numpy as np
v_grad = float(input("skriv inn gradtallet:"))
v_rad = v_grad*np.pi/180
print(v_grad,"grader tilsvarer",v_rad,"radianer")

"""
Oppgave 4 a,b og c. Her slet jeg veldig med b og c oppgaven og måtte jeg bruke KI for å lære om tuple unpacking
da jeg ikke forstod hvordan man skulle bruke dictionaryen når det var flere verdier per nøkkel! Skjønner heller ikke 
om jeg faktisk utvider dictonaryen med denne. Kan dere dele utdrag fra læreboken i canvas om bruk av dictionary? (tror det er rundt side 90)
"""
""" 4a) opprett dictionary"""

Data = { 
    "Norge": ["Oslo", 0.634],
    "England": ["London", 8.982],
    "Frankrike": ["Paris", 2.161],
    "Italia": ["Roma", 2.873]
}

""" 4b) Et program som fir hovedstad og antall inbyggere """
land = input("Skriv inn et land, husk stor forbokstav: ")

# Bruker tuple unpacking for å hente ut hovedstad og innbyggertall
if land in Data:
    hovedstad, innbyggere = Data[land]
    print(f"{hovedstad} er hovedstaden i {land} og det er {innbyggere} mill. innbyggere i {hovedstad}")
else: 
    print(f"Beklager, jeg kjenner ikke igjen landet du skrev inn. Kan du ha glemt å bruke stor forbokstav?")
    
    """4c) Spør bruker om de vil legge til informasjon om det ukjente landet"""
    
    svar = input(f"Vil du legge til informasjon om {land}? (ja/nei/ok): ")

    if svar != "nei":
        hovedstad = input(f"Skriv inn hovedstaden i {land}: ")
        innbyggere = float(input(f"Skriv inn antall innbyggere i {hovedstad} i millioner: "))    
        
        # Legg til det nye landet i dictionaryen
        Data[land] = [hovedstad, innbyggere]
        print(f"{land} er nå lagt til i databasen.")
    else:
        print(f"{land} ble ikke lagt til i databasen.")

print(Data.values())
print(Data.keys())

"""
oppgave 5.
"""
import numpy as np

def areal_og_omkrets(a, b):
    # beregning av areal
    Areal_figur = ((np.pi*a**2) + b*a)/2 
    
    # beregnig av omkrets (hvor vi må trekke fra den ene kortsiden/radius sirkel)
    Omkrets_figur = (np.pi*a)+np.sqrt(a**2+b**2)+b
    
    return Areal_figur, Omkrets_figur

# be brukeren om å oppgi verdiene a og b i konsoll
a = float(input("hva er lengden på kortsiden av trekanten, eller sirkelen sin radius? :"))
b = float(input("hva er lengden på langsiden av trekanten? :"))

areal, omkrets = areal_og_omkrets(a, b)

# skriv ut resultatene til konsoll
print(f"Figurens totale areal er: {areal:.3f}")
print(f"figurens totale omkrets er: {omkrets:.3f}")

"""
Oppgave 6) skriv en kode som plotter funksjonen
f(x)=-x**2-5 for intervallet [-10,10]
"""

import numpy as np
import matplotlib.pyplot as plt

def lin_fun(x, a=5) :
    y = -x**2 - a
    return y 

x = np.linspace(-10, 10, 200)

y = lin_fun(x)

plt.plot(x, y)
plt.show()
