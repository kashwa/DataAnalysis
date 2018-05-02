import matplotlib.pyplot as plt
import pandas as pd


posts_sample = pd.read_csv("AnalyseData/Wuzzuf_Job_Posts_Sample.csv")
app_sample = pd.read_csv("AnalyseData/Wuzzuf_Applications_Sample.csv")

df = pd.DataFrame(posts_sample)

views = df.ix[:, 'views'].head(5)
#siz = views.value_counts()

views_set = set(views)
view_list = [x for x in views_set]

id = df.ix[:, 'id'].head(5)
id_set = set(id)
id_list = [i for i in id_set]

print(id_list)   # xLabel
print(view_list) # yLabel


plt.bar(id_list, view_list, label="bars")


plt.legend()
plt.show()

'''citset = set(cities)


citlist = [x for x in citset]


print(citlist)

print(siz)
#citylist = set(cities)

plt.bar(citlist, siz, label="address")

#print(cities)

plt.legend()
plt.show()'''











'''
this is counting items in a list
now i need to put user on x, count on y

j=[]
for x in usList:
    j.append(usList.count(x))
print(j)

plt.bar(usList, j, label="bars")
'''

#countUser=''

#plt.bar(usList, cntr)



#print(countUser)