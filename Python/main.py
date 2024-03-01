class Building:
    def __init__(self):
        self.floors = []
        self.open = False
    def isOpen(day, time):
        accepted_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
        
        if day in accepted_days and 8 <= time <= 20:
            return True
        else:
            return False
        
class Floor:
    def __init__(self):
        self.rooms = []
        
class Room:
    def __init__(self):
        self.windows = []
        self.busy = False
        self.temperature = 0
        
class Window:
    def __init__(self):
        self.open = False
        
        
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
    room1 = Room()
    room1.busy = True
    room1.temperature = 14
    
    room2 = Room()
    room2.busy = True
    room2.temperature = 25
    
    room3 = Room()
    room3.busy = False
    room3.temperature = 15
    
    #Adding windows to rooms
    room1.windows.append(window1)
    room1.windows.append(window2)
    
    #Floors creation
    floor1 = Floor()
    floor2 = Floor()
    
    #Adding rooms to floors
    floor1.rooms.append(room1)
    floor1.rooms.append(room2)
    
    floor2.rooms.append(room3)
    
    #Building creation
    building = Building()
    
    #Adding floors to buildings
    building.floors.append(floor1)
    building.floors.append(floor2)
    

    


    

           
