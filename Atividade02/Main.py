from Stat import Stat
from Transiction import Transiction


road_map = [
    Stat("Oradea", [Transiction([151, "Sibiu"]), Transiction([71, "Zerind"])]),
    Stat("Zerind", [Transiction([71, "Oradea"]), Transiction([75, "Arad"])]),
    Stat("Arad", [Transiction([75, "Zerind"]), Transiction(
        [140, "Sibiu"]), Transiction([118, "Timisoara"])]),
    Stat("Timisoara", [Transiction([118, "Arad"]),
         Transiction([111, "Lugoj"])]),
    Stat("Lugoj", [Transiction([111, "Timisoara"]),
         Transiction([70, "Mehadin"])]),
    Stat("Mehadin", [Transiction([70, "Lugoj"]),
         Transiction([75, "Drobeta"])]),
    Stat("Drobeta", [Transiction([75, "Mehadin"]),
         Transiction([120, "Craiova"])]),
    Stat("Sibin", [Transiction([151, "Oraden"]), Transiction([140, "Arad"]), Transiction(
        [99, "Fagaras"]), Transiction([80, "Rimnicu Vielcea"])]),
    Stat("Rimnicu Vilcea", [Transiction([80, "Sibin"]), Transiction(
        [97, "Pitesti"]), Transiction([146, "Craiova"])]),
    Stat("Craiova", [Transiction([146, "Rimnicu Vilcea"]), Transiction(
        [138, "Pitesti"]), Transiction([120, "Drobeta"])]),
    Stat("Fagaras", [Transiction([99, "Sibiu"]),
         Transiction([211, "Bucharest"])]),
    Stat("Pitesti", [Transiction([97, "Rimnicu Vilcea"]), Transiction(
        [101, "Bucharest"]), Transiction([138, "Craiova"])]),
    Stat("Bucharest", [Transiction([211, "Fagaras"]), Transiction(
        [101, "Pitesti"]), Transiction([90, "Giurgiu"]), Transiction([85, "Urziceni"])]),
    Stat("Girgiu", [Transiction([90, "Bucharest"])]),
    Stat("Urziceni", [Transiction([98, "Hirsova"]), Transiction(
        [142, "Vaslui"]), Transiction([85, "Bucharest"])]),
    Stat("Hirsova", [Transiction([98, "Urziceni"]),
         Transiction([86, "Efroie"])]),
    Stat("Vaslui", [Transiction([142, "Urziceni"]),
         Transiction([92, "Iasi"])]),
    Stat("Iasi", [Transiction([92, "Vaslui"]), Transiction([87, "Neamt"])]),
    Stat("Eforie", [Transiction([86, "Hirsova"])]),
    Stat("Neamt", [Transiction([87, "Iasi"])])
]

for item in road_map:
    name = item.name
    transiction = ""
    for trans in item.transictions:
        transiction += " (" + \
            str(trans.transiction[0]) + "," + trans.transiction[1] + "),"
    print(name + " : " + transiction.rstrip(","))
