from Estado import Estado
from Transicao import Transicao
from Mapa import Mapa
from Solucao import Solucao

road_map = [
    Estado("Oradea", [Transicao([151, "Sibiu"]),
           Transicao([71, "Zerind"])]),
    Estado("Zerind", [Transicao([71, "Oradea"]), Transicao([75, "Arad"])]),
    Estado("Arad", [Transicao([75, "Zerind"]), Transicao(
        [140, "Sibiu"]), Transicao([118, "Timisoara"])]),
    Estado("Timisoara", [Transicao([118, "Arad"]),
                         Transicao([111, "Lugoj"])]),
    Estado("Lugoj", [Transicao([111, "Timisoara"]),
                     Transicao([70, "Mehadin"])]),
    Estado("Mehadin", [Transicao([70, "Lugoj"]),
                       Transicao([75, "Drobeta"])]),
    Estado("Drobeta", [Transicao([75, "Mehadin"]),
                       Transicao([120, "Craiova"])]),
    Estado("Sibin", [Transicao([151, "Oraden"]), Transicao([140, "Arad"]), Transicao(
        [99, "Fagaras"]), Transicao([80, "Rimnicu Vielcea"])]),
    Estado("Rimnicu Vilcea", [Transicao([80, "Sibin"]), Transicao(
        [97, "Pitesti"]), Transicao([146, "Craiova"])]),
    Estado("Craiova", [Transicao([146, "Rimnicu Vilcea"]), Transicao(
        [138, "Pitesti"]), Transicao([120, "Drobeta"])]),
    Estado("Fagaras", [Transicao([99, "Sibiu"]),
                       Transicao([211, "Bucharest"])]),
    Estado("Pitesti", [Transicao([97, "Rimnicu Vilcea"]), Transicao(
        [101, "Bucharest"]), Transicao([138, "Craiova"])]),
    Estado("Bucharest", [Transicao([211, "Fagaras"]), Transicao(
        [101, "Pitesti"]), Transicao([90, "Giurgiu"]), Transicao([85, "Urziceni"])]),
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

solucao = Solucao()

solucao.bfs("Arad", "Bucharest", road_map)
