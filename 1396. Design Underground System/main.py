class UndergroundSystem:

    def __init__(self):
        self.checkin_lst = []
        self.final_lst = []

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        table = {"id" : id , "stationname":stationName , "t":t}
        self.checkin_lst.append(table)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        for i in self.checkin_lst:
            if i["id"] == id:
                table = {"checkIn":i["stationname"],"checkOut":stationName , "t":t-i["t"]}
                self.final_lst.append(table)
                self.checkin_lst.remove(i)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        time = []
        for i in self.final_lst:
            if startStation == i["checkIn"] and endStation == i["checkOut"]:
                time.append(i["t"])

        avarage = sum(time) / len(time)
        return avarage
