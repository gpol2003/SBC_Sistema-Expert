import tkinter

class Visualization:
    def __init__(self, building):
        max_height = 750
        max_width = 500
        self.root = tkinter.Tk()

        self.root.iconbitmap("building.ico")
        self.root.title("Sistema Expert")
        self.root.config(bg="grey", width=str(max_width), height=str(max_height))

        self.frames = []
        self.canvases = []  

        for floor in building.floors:
            frame = tkinter.Frame(highlightthickness=2)
            frame.pack()
            frame.config(bg="white")
            frame.config(width=str(max_width), height=str(max_height/len(building.floors) + 1))
            self.frames.append(frame)

            canvas_planta = tkinter.Canvas(frame, bg="snow3", highlightbackground="black", highlightthickness=0, width=max_width, height=max_height/len(building.floors) + 1)
            canvas_planta.pack()
            self.canvases.append(canvas_planta)  

            num_rooms = len(floor.rooms)
            room_width = max_width / max(1, num_rooms)  # mirar si hi ha 1 hab

            for room_index, room in enumerate(floor.rooms):
                x_position = room_index * room_width
                room_color = "firebrick1" if room.busy else ""
                canvas_planta.create_rectangle(x_position, 0, x_position + room_width, max_height, fill=room_color, outline="", width=3)
                
                if room_index == 0:
                    canvas_planta.create_line(x_position, 0, x_position, max_height, fill="black", width=3)
                
                canvas_planta.create_line(x_position + room_width, 0, x_position + room_width, max_height, fill="black", width=3)
                window_width = 45 
                window_spacing = 15  

                window_size = 45 
                window_spacing = 10  
                window_y_pos = 50 

                for window_index, window in enumerate(room.windows):
                    window_color = "" if window.open else "blue"
                    window_outline = "blue" if window.open else ""
                    window_x_pos = x_position + 30 + window_index * (window_size + window_spacing)
                    canvas_planta.create_rectangle(window_x_pos, window_y_pos, window_x_pos + window_size, window_y_pos + window_size, fill=window_color, outline=window_outline)

                room_center_x = x_position + room_width / 2

                window_label_left = tkinter.Label(canvas_planta, text=room.name, bg="white", font=("Arial", 8))

                window_label_left.place(x=room_center_x, y=window_y_pos - 15, anchor="center")

                temp = str(room.temperature) + "ºC"

                window_label_right = tkinter.Label(canvas_planta, text=temp , bg="white", font=("Arial", 8))

                window_label_right.place(x=x_position + room_width - 10, y=window_y_pos - 15, anchor="e")

        # Creem la planta inferior on anirà la porta
        frame_inferior = tkinter.Frame(highlightthickness=2)
        frame_inferior.pack()
        frame_inferior.config(bg="black")
        frame_inferior.config(width=str(max_width), height=str(max_height/len(building.floors) + 1))
        self.frames.append(frame_inferior)

        # Afegim canvas al frame_inferior
        canvas_inferior = tkinter.Canvas(frame_inferior, bg="gainsboro", width=max_width, height=max_height/len(building.floors) + 1)
        canvas_inferior.pack()

        # Porta + pany
        porta_esquerra = canvas_inferior.create_rectangle(170, 50, 250, 200, fill="white")
        porta_dreta = canvas_inferior.create_rectangle(250, 50, 330, 200, fill="white")

        pany_esquerra = canvas_inferior.create_rectangle(235, 100, 245, 110, fill="blue")
        pany_dreta = canvas_inferior.create_rectangle(255, 100, 265, 110, fill="blue")

    def run(self):
        self.root.mainloop()

