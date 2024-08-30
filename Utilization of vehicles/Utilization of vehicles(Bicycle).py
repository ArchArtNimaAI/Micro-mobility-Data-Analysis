import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.pyplot import hist

df = pd.read_pickle('Chicago_dataset_3m.pkl')
df
df.describe(include='all')
df_gp = df.groupby(["vehicle_type"], as_index=False).size()
df_gp
new_data = df.dropna(axis = 0, how = 'any')
new_data
print("Old data frame length:", len(df))
print("New data frame length:", len(new_data)) 
print("Number of rows with at least 1 'nan' or 'null' value: ",

Old data frame length: 3000000
New data frame length: 2999340
Number of rows with at least 1 'nan' or 'null' value:  660
vehicle_gp = new_data.groupby(["vehicle_type"], as_index=False).size()
# [149,76,103]
print(vehicle_gp)
vehicle_gp.plot(kind='bar', x='vehicle_type', y='size', color=[0.7,0.25,0.4])

utilize = new_data.groupby(["day_of_week"], as_index=False)["day_of_week"].value_counts()\
.rename(columns={"count":"number_of_Utilize"})

utilize.assign(Utilize_percentage = lambda x: (x['number_of_Utilize'] /len(new_data) * 100))
utilize_gp1 = utilize.assign(days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])
utilize_gp_new = utilize_gp1.assign(mean_percentage = lambda x: (x['number_of_Utilize'] /len(new_data) * 100))
utilize_gp_new["day_of_week"] = utilize_gp_new["day_of_week"].astype('int')

utilize_gp_c = utilize_gp_new.assign(median = 0)
utilize_gp_c = utilize_gp_c.assign(median_percentage = 0)

test = np.arange(1, 10)
np.median(test)
for i in range(len(utilize_gp_c["number_of_Utilize"])):
        if utilize_gp_c["number_of_Utilize"][i] % 2 == 0:
            m1 = np.median(np.arange(utilize_gp_c["number_of_Utilize"][i]))
            med = m1/utilize_gp_c["number_of_Utilize"][i] * 100

            utilize_gp_c['median_percentage'][i] = utilize_gp_c['median_percentage'][i] + med
            utilize_gp_c['median'][i] = utilize_gp_c['median'][i] + m1
        else:
            m2 = np.median(np.arange(utilize_gp_c["number_of_Utilize"][i]))
            med2 = m2/utilize_gp_c["number_of_Utilize"][i] * 100
            utilize_gp_c['median_percentage'][i] = utilize_gp_c['median_percentage'][i] + med2
            utilize_gp_c['median'][i] = utilize_gp_c['median'][i] + m2
            


# mean_bar = utilize_gp_c.plot(kind='bar', xlabel='day_of_week', ylabel='number_of_Utilize', x='days', y='mean_percentage', color=[0.7,0.25,0.4])
# median_bar = utilize_gp_c.plot(kind='bar', xlabel='day_of_week', ylabel='median_percentage', x='days', y='median_percentage', color=[0.7,0.25,0.4])
# median_bar = utilize_gp_c.plot(kind='bar', xlabel='day_of_week', ylabel='median', x='days', y='median')
# print("The mean of 'mean_percentage' is: %f percent" % utilize_gp_c["mean_percentage"].mean())
# print("The median of 'number_of_Utilize' is: %s and equal to %d" % (utilize_gp_c["days"][0],utilize_gp_c["number_of_Utilize"].median()))

Utilize_gp_plt = utilize_gp_c.plot(kind='bar', x='days', y='number_of_Utilize', color=[0.7,0.25,0.4])

utilize_gp_c.sort_values('number_of_Utilize')


C:\Users\nimas\AppData\Local\Temp\ipykernel_18564\2460417367.py:23: SettingWithCopyWarning: 
A value is trying to be set on a copy of a slice from a DataFrame

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
  utilize_gp_c['median_percentage'][i] = utilize_gp_c['median_percentage'][i] + med
C:\Users\nimas\AppData\Local\Temp\ipykernel_18564\2460417367.py:24: SettingWithCopyWarning: 
A value is trying to be set on a copy of a slice from a DataFrame

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
  utilize_gp_c['median'][i] = utilize_gp_c['median'][i] + m1


# df["start_time"].value_counts(), df.unique()
bicycle_ = new_data.query("vehicle_type == 'bicycle'")
bicycle_20 = bicycle_.query("year == '2020'")
bicycle_21 = bicycle_.query("year == '2021'")
bicycle_22 = bicycle_.query("year == '2022'")
# print("The number of rows in bicycle table is: %d"  % len(bicycle_))
bicycle_t = bicycle_.groupby(by=["vehicle_type", "year", "month", "day_of_week", "device_id"], as_index = False).size()

gragh = bicycle_.groupby(["year", "vehicle_type"]).size()
gragh.plot(kind="bar", x="year", ylabel="size", color=[0.7,0.25,0.4])
bicycle_t


month20_gp = bicycle_20.groupby(["month"], as_index=False).size().sort_values(by="size")
month20_gp
month_gp_20 = month20_gp.assign(month_name = ['November', 'December'])

month_gp_20_new = month_gp_20.assign(Percentage_utilize = lambda x: (x['size'] /len(bicycle_20) * 100))

# month_name = ['January', 'February', 'March', 'April', 'May', 'June', 'July',\
#               'August', 'September', 'october', 'november', 'December']
month_gp_20_new
month21_gp_plot = month_gp_20_new.plot(kind='bar', xlabel='month', ylabel='Number of bicycle utilize in 2021', x='month_name', y='size', color=[0.7,0.25,0.4])
month_gp_20_new


# month_gp_new = month_gp.insert(2, "percentage", lambda x: "size"/x)
# bicycle_20


b_id_20 = set()
b_m_20 = set()
for i, j in bicycle_20.iterrows():
    b_id_20.add(j['device_id'])
    b_m_20.add((j['device_id'], j['month']))
    
    
report_b_20 = {}
for i in b_id_20:
    count = 0
    report_b_20[i] = []
    for j in b_m_20:
        if i == j[0]:
            count = count + 1
            report_b_20[i].append(int(j[1]))
            
#     report[i].append(str(count))
    
# print(report_b_20)


report_b_20_s = sorted(report_b_20.items(), key=lambda x: len(x[1]))
converted_dict = dict(report_b_20_s)
# print(len(converted_dict))
# converted_dict
Report_2020 = {}  
for j in range(1, 13):
    count=0
    for i, l in converted_dict.items():
        if len(l) == j:
            count = count + 1
 
    Report_2020['used in ' + str(j) + ' months'] = count 

# print(Report_2020)


470


month_name20 = {}

count11 = 0
count12 = 0
for i, l in converted_dict.items():
    if len(l) == 1:
#         print(l)
        if l[0] == 11:
            count11 = count11 + 1
        if l[0] == 12:
            count12 = count12 + 1
      
    month_name20['Nov'] = count11
    month_name20['Dec'] = count12

print(month_name20)
plt.bar(*zip(*month_name20.items()), color=[0.7,0.25,0.4])
plt.show()               
            


{'Nov': 27, 'Dec': 47}


month21_gp = bicycle_21.groupby(["month"], as_index=False).size().sort_values(by="size")

month21_gp_1 = month21_gp.assign(month_name = ['January', 'october', 'November', 'December', 'February',\
                                               'March', 'April', 'May', 'June', 'July' ,'August', 'September'])

# month21_gp_1
month21_gp_new = month21_gp_1.assign(Percentage_utilize = lambda x: (x['size'] /len(bicycle_21) * 100))

# month_name = ['January', 'February', 'March', 'April', 'May', 'June', 'July',\
#               'August', 'September', 'october', 'november', 'December']

month21_gp_new["month"] = month21_gp_new["month"].astype(str) + "-" + month21_gp_new["month_name"]
month21_gp_plot = month21_gp_new.plot(kind='bar', xlabel='month', ylabel='Number of bicycle utilize in 2021', x='month_name', y='size', color=[0.7,0.25,0.4])
month21_gp_new


b_id_21 = set()
b_m_21 = set()
for i, j in bicycle_21.iterrows():
    b_id_21.add(j['device_id'])
    b_m_21.add((j['device_id'], j['month']))
    
    
report_b_21 = {}
for i in b_id_21:
    count = 0
    report_b_21[i] = []
    for j in b_m_21:
        if i == j[0]:
            count = count + 1
            report_b_21[i].append(int(j[1]))


report_b_21_s = sorted(report_b_21.items(), key=lambda x: len(x[1]))
converted_dict = dict(report_b_21_s)
# print(len(converted_dict))

Report_2021 = {}  
for j in range(1, 13):
    count=0
    for i, l in converted_dict.items():
        if len(l) == j:
            count = count + 1
 
    Report_2021['used in ' + str(j) + ' months'] = count 

print(Report_2021)


{'used in 1 months': 149, 'used in 2 months': 130, 'used in 3 months': 117, 'used in 4 months': 99, 'used in 5 months': 32, 'used in 6 months': 35, 'used in 7 months': 55, 'used in 8 months': 80, 'used in 9 months': 156, 'used in 10 months': 0, 'used in 11 months': 0, 'used in 12 months': 0}


month_name21 = {}

count1 = 0
count2 = 0
count3 = 0
count4 = 0
count5 = 0
count6 = 0
count7 = 0
count8 = 0
count9 = 0
count10 = 0
count11 = 0
count12 = 0
for i, l in converted_dict.items():
    if len(l) == 1:
#         print(l)
        if l[0] == 1:
            count1 = count1 + 1
        if l[0] == 2:
            count2 = count2 + 1
        if l[0] == 3:
            count3 = count3 + 1
        if l[0] == 4:
            count4 = count4 + 1
        if l[0] == 5:
            count5 = count5 + 1
        if l[0] == 6:
            count6 = count6 + 1
        if l[0] == 7:
            count7 = count7 + 1
        if l[0] == 12:
            count8 = count8 + 1
        if l[0] == 9:
            count9 = count9 + 1
        if l[0] == 10:
            count10 = count10 + 1
        if l[0] == 11:
            count11 = count11 + 1            
        if l[0] == 12:
            count12 = count12 + 1            
            
    month_name21['Jan'] = count1
    month_name21['Feb'] = count2
    month_name21['Mar'] = count3
    month_name21['Apr'] = count4
    month_name21['may'] = count5
    month_name21['Jun'] = count6
    month_name21['Jul'] = count7
    month_name21['Aug'] = count8
    month_name21['Sep'] = count9
    month_name21['Oct'] = count10
    month_name21['Nov'] = count11
    month_name21['Dec'] = count12
print(month_name21)
plt.bar(*zip(*month_name21.items()), color=[0.7,0.25,0.4])
plt.show()      


{'Jan': 0, 'Feb': 0, 'Mar': 0, 'Apr': 0, 'may': 0, 'Jun': 0, 'Jul': 0, 'Aug': 47, 'Sep': 0, 'Oct': 0, 'Nov': 27, 'Dec': 47}


month22_gp = bicycle_22.groupby(["month"], as_index=False).size().sort_values(by="size")

month22_gp
month22_gp_1 = month22_gp.assign(month_name = ['March', 'January', 'February'])
month22_gp_new = month22_gp_1.assign(Percentage_utilize = lambda x: (x['size'] /len(bicycle_22) * 100))
                                 
month22_gp_new
# month_name = ['January', 'February', 'March', 'April', 'May', 'June', 'July',\
#               'August', 'September', 'october', 'november', 'December']

month22_gp_new["month"] = month22_gp_new["month"].astype(str) + "-" + month22_gp_new["month_name"]
month22_gp_plot = month22_gp_new.plot(kind='bar', xlabel='month', ylabel='Number of bicycle utilize in 2021', x='month_name', y='size', color=[0.7,0.25,0.4])
month22_gp_new


b_id_22 = set()
b_m_22 = set()
for i, j in bicycle_22.iterrows():
    b_id_22.add(j['device_id'])
    b_m_22.add((j['device_id'], j['month']))
    
    
report_b_22 = {}
for i in b_id_22:
    count = 0
    report_b_22[i] = []
    for j in b_m_22:
        if i == j[0]:
            count = count + 1
            report_b_22[i].append(int(j[1]))


report_b_22_s = sorted(report_b_22.items(), key=lambda x: len(x[1]))
converted_dict22 = dict(report_b_22_s)
# print(len(converted_dict))

Report_2022 = {}  
for j in range(1, 13):
    count=0
    for i, l in converted_dict22.items():
        if len(l) == j:
            count = count + 1
 
    Report_2022['used in ' + str(j) + ' months'] = count 

print(Report_2022)


{'used in 1 months': 153, 'used in 2 months': 25, 'used in 3 months': 1, 'used in 4 months': 0, 'used in 5 months': 0, 'used in 6 months': 0, 'used in 7 months': 0, 'used in 8 months': 0, 'used in 9 months': 0, 'used in 10 months': 0, 'used in 11 months': 0, 'used in 12 months': 0}


month_name22 = {}

count1 = 0
count2 = 0
count3 = 0
for i, l in converted_dict22.items():
    if len(l) == 1:
#         print(l)
        if l[0] == 1:
            count1 = count1 + 1
        if l[0] == 2:
            count2 = count2 + 1
        if l[0] == 3:
            count3 = count3 + 1
      
    month_name22['Jan'] = count1
    month_name22['Feb'] = count2
    month_name22['Mar'] = count3

print(month_name22)
plt.bar(*zip(*month_name22.items()), color=[0.7,0.25,0.4])
plt.show()    


{'Jan': 72, 'Feb': 74, 'Mar': 7}


