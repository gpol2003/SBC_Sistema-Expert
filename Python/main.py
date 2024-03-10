#CLASSES
import json
from interface import Visualization
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
def loadJson(filename):
    #Load data
    try:
        with open('Python/data/'+ filename + ".json") as f:
            data = json.load(f)
            building = Building()
            for floor in data["building"]["floors"]:
                new_floor = Floor(floor["name"])
                for room in floor["rooms"]:
                    new_room = Room(room["name"])
                    new_room.busy = room["busy"]
                    new_room.temperature = room["temperature"]
                    for window in room["windows"]:
                        new_window = Window(window["name"])
                        new_window.open = window["open"]
                        new_room.windows.append(new_window)
                    new_floor.rooms.append(new_room)
                building.floors.append(new_floor)
            f.close()
            return False, data["day"], data["time"], classifyTemperature(data["temperature"]), building
    except FileNotFoundError:
        return True, "", 0, "", None

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
                

#MAIN PROGRAM 
if __name__ == "__main__":
    file = input("Enter json filename (without .json): ")
    #Building structure creation
    err, day, time, weather, building = loadJson(file)
    if err:
        print("Invalid file!")
    else:
        printResult(building, day , time, weather)
        v = Visualization(building, day, time, weather)
        v.run()
        
        

    


    

           
