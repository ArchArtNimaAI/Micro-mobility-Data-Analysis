import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sb
import matplotlib.pyplot as plt

df = pd.read_pickle('AustinTexas_3m.pkl')
new_data = df.dropna(axis = 0, how = 'any')
new_data
# data_2020 = new_data.query("year == '2020'")
utilize = new_data.query("year == '2021'").groupby(["day_of_week"], as_index=False)["day_of_week"].value_counts()\
.rename(columns={"count":"number_of_Utilize"})
utilize
sum_utilize = sum(utilize['number_of_Utilize'])
print(sum_utilize)

# utilize.assign(Utilize_percentage = lambda x: (x['number_of_Utilize'] / sum_utilize * 100))
utilize_gp1 = utilize.assign(days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])
utilize_gp1

utilize_gp_new = utilize_gp1.assign(utilization_percentage = lambda x: (x['number_of_Utilize'] / sum_utilize * 100))
utilize_gp_new["day_of_week"] = utilize_gp_new["day_of_week"].astype('int')
utilize_gp_new.plot(kind='bar', x='days', y='number_of_Utilize', color=[0.7,0.25,0.4])
utilize_gp_new

data = []
monday = np.random.uniform(0, 1, 328624)
for i in monday:
    data.append(i)
tuesday = np.random.uniform(1, 2, 229929)
for i in tuesday:
    data.append(i)
Wednesday = np.random.uniform(2, 3, 233363)
for i in Wednesday:
    data.append(i)
Thursday = np.random.uniform(3, 4, 274633)
for i in Thursday:
    data.append(i)
Friday = np.random.uniform(4, 5, 378309)
for i in Friday:
    data.append(i)
Saturday = np.random.uniform(5, 6, 642619)
for i in Saturday:
    data.append(i)
Sunday = np.random.uniform(6, 7, 668778)
for i in Sunday:
    data.append(i)
        
len(data)
data_mean = np.mean(data)
data_median = np.median(data)

a,bins,c=plt.hist(data,bins=7,histtype='step', color='black')
a,bins,c=plt.hist(data,bins=7, color=[0.7,0.25,0.4])
l=list(bins)
l.insert(0,0)
l.insert(len(bins)+1,bins[len(bins)-1])
mid=[]
for i in range(len(l)-1):
    ele=(l[i]+l[i+1])/2
    mid.append(ele)
x=list(a)
x.insert(0,0)
x.insert(len(a)+1,0)
plt.plot(mid,x,'go--', color='black')
plt.xlabel("Days")
plt.ylabel("Vehicle Utilization")
# plt.title("Student Marks Distribution")
plt.axvline(data_mean, color='y', linestyle='-', label="Mean")
plt.axvline(data_median, color='b', linestyle='--', label="Median")
plt.legend()
plt.show()



