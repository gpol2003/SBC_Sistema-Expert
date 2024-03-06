import tkinter

class Visualization:
    def __init__(self, bulding):
        self.root=tkinter.Tk()

        self.root.iconbitmap("building.ico")
        self.root.title("Sistema Expert")
        self.root.config(bg="grey")

        

        frames = []

        frame1=tkinter.Frame()
        frame2=tkinter.Frame()
        frame3=tkinter.Frame()

        frame1.pack()
        frame1.config(bg="white")
        frame1.config(width="650", height="350")

        frame2.pack()
        frame2.config(bg="yellow")
        frame2.config(width="650", height="350")

        frame3.pack()
        frame3.config(bg="blue")
        frame3.config(width="650", height="350")

    def run(self):
        self.root.mainloop()
