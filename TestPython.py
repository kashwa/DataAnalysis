from tkinter import *
import tkinter as Tk
from tkinter import ttk
# import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("TkAgg")

# from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
# from matplotlib.figure import Figure

import pandas as pd


''' HOW TO DRAW BARCHART ON TKINTER FRAME.

root = Tk.Tk()

f = Figure(figsize=(5,4), dpi=100)
ax = f.add_subplot(111)

data = (20, 35, 30, 35, 27)
index = numpy.arange(5)  # the x locations for the groups
width = .5

rects1 = ax.bar(ind, data, width)

canvas = FigureCanvasTkAgg(f, master=root)
canvas.show()
canvas.get_tk_widget().pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)

Tk.mainloop()
'''
posts_sample = pd.read_csv("AnalyseData/Wuzzuf_Job_Posts_Sample.csv")
app_sample = pd.read_csv("AnalyseData/Wuzzuf_Applications_Sample.csv")
df = pd.DataFrame(posts_sample)

# TODO: implement print in GUI for each other <3> methods
# TODO: continue working on description field.

# root = Tk.Tk()
# root.geometry("800x600")


list_of_index = [x for x in df]

root = Tk.Tk()
root.geometry("400x500")

salariesSet = set(df.ix[:, 'salary_maximum'].head())
salaries = [x for x in salariesSet]

# val1 = StringVar()
# val2 = StringVar()

# combo1 = ttk.Combobox(width=25, textvariable=val1)
# combo1.grid(column=1, row=10)
# combo1['values'] = list_of_index

# combo2 = ttk.Combobox(width=15, textvariable=val2)
# combo2.grid(column=2, row=10)
# combo2['values'] = salaries


# myVal = df.loc[df.salary_minimum <= int(val2.get()), val1.get()]
myVal = df.loc[df.salary_minimum <= 2500, 'job_title']
label = ttk.Label(text=myVal)
label.pack()

# job_Str = ', \n'.join(str(j) for j in job_list)
# salary_str = ', \n'.join(str(s) for s in min_list)


# lbl = ttk.Label(text=myVal)
# lbl.grid(column=0, row=1)


root.mainloop()

# print(job_list)
# print(mean)



#root = Tk.Tk()
#root.geometry("400x400")



'''
def open_tkframe():
   root = Tk.Tk()
   root.geometry("400x400")

   data_cities = df.ix[:, 'city'].head(15)
   siz = data_cities.value_counts()
   city_set = set(data_cities)# Convert set to List, so it can match in bar chart.
   city_list = [city for city in city_set]

   f = Figure(figsize=(5, 4), dpi=100)
   ax_subplt = f.add_subplot(111)  # l by 1 chart * 121:1by2

   data = city_list
   index = siz  # the x locations for the groups
   width = .5

   rects1 = ax_subplt.bar(index, data, width)

   canvas = FigureCanvasTkAgg(f, master=root)
   canvas.show()
   canvas.get_tk_widget().pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)
#   root.mainloop()



bttn = ttk.Button(text="print", command=open_tkframe).pack()

#root.mainloop()








''''''
list_of_index = [x for x in df]


salariesSet = set(df.ix[:, 'salary_maximum'].head())
salaries = [x for x in salariesSet]

val1 = StringVar()
val2 = StringVar()

combo1 = ttk.Combobox(width=25, textvariable = val1)
combo1.grid(column=0, row=0)
combo1['values'] = list_of_index

combo2 = ttk.Combobox(width=15, textvariable = val2)
combo2.grid(column=1, row=0)
combo2['values'] = salaries


views = df.ix[:, 'views'].head(5)
# siz = views.value_counts()

views_set = set(views)
view_list = [x for x in views_set]
'''

'''
Ok, >> List
* Pass list to the combobox.
* Try to make action to this combobox.


root = Tk()
root.geometry("400x200")

lstvar = StringVar()

combo = ttk.Combobox(width=15, textvariable=lstvar)
combo['values'] = view_list
combo.grid(column=0, row=1)


def test_combobox():
   lbl = ttk.Label(text=lstvar.get())
   lbl.grid(column=1, row=1)


btn = ttk.Button(text="ClickMe", command=test_combobox).grid(column=0, row=3)

root.mainloop()
'''