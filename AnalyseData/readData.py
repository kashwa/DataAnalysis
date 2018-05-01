"""
Read the files of WUZZUF data,
performing operations using Pandas
Data Analysis Library,
Data Structure :[DataFrame - Series].

"""


class ReadCsvData:
    import pandas as pd

    # Read the first file [Application Sample].
    app_sample = pd.read_csv("Wuzzuf_Applications_Sample.csv")

    # Read the second file [Job Posts Sample].
    posts_sample = pd.read_csv("Wuzzuf_Job_Posts_Sample.csv")


"""
## take object and access data ##
---------------------------------

r = ReadCsvData()

read_head = r.app_sample.head()

print(read_head)
"""
