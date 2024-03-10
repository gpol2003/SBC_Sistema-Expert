import tkinter
from PIL import Image, ImageTk


class Visualization:
    def __init__(self, building, day, time, weather):
        max_height = 600
        max_width = 500

        self.frames = []
        self.canvases = []
        self.imagenes = []

        self.root = tkinter.Tk()
        self.root.iconbitmap(r"Python\data\images\building.ico")
        self.root.title("Sistema Expert")

        # En funció de quin sigui el clima, el fons serà d'un color o d'un altre
        if weather == "hot":
            bg_color = "light goldenrod"
        if weather == "cold":
            bg_color = "SteelBlue2"
        if weather == "templated":
            bg_color = "light coral"

        self.root.config(bg=bg_color, width=str(max_width), height=str(max_height))

        # Afegim una etiqueta amb el dia de la setmana
        label_day = tkinter.Label(self.root, text=day, bg=bg_color, font=("Helvetica", 28), fg="white")
        label_day.place(x=30, y=60, anchor="nw")

        # Afegim una etiqueta amb l'hora actual
        time_str = str(time) + ":00 hrs"
        label_time = tkinter.Label(self.root, text=time_str, bg=bg_color, font=("Helvetica", 28), fg="white")
        label_time.place(x=30, y=110, anchor="nw")

        self.frame_building = tkinter.Frame(self.root, highlightthickness=2, bg="white")
        self.frame_building.place(relx=0.5, rely=0.5, anchor="center") 

        self.canvas_building = tkinter.Canvas(self.frame_building, bg="snow3", highlightbackground="black", highlightthickness=0, width=max_width, height=max_height)
        self.canvas_building.pack()

        for floor in building.floors:
            # Creem un frame per cada planta que té l'edifici
            frame = tkinter.Frame(self.canvas_building, highlightthickness=2, bg="white")
            frame.pack()
            # La mida de la planta, dependrà del número de plantes de l'edifici
            frame.config(width=str(max_width), height=str(max_height/len(building.floors) + 1))
            self.frames.append(frame)

            # Creem un canvas per la planta
            canvas_planta = tkinter.Canvas(frame, bg="snow3", highlightbackground="black", highlightthickness=0, width=max_width, height=max_height/len(building.floors) + 1)
            canvas_planta.pack()
            self.canvases.append(canvas_planta)

            num_rooms = len(floor.rooms)

            # La mida de la habitació depndrà del número d'habitacions que tingui la planta
            room_width = max_width / max(1, num_rooms) 

            # Iterarem per cada habitació de la planta
            for room_index, room in enumerate(floor.rooms):
                x_position = room_index * room_width
                # Su l'habitació està ocupada la pintarem de color vermellós mentre que si està lliure, no es trobarà pintada
                room_color = "brown1" if room.busy else "snow3"
                room_outline = "" if room.busy else "brown1"
                canvas_planta.create_rectangle(x_position, 0, x_position + room_width, max_height, fill=room_color, outline=room_outline, width=7)
                
                # Si l'habitació està ocupada, no tindrà marc i per contra, si està lliure, tindrà el marc de color vermellós
                if room.busy:
                    if room_index == num_rooms - 1:
                       canvas_planta.create_line(x_position, 0, x_position, max_height, fill="snow3", width=3, dash=(4, 2))
                    else:
                        canvas_planta.create_line(x_position + room_width, 0, x_position + room_width, max_height, fill="snow3", width=3, dash=(4, 2))

                else:
                    canvas_planta.create_line(x_position + room_width, 0, x_position + room_width, max_height, fill="brown1", width=3, dash=(4, 2))

                window_spacing = 15
                window_size = 55 
                window_spacing = 15  
                window_y_pos = 50 

                for window_index, window in enumerate(room.windows):
                    # Si la finestra està tencada, la pintarem de color blau. Si està oberta, tindrà el marc de color blau
                    window_color = "" if window.open else "blue"
                    window_outline = "blue" if window.open else ""
                    window_x_pos = x_position + 30 + window_index * (window_size + window_spacing)
                    canvas_planta.create_rectangle(window_x_pos, window_y_pos + 40, window_x_pos + window_size, window_y_pos + window_size + 40, fill=window_color, outline=window_outline)
                
                room_center_x = x_position + room_width / 2

                # Escriurem a la part superior central de l'habitació, el nom que té aquesta
                if room.busy:
                    label_name = tkinter.Label(canvas_planta, text=room.name, font=("Helvetica", 18), bg="brown1")
                    label_name.place(x=room_center_x, y=window_y_pos - 10, anchor="center")
                else:
                    label_name = tkinter.Label(canvas_planta, text=room.name, font=("Helvetica", 18), bg="snow3")
                    label_name.place(x=room_center_x, y=window_y_pos - 10, anchor="center")

                # La temperatura també es podrà visualitzar a la part superior dreta. 
                temp = str(room.temperature) + "ºC"

                label_temp = tkinter.Label(canvas_planta, text=temp , bg="white", font=("Helvetica", 14), background="sky blue")
                label_temp.place(x=x_position + room_width - 10, y=window_y_pos - 30, anchor="e")

                # Si l'habitació té el sistema de ventilació activat, es mostrarà una icona
                if room.ventilation:
                    imagen_ventilation = Image.open(r"Python\data\images\ventilacio.png")
                    imagen_ventilation = imagen_ventilation.resize((40, 40), Image.LANCZOS)
                    imagen_ventilation_tk = ImageTk.PhotoImage(imagen_ventilation)
                    self.imagenes.append(imagen_ventilation_tk)
                    canvas_planta.create_image(x_position + 30, window_y_pos + 150, anchor="w", image=imagen_ventilation_tk)

                # Si l'habitació te l'aire condicionat obert, es mostrarà una icona
                if room.air_conditioning:
                    imagen_aire = Image.open(r"Python\data\images\aire.png")
                    imagen_aire = imagen_aire.resize((40, 40), Image.LANCZOS)
                    imagen_aire_tk = ImageTk.PhotoImage(imagen_aire)
                    self.imagenes.append(imagen_aire_tk)
                    canvas_planta.create_image(x_position + 80, window_y_pos + 150, anchor="w", image=imagen_aire_tk)

                # Si l'habitació té la llum artificial oberta, es mostrarà una icona
                if room.artificial_light:
                    imagen_artificial = Image.open(r"Python\data\images\artificial.png")
                    imagen_artificial = imagen_artificial.resize((40, 40), Image.LANCZOS)
                    imagen_artificial_tk = ImageTk.PhotoImage(imagen_artificial)
                    self.imagenes.append(imagen_artificial_tk)
                    canvas_planta.create_image(x_position + 130, window_y_pos + 150, anchor="w", image=imagen_artificial_tk)

                # Si la calefacció es troba activada, es mostrarà una icona
                if room.heating:
                    imagen_heating = Image.open(r"Python\data\images\heating.png")
                    imagen_heating = imagen_heating.resize((40, 40), Image.LANCZOS)
                    imagen_heating_tk = ImageTk.PhotoImage(imagen_heating)
                    self.imagenes.append(imagen_heating_tk)
                    canvas_planta.create_image(x_position + 180, window_y_pos + 150, anchor="w", image=imagen_heating_tk)                         

            # Si la planta té l'alarma activada, es mostrarà una icona a l'última habitació
            if floor.alarm:
                imagen_alarm_floor = Image.open(r"Python\data\images\alarma.png")
                imagen_alarm_floor = imagen_alarm_floor.resize((50, 50), Image.LANCZOS)
                imagen_alarm_floor_tk = ImageTk.PhotoImage(imagen_alarm_floor)
                self.imagenes.append(imagen_alarm_floor_tk)
                canvas_planta.create_image(x_position + 180, window_y_pos + 220, anchor="w", image=imagen_alarm_floor_tk)     

        # Creem la planta inferior on anirà la porta
        frame_inferior = tkinter.Frame(self.canvas_building, highlightthickness=2, bg="black")
        frame_inferior.pack()
        frame_inferior.config(width=str(max_width), height=str(max_height/len(building.floors) + 1))
        self.frames.append(frame_inferior)

        canvas_inferior = tkinter.Canvas(frame_inferior, bg="snow3", width=max_width, height=max_height/len(building.floors) + 1)
        canvas_inferior.pack()

        tamany_porta = (200, 200)

        # Si l'edifici té la porta oberta, aquesta és veurà oberta
        if building.open:
            imagen_open = Image.open(r"Python\data\images\open.png")
            imagen_open = imagen_open.resize(tamany_porta, Image.LANCZOS)
            self.imagen_open = ImageTk.PhotoImage(imagen_open)
            canvas_inferior.create_image(max_width - 140, 120, anchor="ne", image=self.imagen_open)
        # Per contra, si l'edifici té la porta tancada, aquesta es mostrarà tancada
        else:
            imagen_closed = Image.open(r"Python\data\images\closed.png")
            imagen_closed = imagen_closed.resize(tamany_porta, Image.LANCZOS)
            self.imagen_closed = ImageTk.PhotoImage(imagen_closed)
            canvas_inferior.create_image(max_width - 140, 120, anchor="ne", image=self.imagen_closed)
        
        # Si l'edifici té l'alarma activada, es mostrarà una icona al costat de la porta
        if building.alarm:
            imagen_alarma = Image.open(r"Python\data\images\alarma.png")
            nuevo_tamano = (70, 70)
            imagen_alarma = imagen_alarma.resize(nuevo_tamano, Image.LANCZOS)
            self.imagen_alarma = ImageTk.PhotoImage(imagen_alarma)
            canvas_inferior.create_image(max_width - 25, 25, anchor="ne", image=self.imagen_alarma)

    def run(self):
        self.root.mainloop()
