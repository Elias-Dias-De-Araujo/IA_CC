from Stat import Stat
from Transiction import Transiction


road_map = [
    Stat("Oradea", [Transiction([151, "Sibiu"]), Transiction([71, "Zerind"])]),
    Stat("Zerind", [Transiction([71, "Oradea"]), Transiction([75, "Arad"])]),
    # Colocar as novas cidades aqui, seguindo o padrão acima  #
]

for item in road_map:
    name = item.name
    transiction = ""
    for trans in item.transictions:
        transiction += " (" + \
            str(trans.transiction[0]) + "," + trans.transiction[1] + "),"
    print(name + " : " + transiction.rstrip(","))
