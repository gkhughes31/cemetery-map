try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk
from tkinter.font import Font
import pandas as pd

#pandas.merge(data1, data2, how, on)

df = pd.read_csv(r'C:\Users\18283\OneDrive\Desktop\Gethsemane Reference Sheet CSV.csv')



#deriving base class of tk.Frame onto My_GUI
class My_GUI(tk.Frame):
    def __init__(self, root):
        #creates an instance of the Frame class, when you create an instance of the My_GUI class
        tk.Frame.__init__(self,root)
        self.font = Font(self, "Arial 3")
        self.fontsize = 3
        self.canvas = tk.Canvas(self, width=400, height=300, background = "gray")
        self.title = root.title("Cemetery Map")
        self.xsb = tk.Scrollbar(self, orient = 'horizontal', command=self.canvas.xview)
        self.ysb = tk.Scrollbar(self, orient = 'vertical', command=self.canvas.yview)
        self.canvas.configure(scrollregion= self.canvas.bbox("all"))
        self.xsb.grid(row=1, column=0, sticky="ew")
        self.ysb.grid(row=0, column=1, sticky="ns")
        self.canvas.grid(row=0, column=0, sticky= "nsew")
        self.grid_rowconfigure(0, weight = 1)
        self.grid_columnconfigure(0, weight = 1)
        self.button = tk.Button(self, text = "Hide Garden Names/Show Plot Names", command = self.on_test_click)
        self.button.grid()
        self.spincount = 0
        self.label = tk.Label(self)
        self.label.grid()
        self.switch = True
        
        for i in df.index:
            x0, y0 = df.x1[i]*10, df.y1[i]*10 + df.height[i]*10
            x1, y1 = df.x1[i]*10 + df.width[i]*10, df.y1[i]*10
            cx = df.x1[i]*10 + df.width[i]*5
            cy = df.y1[i]*10 + df.height[i]*5
            if df.fc[i] == "!3!":
                fc = "gold"
            elif df.fc[i] == "!2!":
                fc = "green"
            elif df.fc[i] == "!1!":
                fc = "purple"
            else:
                fc = "white"
            self.canvas.create_rectangle((x0,-y0),(x1,-y1), fill = fc, width = 1, tags = f"Plot{df.PLOT[i]}")
            self.canvas.create_text(cx,-cy, text = f'{df.Map_Names[i]}\n {df.full[i]}', state = "hidden", anchor = tk.CENTER, tags = "FullDetail", width = 30, font = "Arial 7")
            if df.height[i]>=df.width[i]:
                self.create_text(cx,-cy, text = f"{df.PLOT[i]}-{df.SECTION[i]}-{df.SPACE[i]}", state = "hidden", anchor = tk.CENTER, angle =90, tags = ("Plots",f"Plot{df.PLOT[i]}"))
            else:
                self.create_text(cx,-cy, text = df.Map_Names[i], state = "hidden" ,anchor = tk.CENTER, angle =0, tags = ("Plots", f"Plot{df.PLOT[i]}"))
        
        self.canvas.create_text(300,-800, anchor=tk.CENTER, text = "PASTORAL", tags = "GardenNames", font = "Helvetica 36")
        
        
        # This is what enables scrolling with the mouse:
        self.canvas.bind("<ButtonPress-1>", self.scroll_start)
        self.canvas.bind("<B1-Motion>", self.scroll_move)
        self.canvas.bind("<MouseWheel>", self.zoom_start)
        
        #canvas.itemconfigure(id, state='hidden'/'normal')
        
        #self.canvas.itemconfigure("Plot11", state = "hidden")
        
    def create_text(self, *args, **kwargs):
        self.canvas.create_text(*args, **kwargs, font = self.font)
        
    def scroll_start(self, event):
        self.canvas.scan_mark(event.x, event.y)

    def scroll_move(self, event):
        self.canvas.scan_dragto(event.x, event.y, gain=1)
        
    def zoom_start(self, event):
        if (event.delta > 0):
            self.fontsize *= 1.1
            self.canvas.scale("all", event.x, event.y, 1.1, 1.1)
            self.spincount += 1
        elif (event.delta < 0):
            self.fontsize *= 0.9
            self.canvas.scale("all", event.x, event.y, 0.9, 0.9)
            self.spincount -= 1
        if self.spincount >= 22:
            self.canvas.itemconfigure("GardenNames", state = "hidden")
            self.canvas.itemconfigure("FullDetail", state = "normal")
            self.canvas.itemconfigure("Plots", state = "hidden")
        elif self.spincount >= 14:
            self.canvas.itemconfigure("GardenNames", state = "hidden")
            self.canvas.itemconfigure("FullDetail", state = "hidden")
            self.canvas.itemconfigure("Plots", state = "normal")
        else:
            self.canvas.itemconfigure("GardenNames", state = "normal")
            self.canvas.itemconfigure("FullDetail", state = "hidden")
            self.canvas.itemconfigure("Plots", state = "hidden")
        self.label['text'] = self.spincount
        self.font.configure(size=int(self.fontsize))
        self.canvas.configure(scrollregion = self.canvas.bbox("all"))
        
    def on_test_click(self):
        if self.switch:
            self.canvas.itemconfigure("GardenNames", state = "hidden")
            self.canvas.itemconfigure("Plots", state = "normal")
            self.switch = False
        else:
            self.canvas.itemconfigure("GardenNames", state = "normal")
            self.canvas.itemconfigure("Plots", state = "hidden")
            self.switch = True
    

        
    
  
if __name__ == "__main__":
    root = tk.Tk()
    #fill determines whether widget fills beyond it's defined dimensions
    #expand
    My_GUI(root).pack(fill="x", expand=False)
    root.mainloop()
    