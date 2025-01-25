from library_system.application import Application
import tkinter as tk

def main():
    root = tk.Tk()
    root.title("System Biblioteczny")
    root.geometry("800x600")
    app = Application(master=root)
    app.mainloop()

if __name__ == "__main__":
    main()
