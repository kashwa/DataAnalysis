from readData import ReadCsvData
from WuzzufGui import WuzzufGui
import pandas as pd
import matplotlib.pyplot as plt

'''Class <CategoryPChart> to draw Pie chart for the first 3 categories'''


class CategoryPChart(WuzzufGui, ReadCsvData):

    df = pd.DataFrame(ReadCsvData.posts_sample)

    def category1PieChart(self):

        # search for "category" in df.
        category1 = self.df.ix[:, 'job_category1']

        '''The Count of each item => So, this can be slices'''
        siz = category1.value_counts()

        '''To make it Unique => So, this can be [Labels]'''
        cat_set = set(category1)

        plt.pie(siz, labels=cat_set, autopct='%1.1f%%')
        plt.show()

    # Draw Category-2 Pie Chart
    def category2PieChart(self):

        # search for "category 2" in df.
        category2 = self.df.ix[:, 'job_category2']

        siz = category2.value_counts()

        cat_set = set(category2)

        plt.pie(siz, labels=cat_set, autopct='%1.1f%%')
        plt.show()

    # Draw Category-3 Pie Chart
    def category3PieChart(self):

        # search for "category 2" in df.
        category3 = self.df.ix[:, 'job_category3']

        siz = category3.value_counts()

        cat_set = set(category3)

        plt.pie(siz, labels=cat_set, autopct='%1.1f%%')
        plt.show()


rt = WuzzufGui() # Draw the Ui

categPie = CategoryPChart()
category_label = rt.lbl(rt.root, text="(1) Choose Category To print its Pie Chart: ",
                        padx=10, font="sans-serif").grid(column=0, row=0)
button1 = rt.btn(rt.root, text="Category 1", padx=5, command=categPie.category1PieChart).grid(column=1, row=0)
button2 = rt.btn(rt.root, text="Category 2", padx=5, command=categPie.category2PieChart).grid(column=2, row=0)
button3 = rt.btn(rt.root, text="Category 3", padx=5, command=categPie.category3PieChart).grid(column=3, row=0)
rt.root.mainloop()
