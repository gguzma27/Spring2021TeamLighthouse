#Test GUI for COVID-19 results reporting
#Created by Glenn Guzman-Rockett
#Date: 03/21/2021
#Revision date: 03/21/2021


from tkinter import *
import sys
class Application(Tk):
    def __init__(self):
        Tk.__init__(self)
        self._frame = None
        self.switch_frame(StartPage)
    def switch_frame(self, frame_class):
        """Destroys current frame and replaces it with a new one."""
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack(expand=True, fill="both")
#This is the starting page
class StartPage(Frame):
    def __init__(self, root):
        Frame.__init__(self, root)
        label_1 = Label(self,text="I exist", font=('Courier', 30))
        label_1.grid(row=0, column=1)
        label_2 = Label(self, text="Pick a way to play", font=('Courier', 15))
        label_2.grid(row=1, column=1)
        button_1 = Button(self, text="New Game", fg='black', bg='green', width=25, command=lambda: root.switch_frame(PlayerInfo))
        button_1.grid(row=1, column=0)
        button_2 = Button(self, text="Load Game", fg='black', bg='yellow', width=25, command=lambda: root.switch_frame(LoadGame))
        button_2.grid(row=1, column=2)
        button_3 = Button(self, text='Exit Game', fg='black', bg='red', width=25, command=lambda: sys.exit())
        button_3.grid(row=2, column=1)
        label_3 = Label(self, text='')
        label_3.grid(row=1, column=1)
        label_4 = Label(self, text='')
        label_4.grid(row=2, column=0)
        label_5 = Label(self, text='')
        label_5.grid(row=2, column=2)
#Here is the configuring problem
        self.grid_columnconfigure(0,weight=1)
        self.grid_columnconfigure(1,weight=1)
        self.grid_columnconfigure(2,weight=1)
        self.grid_columnconfigure(3,weight=1)
        self.grid_rowconfigure(3, weight=1)
        self.grid_rowconfigure(0,weight=1)
        self.grid_rowconfigure(1,weight=1)
        self.grid_rowconfigure(2,weight=1)
class PlayerInfo(Frame):
    def __init__(self, root):
        Frame.__init__(self, root)
        Label(self, text='Game will start').pack(expand=True, fill="both")
class LoadGame(Frame):
    def __init__(self, root):
        Frame.__init__(self, root)
        Label(self, text='Load old game').pack(expand=True, fill="both")
#Run it
if __name__ == "__main__":
    app = Application()
    app.mainloop()
