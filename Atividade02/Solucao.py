import numpy as np
from No import No


class Solucao:
    def getChildren(self, city, road_map):
        for item in road_map:
            if (item.name == city):
                return item.transictions

    def bfs(self, city_begin, city_destiny, road_map):
        childrens = self.getChildren(city_begin, road_map)
        noBegin = No(None, city_begin, 0, childrens)
        borda = [noBegin]
        explorados = []
        while True:
            if (len(borda) == 0):
                return None
            no = borda[0]
            borda.pop(0)
            explorados.append(no.name)
            for child in no.childrens:
                childrensChild = self.getChildren(
                    child.transiction[1], road_map)
                newChild = No(
                    no, child.transiction[1], child.transiction[0], childrensChild)
                if(not(newChild.name in explorados) and not(newChild.name in explorados)):
                    if(newChild.name == city_destiny):
                        print(newChild.name)
                        break
                    borda.append(newChild)
                    # node = No(None, 0, [])
