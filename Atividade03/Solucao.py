from No import No


class Solucao:
    def getChildren(self, city, road_map):
        for item in road_map:
            if (item.name == city):
                return item.transictions

    def bcu(self, city_begin, city_destiny, road_map):
        childrens = self.getChildren(city_begin, road_map)
        noBegin = No(None, city_begin, 0, childrens)
        bordaNames = [city_begin]
        borda = [noBegin]
        explorados = []

        while True:
            menorCusto = []
            menorCustoOrdenado = []

            if (len(borda) == 0):
                return None

            for n in borda:
                menorCusto.append(n.distance)
                menorCustoOrdenado.append(n.distance)

            menorCustoOrdenado.sort()
            indexBorda = menorCusto.index(menorCustoOrdenado[0])

            no = borda[indexBorda]
            bordaNames.pop(indexBorda)
            borda.pop(indexBorda)
            if(no.name == city_destiny):
                self.printWay(no)
                return
            explorados.append(no.name)
            for child in no.childrens:
                childrensChild = self.getChildren(
                    child.transiction[1], road_map)
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
