from tkinter import *

class Elwiwi:
    def __init__(self, master):
        self.master = master
        master.title("Elwiwi")

        self.label = Label(master, text="Elwiwi GUI")
        self.label.pack()

        self.greet_button = Button(master, text="Greet", command=self.greet)
        self.greet_button.pack()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()

        self.wiwi_image = PhotoImage(file="assets/wiwi.png")
        self.wiwi_label = Label(master, image=self.wiwi_image)
        self.wiwi_label.pack()


    def greet(self):
        print("Greetings from Elwiwi!")

root = Tk()
elwiwi_gui = Elwiwi(root)
root.mainloop()