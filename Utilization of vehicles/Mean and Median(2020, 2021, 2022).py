import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sb
import matplotlib.pyplot as plt

df = pd.read_pickle('AustinTexas_3m.pkl')
df
df.describe(include='all')
df_gp = df.groupby(["vehicle_type"], as_index=False).size()
df_gp

new_data = df.dropna(axis = 0, how = 'any')
new_data
print("Old data frame length:", len(df))
print("New data frame length:", len(new_data)) 
print("Number of rows with at least 1 'nan' or 'null' value: ",

vehicle_gp = new_data.groupby(["vehicle_type"], as_index=False).size()
# [149,76,103]
print(vehicle_gp)
vehicle_gp.plot(kind='bar', x='vehicle_type', y='size', color=[0.7,0.25,0.4])

# od_matrix1 = (new_data.assign(count=1)).pivot_table(index="vehicle_type", columns= 'day_of_week', values="count", aggfunc="count")\
# .query("vehicle_type == 'bicycle'")

# od_matrix1.plot(kind='bar', color=[0.7,0.25,0.4])
# od_matrix1
# od_matrix1


utilize = new_data.groupby(["day_of_week"], as_index=False)["day_of_week"].value_counts()\
.rename(columns={"count":"number_of_Utilize"})

utilize.assign(Utilize_percentage = lambda x: (x['number_of_Utilize'] /len(new_data) * 100))
utilize_gp1 = utilize.assign(days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])
utilize_gp1

# Utilize_piv = utilize_gp1.pivot_table(index="vehicle_type", columns= 'year', values="count", aggfunc="count")\
# .query("vehicle_type == 'bicycle'")

utilize_gp_new = utilize_gp1.assign(utilization_percentage = lambda x: (x['number_of_Utilize'] /len(new_data) * 100))
utilize_gp_new["day_of_week"] = utilize_gp_new["day_of_week"].astype('int')

utilize_gp_new.plot(kind='bar', x='days', y='number_of_Utilize', color=[0.7,0.25,0.4])
utilize_gp_new
# utilize_gp_c = utilize_gp_new.assign(median = 0)
# utilize_gp_c = utilize_gp_c.assign(median_percentage = 0)


# for i in range(len(utilize_gp_c["number_of_Utilize"])):
#         if utilize_gp_c["number_of_Utilize"][i] % 2 == 0:
#             m1 = np.median(np.arange(utilize_gp_c["number_of_Utilize"][i]))
#             med = m1/utilize_gp_c["number_of_Utilize"][i] * 100

#             utilize_gp_c['median_percentage'][i] = utilize_gp_c['median_percentage'][i] + med
#             utilize_gp_c['median'][i] = utilize_gp_c['median'][i] + m1
#         else:
#             m2 = np.median(np.arange(utilize_gp_c["number_of_Utilize"][i]))
#             med2 = m2/utilize_gp_c["number_of_Utilize"][i] * 100
#             utilize_gp_c['median_percentage'][i] = utilize_gp_c['median_percentage'][i] + med2
#             utilize_gp_c['median'][i] = utilize_gp_c['median'][i] + m2
            


# mean_bar = utilize_gp_c.plot(kind='bar', xlabel='day_of_week', ylabel='number_of_Utilize', x='days', y='mean_percentage', color=[0.7,0.25,0.4])
# median_bar = utilize_gp_c.plot(kind='bar', xlabel='day_of_week', ylabel='median_percentage', x='days', y='median_percentage', color=[0.7,0.25,0.4])
# median_bar = utilize_gp_c.plot(kind='bar', xlabel='day_of_week', ylabel='median', x='days', y='median')
# print("The mean of 'mean_percentage' is: %f percent" % utilize_gp_c["mean_percentage"].mean())
# print("The median of 'number_of_Utilize' is: %s and equal to %d" % (utilize_gp_c["days"][0],utilize_gp_c["number_of_Utilize"].median()))

# Utilize_gp_plt = utilize_gp_c.plot(kind='bar', x='days', y='number_of_Utilize', color=[0.7,0.25,0.4])
# utilize_gp_c


data = []
monday = np.random.uniform(0, 1, 360064)
for i in monday:
    data.append(i)
tuesday = np.random.uniform(1, 2, 258438)
for i in tuesday:
    data.append(i)
Wednesday = np.random.uniform(2, 3, 264706)
for i in Wednesday:
    data.append(i)
Thursday = np.random.uniform(3, 4, 298799)
for i in Thursday:
    data.append(i)
Friday = np.random.uniform(4, 5, 405883)
for i in Friday:
    data.append(i)
Saturday = np.random.uniform(5, 6, 690238)
for i in Saturday:
    data.append(i)
Sunday = np.random.uniform(6, 7, 721212)
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
