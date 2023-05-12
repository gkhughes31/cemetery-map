import pandas as pd

import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.textpath import TextPath
from matplotlib.patches import PathPatch


plt.rcParams['figure.autolayout'] = True
fig = plt.figure(figsize = (16,9), dpi = 100)



#Subplot by rows, column, indexes
# fig is "actual canvas" ax is subplot name
ax = fig.add_subplot(111)

df = pd.read_csv(r'C:\Users\18283\OneDrive\Desktop\Gethsemane Reference Sheet CSV.csv')

# this is a new comment

def plot_rectangle(anchor1, anchor2, width, height, fc):
    #Plots a single rectangle#
    rectangle = plt.Rectangle((anchor1, anchor2), width, height, fc= fc , ec= 'black')
    plt.gca().add_patch(rectangle)
    
def text_rectangle(anchor1, anchor2, label, size, width, height):
    tp = TextPath((anchor1, anchor2), str(label), size = size)
    pp1 = PathPatch(tp, color = "black")
    rot1 = mpl.transforms.Affine2D().rotate_deg_around(anchor1, anchor2, 90)
    translat1 = mpl.transforms.Affine2D().translate(.5,0)
    rottra = rot1 + translat1 + ax.transData
    if height >= width:
        pp1.set_transform(rottra)
        ax.add_patch(pp1)
    else:
        ax.add_patch(pp1)
    
for i in df.index:
    if df.fc[i] == "!3!":
        fc = "gold"
    elif df.fc[i] == "!2!":
        fc = "green"
    elif df.fc[i] == "!1!":
        fc = "purple"
    else:
        fc = "white"
    plot_rectangle(df.x1[i], df.y1[i], df.width[i], df.height[i], fc)
    text_rectangle(df.x1[i], df.y1[i], df.Map_Names[i], 0.5, df.width[i], df.height[i])
plt.axis('equal')
ax.set_axis_off()
ax.set_aspect('equal')
plt.show()