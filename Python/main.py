#CLASSES
class Building:
    def __init__(self):
        self.floors = []
        self.open = False
        self.alarm = False
        
    def checkOpen(self, day = "", time = 0):
        accepted_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
        self.open = day in accepted_days and 8 <= time <= 20
        
    def checkAlarm(self):
        for floor in self.floors:
            for room in floor.rooms:
                if room.busy:
                    self.alarm = not self.open
        
        
class Floor:
    def __init__(self, name = "floor"):
        self.rooms = []
        self.name = name
        self.alarm = False
        
    def checkAlarm(self, building_open = False):
        for room in self.rooms:
            for window in room.windows:
                if window.open:
                    self.alarm = not building_open
        
        
class Room:
    def __init__(self, name):
        self.windows = []
        self.name = name
        self.busy = False
        self.temperature = 0
        self.weather = ""
        self.natural_light = False
        self.artificial_light = False
        self.ventilation = False
        self.air_conditioning = False
        self.heating = False
        
    def checkNaturalLight(self, time):
        self.natural_light = len(self.windows) > 0 and 9 <= time <= 16
    
    def checkArtificialLight(self, building_open):
        self.artificial_light = building_open and self.busy and not self.natural_light
        
    def checkVentilation(self, building_open, weather):
        self.ventilation = building_open and self.busy and (len(self.windows) == 0 or weather != "templated")
    
    def checkAirConditioning(self, building_open, weather):
        self.air_conditioning = building_open and self.busy and weather == "hot" and self.temperature > 27
    
    def checkHeating(self, building_open, weather):
        self.heating = building_open and self.busy and weather == "cold" and self.temperature < 19
        
        
        
class Window:
    def __init__(self):
        self.open = False
        

#AUXILIAR FUNCTIONS
def transformBoolean(b):
    if b == True:
        return "on"
    return "off"

def classifyTemperature(temperature):
    if temperature <= 17:
        return "cold"
    elif 17 < temperature < 31:
        return "templated"
    elif temperature >= 31:
        return "hot"

def printResult(building, day, time, weather):
    #Checking conditions
    building.checkOpen(day, time)
    building.checkAlarm()
    
    for floor in building.floors:
        floor.checkAlarm(building.open)
        for room in floor.rooms:
            room.checkNaturalLight(time)
            room.checkArtificialLight(building.open)
            room.checkVentilation(building.open, weather)
            room.checkAirConditioning(building.open, weather)
            room.checkHeating(building.open, weather)

    #Printing building status
    print("Building status:")
    
    for floor in building.floors:
        for room in floor.rooms:
            print(room.name, ":")
            print ("\t- Artificial light: ", transformBoolean(room.artificial_light))
            print ("\t- Ventilation ", transformBoolean(room.ventilation))
            print ("\t- Air conditioning: ", transformBoolean(room.air_conditioning))
            print ("\t- Heating: ", transformBoolean(room.heating))

    for floor in building.floors:
        print(floor.name, ":")
        print("\t- Floor alarm: ", transformBoolean(floor.alarm))
        
    print("Building alarm:")
    print("\tBuilding alarm:", transformBoolean(building.alarm))
    
#TESTS   
def test1():
    day = "Monday"
    time = 10
    temperature = 23
    
    #Windows creation
    window1 = Window()
    window1.open = True
    
    window2 = Window()
    window2.open = False
    
    #Rooms creation
    room1 = Room("room1")
    room1.busy = True
    room1.temperature = 14
    
    room2 = Room("room2")
    room2.busy = True
    room2.temperature = 25
    
    room3 = Room("room3")
    room3.busy = False
    room3.temperature = 15
    
    #Adding windows to rooms
    room1.windows.append(window1)
    room1.windows.append(window2)
    
    #Floors creation
    floor1 = Floor("floor1")
    floor2 = Floor("floor2")
    
    #Adding rooms to floors
    floor1.rooms.append(room1)
    floor1.rooms.append(room2)
    
    floor2.rooms.append(room3)
    
    #Building creation
    building = Building()
    
    #Adding floors to buildings
    building.floors.append(floor1)
    building.floors.append(floor2)
    
    return building, day, time, classifyTemperature(temperature)
    
def test2():
    day = "Monday"
    time = 10
    temperature = 12
    
    #Windows creation
    window1 = Window()
    window1.open = True
    
    window2 = Window()
    window2.open = False
    
    #Rooms creation
    room1 = Room("room1")
    room1.busy = True
    room1.temperature = 14
    
    room2 = Room("room2")
    room2.busy = True
    room2.temperature = 25
    
    room3 = Room("room3")
    room3.busy = False
    room3.temperature = 15
    
    #Adding windows to rooms
    room1.windows.append(window1)
    room1.windows.append(window2)
    
    #Floors creation
    floor1 = Floor("floor1")
    floor2 = Floor("floor2")
    
    #Adding rooms to floors
    floor1.rooms.append(room1)
    floor1.rooms.append(room2)
    
    floor2.rooms.append(room3)
    
    #Building creation
    building = Building()
    
    #Adding floors to buildings
    building.floors.append(floor1)
    building.floors.append(floor2)
    
    return building, day, time, classifyTemperature(temperature)

def test3():
    day = "Monday"
    time = 22
    temperature = 12
    
    #Windows creation
    window1 = Window()
    window1.open = True
    
    window2 = Window()
    window2.open = False
    
    #Rooms creation
    room1 = Room("room1")
    room1.busy = True
    room1.temperature = 14
    
    room2 = Room("room2")
    room2.busy = True
    room2.temperature = 25
    
    room3 = Room("room3")
    room3.busy = False
    room3.temperature = 15
    
    #Adding windows to rooms
    room1.windows.append(window1)
    room1.windows.append(window2)
    
    #Floors creation
    floor1 = Floor("floor1")
    floor2 = Floor("floor2")
    
    #Adding rooms to floors
    floor1.rooms.append(room1)
    floor1.rooms.append(room2)
    
    floor2.rooms.append(room3)
    
    #Building creation
    building = Building()
    
    #Adding floors to buildings
    building.floors.append(floor1)
    building.floors.append(floor2)
    
    return building, day, time, classifyTemperature(temperature)

#MAIN PROGRAM 
if __name__ == "__main__":
    print("TEST 1:\n")
    building, day, time, weather = test1()
    printResult(building, day, time, weather)
    
    print("\nTEST 2:\n")
    building, day, time, weather = test2()
    printResult(building, day, time, weather)
    
    print("\nTEST 3:\n")
    building, day, time, weather = test3()
    printResult(building, day, time, weather)

    


    

           
