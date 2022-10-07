from No import No


class Solucao:
    def getChildren(self, city, road_map):
        for item in road_map:
            if (item.name == city):
                return item.transictions

    def bfs(self, city_begin, city_destiny, road_map):
        childrens = self.getChildren(city_begin, road_map)
        noBegin = No(None, city_begin, 0, childrens)
        bordaNames = [city_begin]
        borda = [noBegin]
        explorados = []
        while True:
            if (len(borda) == 0):
                return None
            no = borda[len(borda)-1]
            bordaNames.pop(len(borda)-1)
            borda.pop(len(borda)-1)
            explorados.append(no.name)
            for child in no.childrens:
                childrensChild = self.getChildren(
                    child.transiction[1], road_map)
                distance_children = child.transiction[0] + no.distance
                newChild = No(
                    no, child.transiction[1], distance_children, childrensChild)
                if ((not(newChild.name in explorados)) and (not(newChild.name in bordaNames))):
                    if(newChild.name == city_destiny):
                        self.printWay(newChild)
                        return
                    borda.append(newChild)
                    bordaNames.append(newChild.name)

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
