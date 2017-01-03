from pokedex import Pokedex
from dexter import Pokedex as Dexter
dex = {}
for key in Pokedex:
    mon = Pokedex[key] 
    name = mon["species"] 
    dex[name] = {}
    poke = dex[name]
    poke["baseStats"] = mon["baseStats"]
    poke["dex"] = mon["num"] 
    poke["types"] = mon["types"]
    poke["abilities"] = []
    for a in mon["abilities"]: poke["abilities"].append(mon["abilities"][a])
    poke["weightkg"] = mon["weightkg"]

    try:
        for a in mon["otherFormes"]:
            if "mega" in a:
                poke["hasMega"] = True
    except Exception:
        continue 

f = open("fin_dex.py", "w")
f.write("Pokedex = ")
f.write(str(dex))
f.close()