from Estado import Estado
from Transicao import Transicao
from Mapa import Mapa

road_map = [
    Estado("Oradea", [Transicao([151, "Sibiu"]),
           Transicao([71, "Zerind"])]),
    Estado("Zerind", [Transicao([71, "Oradea"]), Transicao([75, "Arad"])]),
    Estado("Arad", [Transicao([75, "Zerind"]), Transicao(
        [140, "Sibiu"]), Transicao([118, "Timisoara"])]),
    Estado("Timisoara", [Transicao([118, "Arad"]),
                         Transicao([111, "Lugoj"])]),
    Estado("Lugoj", [Transicao([111, "Timisoara"]),
                     Transicao([70, "Mehadia"])]),
    Estado("Mehadia", [Transicao([70, "Lugoj"]),
                       Transicao([75, "Drobeta"])]),
    Estado("Drobeta", [Transicao([75, "Mehadia"]),
                       Transicao([120, "Craiova"])]),
    Estado("Sibiu", [Transicao([151, "Oradea"]), Transicao([140, "Arad"]), Transicao(
        [99, "Fagaras"]), Transicao([80, "Rimnicu Vilcea"])]),
    Estado("Rimnicu Vilcea", [Transicao([80, "Sibiu"]), Transicao(
        [97, "Pitest"]), Transicao([146, "Craiova"])]),
    Estado("Craiova", [Transicao([146, "Rimnicu Vilcea"]), Transicao(
        [138, "Pitest"]), Transicao([120, "Drobeta"])]),
    Estado("Fagaras", [Transicao([99, "Sibiu"]),
                       Transicao([211, "Bucharest"])]),
    Estado("Pitest", [Transicao([97, "Rimnicu Vilcea"]), Transicao(
        [101, "Bucharest"]), Transicao([138, "Craiova"])]),
    Estado("Bucharest", [Transicao([211, "Fagaras"]), Transicao(
        [101, "Pitest"]), Transicao([90, "Giurgiu"]), Transicao([85, "Urziceni"])]),
    Estado("Girgiu", [Transicao([90, "Bucharest"])]),
    Estado("Urziceni", [Transicao([98, "Hirsova"]), Transicao(
        [142, "Vaslui"]), Transicao([85, "Bucharest"])]),
    Estado("Hirsova", [Transicao([98, "Urziceni"]),
                       Transicao([86, "Efroie"])]),
    Estado("Vaslui", [Transicao([142, "Urziceni"]),
                      Transicao([92, "Iasi"])]),
    Estado("Iasi", [Transicao([92, "Vaslui"]), Transicao([87, "Neamt"])]),
    Estado("Eforie", [Transicao([86, "Hirsova"])]),
    Estado("Neamt", [Transicao([87, "Iasi"])])
]

mapa = Mapa(road_map)
mapa.printRoadMap()
