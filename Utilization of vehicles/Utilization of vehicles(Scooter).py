import pandas as pd
import matplotlib.pyplot as plt

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

vehicle_gp = new_data.groupby(["vehicle_type"], as_index=False).size()
vehicle_gp.plot(kind='bar', x='vehicle_type', y='size', color=[0.7,0.25,0.4])
vehicle_gp

# df["start_time"].value_counts(), df.unique()
scooter_ = new_data.query("vehicle_type == 'scooter'")
scooter_20 = scooter_.query("year == '2020'")
scooter_21 = scooter_.query("year == '2021'")
scooter_22 = scooter_.query("year == '2022'")
# print("The number of rows in bicycle table is: %d"  % len(bicycle_))
scooter_t = scooter_.groupby(by=["vehicle_type", "year", "month", "day_of_week", "device_id"], as_index = False).size()

gragh = scooter_.groupby(["year", "vehicle_type"]).size()
gragh.plot(kind="bar", x="year", ylabel="size", color=[0.7,0.25,0.4])
scooter_t


month20_gp = scooter_20.groupby(["month"], as_index=False).size().sort_values(by="size")
month20_gp
month_gp_20 = month20_gp.assign(month_name = ['December', 'November'])

month_gp_20_new = month_gp_20.assign(Percentage_utilize = lambda x: (x['size'] /len(scooter_20) * 100))

# # month_name = ['January', 'February', 'March', 'April', 'May', 'June', 'July',\
# #               'August', 'September', 'october', 'november', 'December']

month21_gp_plot = month_gp_20_new.plot(kind='bar', xlabel='month', ylabel='Number of scooter utilize in 2021', x='month_name', y='size', color=[0.7,0.25,0.4])
month_gp_20_new


b_id_20 = set()
b_m_20 = set()
for i, j in scooter_20.iterrows():
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
converted_dict20 = dict(report_b_20_s)
# print(len(converted_dict))

Report_2020 = {}  
for j in range(1, 13):
    count=0
    for i, l in converted_dict20.items():
        if len(l) == j:
            count = count + 1
 
    Report_2020['used in ' + str(j) + ' months'] = count 

print(Report_2020)


{'used in 1 months': 1331, 'used in 2 months': 6955, 'used in 3 months': 0, 'used in 4 months': 0, 'used in 5 months': 0, 'used in 6 months': 0, 'used in 7 months': 0, 'used in 8 months': 0, 'used in 9 months': 0, 'used in 10 months': 0, 'used in 11 months': 0, 'used in 12 months': 0}


month_name20 = {}

count11 = 0
count12 = 0
for i, l in converted_dict20.items():
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


{'Nov': 613, 'Dec': 718}


month21_gp = scooter_21.groupby(["month"], as_index=False).size().sort_values(by="size")
month21_gp.sort_values(by="month")
month21_gp_1 = month21_gp.assign(month_name = ['January', 'october', 'November', 'December', 'February', 'March',\
                                               'April', 'May', 'June', 'July', 'August', 'September'])

# month21_gp_1
month21_gp_new = month21_gp_1.assign(Percentage_utilize = lambda x: (x['size'] /len(scooter_21) * 100))

# # # month_name = ['January', 'February', 'March', 'April', 'May', 'June', 'July',\
# # #               'August', 'September', 'october', 'november', 'December']

month21_gp_plot = month21_gp_new.plot(kind='bar', xlabel='month', ylabel='Number of bicycle utilize in 2021', x='month_name', y='size', color=[0.7,0.25,0.4])
month21_gp_new


b_id_21 = set()
b_m_21 = set()
for i, j in scooter_21.iterrows():
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


{'used in 1 months': 4044, 'used in 2 months': 5544, 'used in 3 months': 7092, 'used in 4 months': 5154, 'used in 5 months': 1461, 'used in 6 months': 3480, 'used in 7 months': 2192, 'used in 8 months': 882, 'used in 9 months': 1990, 'used in 10 months': 0, 'used in 11 months': 0, 'used in 12 months': 0}


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
        if l[0] == 8:
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


{'Jan': 351, 'Feb': 51, 'Mar': 110, 'Apr': 100, 'may': 95, 'Jun': 49, 'Jul': 52, 'Aug': 47, 'Sep': 1073, 'Oct': 938, 'Nov': 299, 'Dec': 879}


month22_gp = scooter_22.groupby(["month"], as_index=False).size().sort_values(by="size")

month22_gp
month22_gp_1 = month22_gp.assign(month_name = ['March', 'January', 'February'])
month22_gp_new = month22_gp_1.assign(Percentage_utilize = lambda x: (x['size'] /len(scooter_22) * 100))
                                 
month22_gp_new
# # month_name = ['January', 'February', 'March', 'April', 'May', 'June', 'July',\
# #               'August', 'September', 'october', 'november', 'December']

month22_gp_plot = month22_gp_new.plot(kind='bar', xlabel='month', ylabel='Number of bicycle utilize in 2021', x='month_name', y='size', color=[0.7,0.25,0.4])
month22_gp_new


b_id_22 = set()
b_m_22 = set()
for i, j in scooter_22.iterrows():
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


{'used in 1 months': 5944, 'used in 2 months': 1279, 'used in 3 months': 119, 'used in 4 months': 0, 'used in 5 months': 0, 'used in 6 months': 0, 'used in 7 months': 0, 'used in 8 months': 0, 'used in 9 months': 0, 'used in 10 months': 0, 'used in 11 months': 0, 'used in 12 months': 0}


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


{'Jan': 2403, 'Feb': 2889, 'Mar': 652}


