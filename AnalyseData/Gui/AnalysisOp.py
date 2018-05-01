from readData import ReadCsvData
from WuzzufGui import WuzzufGui
import pandas as pd
import matplotlib.pyplot as plt

'''Class <CategoryPChart> to draw Pie chart for the first 3 categories'''


class CategoryPChart(WuzzufGui, ReadCsvData):

    df = pd.DataFrame(ReadCsvData.posts_sample)

    def category1PieChart(self):

        # search for "category" in df.
        category1 = self.df.ix[:, 'job_category1'].head(7)

        '''The Count of each item => So, this can be slices'''
        siz = category1.value_counts()

        '''To make it Unique => So, this can be [Labels]'''
        cat_set = set(category1)
        plt.pie(siz, labels=cat_set, autopct='%1.1f%%')
        plt.show()

    # Draw Category-2 Pie Chart
    def category2PieChart(self):
        # search for "category 2" in df.
        category2 = self.df.ix[:, 'job_category2'].head(7)
        siz = category2.value_counts()
        cat_set = set(category2)
        plt.pie(siz, labels=cat_set, autopct='%1.1f%%')
        plt.show()

    # Draw Category-3 Pie Chart
    def category3PieChart(self):
        # search for "category 2" in df.
        category3 = self.df.ix[:, 'job_category3'].head(7)
        siz = category3.value_counts()
        cat_set = set(category3)
        plt.pie(siz, labels=cat_set, autopct='%1.1f%%')
        plt.show()


'''Class <IndustryPChart> to draw Pie chart for the first 3 Industries'''


class IndustryPChart(WuzzufGui, ReadCsvData):

    df = pd.DataFrame(ReadCsvData.posts_sample)

    def industry1PieChart(self):
        indust1 = self.df.ix[:, 'job_industry1'].head(7)
        siz = indust1.value_counts()
        indust_set = set(indust1)
        plt.pie(siz, labels=indust_set, autopct='%1.1f%%')
        plt.show()

    def industry2PieChart(self):
        indust2 = self.df.ix[:, 'job_industry2'].head(7)
        siz = indust2.value_counts()
        indust_set = set(indust2)
        plt.pie(siz, labels=indust_set, autopct='%1.1f%%')
        plt.show()

    def industry3PieChart(self):
        indust3 = self.df.ix[:, 'job_industry3'].head(7)
        siz = indust3.value_counts()
        indust_set = set(indust3)
        plt.pie(siz, labels=indust_set, autopct='%1.1f%%')
        plt.show()


class ApplicantsJU(WuzzufGui, ReadCsvData):
    # Read app_sample Data
    df = pd.DataFrame(ReadCsvData.app_sample)

    def JobUserApplicant(self):
        userID = self.df.ix[:, 'user_id'].head(15)  # xLabel
        jobID = self.df.ix[:, 'job_id'].tail(15)  # yLabel

        # Convert into List
        userList = list(userID)
        jobList = list(jobID)

        plt.bar(jobList, userList, label="Applicants")
        plt.xlabel("Job")
        plt.ylabel("User")
        plt.legend()
        plt.show()

    def UserJobApplicant(self):
        # Read app_sample Data
        df = pd.DataFrame(ReadCsvData.app_sample)

        # Set xLabel => User
        uID = df.ix[:, 'user_id'].tail(4)
        uList = list(uID)

        counter=[]
        for user in uList:
            counter.append(uList.count(user))

        plt.bar(uList, counter, label="Users Appl")
        plt.xlabel("User ID")
        plt.ylabel("#Applicant")
        plt.legend()
        plt.show()


'''Class of City Bar Chart >> print bar chart for each job within a unique city'''

class CityBarChart(WuzzufGui, ReadCsvData):
    # Read app_sample Data
    df = pd.DataFrame(ReadCsvData.posts_sample)

    def cityBCh(self):
        cities = self.df.ix[:, 'city'].head(15)
        siz = cities.value_counts()
        city_set = set(cities)
        # Convert set to List, so it can match in bar chart.
        city_list = [city for city in city_set]

        plt.bar(city_list, siz, label="Cities")
        plt.legend()
        plt.show()

    def viewsBch(self):
        views = self.df.ix[:, 'views'].head(5)
        id = self.df.ix[:, 'id'].head(5)

        views_set = set(views)
        view_list = [x for x in views_set]

        id_set = set(id)
        id_list = [i for i in id_set]

        plt.bar(id_list, view_list, label="Views")
        plt.xlabel("Id")
        plt.ylabel("Views")
        plt.legend()
        plt.show()

rt = WuzzufGui() # Draw the Ui

# Category Data
categPie = CategoryPChart()
category_label = rt.lbl(rt.root, text="(1) Choose Category To print its Pie Chart: ",
                        padx=10, font="sans-serif").grid(column=0, row=0)
button1 = rt.btn(rt.root, text="Category 1", padx=5, command=categPie.category1PieChart).grid(column=1, row=0)
button2 = rt.btn(rt.root, text="Category 2", padx=5, command=categPie.category2PieChart).grid(column=2, row=0)
button3 = rt.btn(rt.root, text="Category 3", padx=5, command=categPie.category3PieChart).grid(column=3, row=0)

# Industry Data
industPie = IndustryPChart()
indust_label = rt.lbl(rt.root, text="(2) Choose Industry to print its Pie Chart: "
                      , font="sans-serif").grid(column=0, row=2)
indst_button1 = rt.btn(rt.root, text="Industry 1", padx=5,command=industPie.industry1PieChart).grid(column=1, row=2)
indst_button2 = rt.btn(rt.root, text="Industry 2", padx=5,command=industPie.industry2PieChart).grid(column=2, row=2)
indst_button3 = rt.btn(rt.root, text="Industry 3", padx=5,command=industPie.industry3PieChart).grid(column=3, row=2)

# Job Applicants and Users' Jobs
JobUserBar = ApplicantsJU()
JUB_label = rt.lbl(rt.root, text="(3) Choose User or Job Bar Chart: ", font="sans-serif").grid(column=0, row=4)
JUB_button1 = rt.btn(rt.root, text="Job-User", padx=5, command=JobUserBar.JobUserApplicant).grid(column=1, row=4)
JUB_button2 = rt.btn(rt.root, text="User-Job", padx=5, command=JobUserBar.UserJobApplicant).grid(column=2, row=4)


# City Bar Chart.
citybchart = CityBarChart()
city_label = rt.lbl(rt.root, text="(4) Preview bar chart for each cities' jobs: ", font="sans-serif").grid(column=0, row=6)
city_button = rt.btn(rt.root, text="Cities' jobs", padx=5, command=citybchart.cityBCh).grid(column=1, row=6)
city_button2 = rt.btn(rt.root, text="Views", padx=5, command=citybchart.viewsBch).grid(column=2, row=6)

rt.root.mainloop()
