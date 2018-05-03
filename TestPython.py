from tkinter import *
from tkinter import ttk
import matplotlib.pyplot as plt
import pandas as pd


posts_sample = pd.read_csv("AnalyseData/Wuzzuf_Job_Posts_Sample.csv")
app_sample = pd.read_csv("AnalyseData/Wuzzuf_Applications_Sample.csv")

df = pd.DataFrame(posts_sample)

root = Tk()
root.geometry("400x200")
#x = df.loc[df.job_title == 'Sales & Marketing Agent', df.job_description]

jobTitles = df.ix[:, 'job_title'].head(5)
# siz = views.value_counts()

jobTitles_set = set(jobTitles)
jobTitles_list = [x for x in jobTitles_set]



x = df.loc[df.job_title == 'Sales & Marketing Agent', 'job_description']

val = StringVar()
combo = ttk.Combobox(width=25, textvariable = val)
combo.grid(column=0, row=0)
combo['values'] = jobTitles_list


def print_btn():
   myVal = df.loc[df.job_title == val.get(), :]
   print(myVal)


bttn = ttk.Button(text="print", command=print_btn).grid(column=1, row=2)

root.mainloop()








'''Those 2 will be in combo box'''
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








#






#
#

'''textvariable=lstvar >>> beside 15'''
#combo = ttk.Combobox(width=25)
#combo['values'] = job_list
#combo.grid(column=0, row=1)


#btn = ttk.Button(text="ClickMe").grid(column=0, row=3)















views = df.ix[:, 'views'].head(5)
# siz = views.value_counts()

views_set = set(views)
view_list = [x for x in views_set]
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