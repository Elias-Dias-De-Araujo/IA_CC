from No import No


class Solucao:
    def getChildren(self, city, mapa):
        for item in mapa.road_map:
            if (item.name == city):
                return item.transictions

    def smallerCostIndex(self, borda, heuristic):
        menorCusto = []
        menorCustoOrdenado = []

        for n in borda:
            menorCusto.append(heuristic[n.name])
            menorCustoOrdenado.append(heuristic[n.name])

        menorCustoOrdenado.sort()
        indexBorda = menorCusto.index(menorCustoOrdenado[0])
        return indexBorda

    def bh(self, city_begin, city_destiny, mapa, heuristic):
        childrens = self.getChildren(city_begin, mapa)
        noBegin = No(None, city_begin, 0, childrens)
        bordaNames = [city_begin]
        borda = [noBegin]
        explorados = []

        while True:
            if (len(borda) == 0):
                return None

            indexBorda = self.smallerCostIndex(borda, heuristic)
            no = borda[indexBorda]
            bordaNames.pop(indexBorda)
            borda.pop(indexBorda)
            if(no.name == city_destiny):
                self.printWay(no)
                return
            explorados.append(no.name)
            for child in no.childrens:
                childrensChild = self.getChildren(
                    child.transiction[1], mapa)
                distance_children = child.transiction[0] + no.distance
                newChild = No(
                    no, child.transiction[1], distance_children, childrensChild)
                if ((not(newChild.name in explorados)) and (not(newChild.name in bordaNames))):
                    borda.append(newChild)
                    bordaNames.append(newChild.name)
                elif newChild.name in bordaNames:
                    index = bordaNames.index(newChild.name)
                    if newChild.distance < borda[index].distance:
                        borda[index] = newChild

    def printWay(self, No):
        way = []
        distance = No.distance
        while No != None:
            way.append(No.name)
            No = No.parent
        way.reverse()
        print("Caminho percorrido:")
        print(way)
        print("Distância percorrida:")
        print(distance)
