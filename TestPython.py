from tkinter import *
from tkinter import ttk
import matplotlib.pyplot as plt
import pandas as pd


posts_sample = pd.read_csv("AnalyseData/Wuzzuf_Job_Posts_Sample.csv")
app_sample = pd.read_csv("AnalyseData/Wuzzuf_Applications_Sample.csv")

df = pd.DataFrame(posts_sample)


'''حلو..كدة
 قدرت الف على اتنين ليست 
 و اجمع العناصر اللى جواهم
  و حسبتلهم المتوسط كمان 
  ..طبقهاعلى الوظايف'''

l = [1, 2, 3, 4, 5]
k = [2, 4, 6, 8, 7]

e = []
for i in range(len(l)):
   e.append((l[i] + k[i])/2.0)












'''الفكرة هنا انه هايعرض عدد سنين الخبرة
 للوظايف اللى مرتبها اقل من رقم معين'''













root = Tk()
root.geometry("400x200")

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



def print_btn():
   myVal = df.loc[df.salary_minimum <= int(val2.get()), val1.get()]
   print(myVal)

bttn = ttk.Button(text="print", command=print_btn).grid(column=1, row=2)


root.mainloop()






#
#

'''textvariable=lstvar >>> beside 15'''
combo = ttk.Combobox(width=25)
combo['values'] = job_list
combo.grid(column=0, row=1)


btn = ttk.Button(text="ClickMe").grid(column=0, row=3)















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