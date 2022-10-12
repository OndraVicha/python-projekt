'''
Konstanty v Pythonu

Konstanta je vlastně speciální typ proměnné, jejíž hodnota nemůže být změněna.
V Pythonu jsou konstanty obvykle deklarovány a přiřazovány v modulu, který bývá importován do souboru aplikace.
Konstanty jsou pojmenovány velkými písmeny a jednotlivá slova jsou oddělována podtržítky.
'''

import math

def zeme(pad):
    print("Těleso bylo vyhozeno z výšky 70 metrů na Zemi. Na zem dopadne rychlostí %4.2f metrů za sekundu"%pad)
def mesic(pad2):
    print("Těleso bylo vyhozeno z výšky 70 metrů na Měsíci. Na zem dopadne rychlostí %4.2f metrů za sekundu"%pad2)
def svetlo(cas,minuty,sekundy):
    print("Sluneční paprsky dopadnou na Zemi za {} sekund to je {} minut a {} sekund".format(cas,minuty,sekundy))
def zvuk(metry):
    print("Blesk který jsme slyšeli 4 vteřiny po tom co jsme jej uviděli je vzdálen %d metrů"%metry)
''' 
Úkol:
1. Doplňte správně hodnoty uvedených konstant.
2. Doplňte physics.py o několik výpočtových funkcí (opatřené docstrings), v nichž využijete minimálně všechny výše uvedené konstanty.
Samozřejmě můžete své řešení rozšířit i o jiné fyzikální konstanty.
3. Vytvořte z tohoto souboru samostatný modul v Pythonu podle návodu, který si sami najdete na internetu.      
4. Vytvořte vlastní aplikaci myapp.py, do níž tento modul importujte. Demonstrujte v ní na jednoduchých příkladech využití vámi
připravených funkcí.  
'''