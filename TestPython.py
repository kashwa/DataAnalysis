import matplotlib.pyplot as plt
import pandas as pd


posts_sample = pd.read_csv("AnalyseData/Wuzzuf_Job_Posts_Sample.csv")

df = pd.DataFrame(posts_sample)

# search for "category" in df.
category1 = df.ix[:, 'job_category1']

'''The Count of each item => So, this can be slices'''
siz = category1.value_counts()

'''To make it Unique => So, this can be [Labels]'''
cat_set = set(category1)

plt.pie(siz, labels=cat_set, autopct='%1.1f%%')
plt.show()
