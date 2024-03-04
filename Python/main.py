#CLASSES
import json

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
    def __init__(self, name):
        self.open = False
        self.name = name
        

#AUXILIAR FUNCTIONS
def loadJson():
    #Load data
    f = open('Python/building_structure.json')
    data = json.load(f)
    
    building = Building()
    
    for floor in data["floors"]:
        new_floor = Floor(floor["name"])
        for room in floor["rooms"]:
            new_room = Room(room["name"])
            for window in room["windows"]:
                new_window = Window(window["name"])
                new_room.windows.append(new_window)
            new_floor.rooms.append(new_room)
        building.floors.append(new_floor)
        
    f.close()
    return building

def transformBoolean(b):
    if b:
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

def debugBuilding(building):
    for floor in building.floors:
        print(floor.name, floor.alarm)
        for room in floor.rooms:
            print(room.name, 
                  room.busy,
                  room.temperature,
                  room.natural_light, 
                  room.artificial_light,
                  room.ventilation,
                  room.air_conditioning,
                  room.heating)
            for window in room.windows:
                print(window.name, window.open)
                
#TESTS   
def test1(building):
    day = "Monday"
    time = 10
    temperature = 23

    #FLOOR 1
    #Windows conditions setting
    building.floors[0].rooms[0].windows[0].open = True

    building.floors[0].rooms[0].windows[1].open = False
    
    #Rooms conditions setting
    building.floors[0].rooms[0].busy = True
    building.floors[0].rooms[0].temperature = 14
    
    building.floors[0].rooms[1].busy = True
    building.floors[0].rooms[1].temperature = 25
    
    #FLOOR 2
    #Windows conditions setting
    building.floors[1].rooms[0].busy = False
    building.floors[1].rooms[0].temperature = 15    
    
    return day, time, classifyTemperature(temperature)
    
def test2(building):
    day = "Monday"
    time = 10
    temperature = 12

    #FLOOR 1
    #Windows conditions setting
    building.floors[0].rooms[0].windows[0].open = True

    building.floors[0].rooms[0].windows[1].open = False
    
    #Rooms conditions setting
    building.floors[0].rooms[0].busy = True
    building.floors[0].rooms[0].temperature = 14
    
    building.floors[0].rooms[1].busy = True
    building.floors[0].rooms[1].temperature = 25
    
    #FLOOR 2
    #Windows conditions setting
    building.floors[1].rooms[0].busy = False
    building.floors[1].rooms[0].temperature = 15    
    
    return day, time, classifyTemperature(temperature)

def test3(building):
    day = "Monday"
    time = 22
    temperature = 12

    #FLOOR 1
    #Windows conditions setting
    building.floors[0].rooms[0].windows[0].open = True

    building.floors[0].rooms[0].windows[1].open = False
    
    #Rooms conditions setting
    building.floors[0].rooms[0].busy = True
    building.floors[0].rooms[0].temperature = 14
    
    building.floors[0].rooms[1].busy = True
    building.floors[0].rooms[1].temperature = 25
    
    #FLOOR 2
    #Windows conditions setting
    building.floors[1].rooms[0].busy = False
    building.floors[1].rooms[0].temperature = 15    
    
    return day, time, classifyTemperature(temperature)

#MAIN PROGRAM 
if __name__ == "__main__":
    #Building structure creation
    building = loadJson()
    print("TEST 1:\n")
    day, time, weather = test1(building)
    printResult(building, day, time, weather)
    
    
    print("\nTEST 2:\n")
    day, time, weather = test2(building)
    printResult(building, day, time, weather)
    
    print("\nTEST 3:\n")
    day, time, weather = test3(building)
    printResult(building, day, time, weather)

    


    

           
