import physics
import math

EARTH_GRAVITY = 9.8 #? normální pozemské tíhové zrychlení
MOON_GRAVITY = 1.62 #? měsíční gravitace
SPEED_OF_LIGHT = 300000  #? rychlost světla ve vakuu
SPEED_OF_SOUND = 343 #? rychlost zvuku při teplotě 20 °C v suchém vzduchu

altitude = 70

vzdalenost = 150000000
cas = vzdalenost//SPEED_OF_LIGHT
minuty = round(cas/60)
sekundy = cas%60

vteriny = 4
metry = vteriny*SPEED_OF_SOUND

physics.zeme(math.sqrt(2*EARTH_GRAVITY*altitude))
physics.mesic(math.sqrt(2*MOON_GRAVITY*altitude))
physics.svetlo(cas,minuty,sekundy)
physics.zvuk(vteriny*SPEED_OF_SOUND)