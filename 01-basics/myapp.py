print("Test pro první třídu základní školy\n")
jmeno = input('Zadejte svoje jméno: \n')
prijmeni = input('Zadejte svoje příjmení: \n')
vek = input('Zadejte svůj věk: \n')
detsky_vek = 10
pocet_bodu = 0
if (int(vek) >= detsky_vek):
    print("Co děláš se svým životem jestli potřebuješ počítat tyhle příklady?")
else:
    print("Jen se uč")
priklad1 = input('Kolik je 2+2: \n')
if (int(priklad1) != 4 & int(vek) < detsky_vek):
    print('Špatně, za 5, hodně štěstí do budoucna\n')
elif (int(priklad1) != 4 & int(vek) >= detsky_vek):
    print('J..Jak? Jak můžeš... udělat chybu? Tady někdo má dvouciferné IQ a já to nejsem\n')

elif (int(priklad1) == 4 & int(vek) > detsky_vek):
    print('Gratuluji zvládl jsi první příklad\n')
    pocet_bodu+=1
else:
    print('Gratuluji úspěšně byl první příklad zvládnut, možná ještě nějaké IQ máš\n')
    pocet_bodu += 1

priklad2 = input('Každopádně....další příklad je 8-1 a to se rovná?\n')
if (int(priklad2) != 7) & (int(vek) > detsky_vek):
    print('J..Jak? Jak můžeš... udělat chybu? Tady někdo má dvouciferné IQ a já to nejsem\n')
elif (int(priklad2) != 7) & (int(vek) <= detsky_vek):
    print('Špatně, za 5, hodně štěstí do budoucna\n')
elif (int(priklad2) != 7) & (int(vek) < detsky_vek & pocet_bodu < 1):
    print('Ale notak, já vím že to příště zvládneš\n')
elif (int(priklad2) != 7) & (int(vek) <= detsky_vek & pocet_bodu < 1):
    print('J..Jak? Jak můžeš... udělat chybu...Znova? I ve školce to umí\n')
elif (int(priklad2) == 7) & (int(vek) > detsky_vek):
    print('Gratuluji zvládl jsi druhý příklad\n')
    pocet_bodu += 1
else:
    print('Gratuluji úspěšně byl druhý příklad zvládnut, možná ještě nějaké IQ máš\n')
    pocet_bodu += 1

priklad3 = input('Teď něco težšího, kolik je (4x5:1)x0\n')
if (int(priklad3) != 0) & (int(vek) > detsky_vek):
    print('Potřebuješ doučování\n')
elif (int(priklad3) != 0) & (int(vek) <= detsky_vek):
    print('Ty jsi asi úplný ementál ne?\n')
elif (int(priklad3) == 0) & (int(vek) > detsky_vek):
    print('Gratuluji zvládl jsi třetí příklad\n')
    pocet_bodu += 3
else:
    print('Gratuluji úspěšně byl třetí příklad zvládnut, možná ještě nějaké IQ máš\n')
    pocet_bodu += 3

print('VYHODNOCENÍ TESTU')
znamka = 0
if(int(pocet_bodu)<=1):
    znamka = 5
elif(int(pocet_bodu)==2):
    znamka = 4
elif(int(pocet_bodu) == 3):
    znamka = 3
elif(int(pocet_bodu)== 4):
    znamka = 2
else:
    znamka = 1
print('{} {} s věkem {} získal {} bod[ů] a dostal známku {}'.format(jmeno,prijmeni,vek,pocet_bodu,znamka))
