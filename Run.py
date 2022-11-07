import tkinter as tk
import My
import GUI

win1 = tk.Tk()
My = My.GUI(win1)
My.pack(fill="both", expand=True)

win2 = tk.Toplevel(win1)
GUI = GUI.GUI(win2)
GUI.pack(fill="both", expand=True)

tk.mainloop()