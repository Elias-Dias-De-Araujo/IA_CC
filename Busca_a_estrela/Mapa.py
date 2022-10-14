class Mapa:
    def __init__(self, road_map):
        self.road_map = road_map

    def printRoadMap(self):
        for item in self.road_map:
            name = item.name
            transiction = ""
            for trans in item.transictions:
                transiction += " (" + \
                    str(trans.transiction[0]) + "," + \
                    trans.transiction[1] + "),"
            print(name + " : " + transiction.rstrip(","))
