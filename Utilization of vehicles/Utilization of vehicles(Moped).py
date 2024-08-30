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

print(vehicle_gp)
vehicle_gp.plot(kind='bar', x='vehicle_type', y='size', color=[0.7,0.25,0.4])

# df["start_time"].value_counts(), df.unique()
moped_ = new_data.query("vehicle_type == 'moped'")
moped_20 = moped_.query("year == '2020'")
moped_21 = moped_.query("year == '2021'")
moped_22 = moped_.query("year == '2022'")
# print("The number of rows in bicycle table is: %d"  % len(bicycle_))
moped_t = moped_.groupby(by=["vehicle_type", "year", "month", "day_of_week", "device_id"], as_index = False).size()

gragh = moped_.groupby(["year", "vehicle_type"]).size()
gragh.plot(kind="bar", x="year", ylabel="size", color=[0.7,0.25,0.4])
moped_t


month20_gp = moped_20.groupby(["month"], as_index=False).size().sort_values(by="size")
month20_gp
month_gp_20 = month20_gp.assign(month_name = ['December', 'November'])

month_gp_20_new = month_gp_20.assign(Percentage_utilize = lambda x: (x['size'] /len(moped_20) * 100))

# month_name = ['January', 'February', 'March', 'April', 'May', 'June', 'July',\
#               'August', 'September', 'october', 'november', 'December']
month21_gp_plot = month_gp_20_new.plot(kind='bar', xlabel='month', ylabel='Number of moped utilize in 2021', x='month_name', y='size', color=[0.7,0.25,0.4])
month_gp_20_new


b_id_20 = set()
b_m_20 = set()
for i, j in moped_20.iterrows():
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

Report_2020 = {}  
for j in range(1, 13):
    count=0
    for i, l in converted_dict.items():
        if len(l) == j:
            count = count + 1
 
    Report_2020['used in ' + str(j) + ' months'] = count 

print(Report_2020)

{'used in 1 months': 123, 'used in 2 months': 311, 'used in 3 months': 0, 'used in 4 months': 0, 'used in 5 months': 0, 'used in 6 months': 0, 'used in 7 months': 0, 'used in 8 months': 0, 'used in 9 months': 0, 'used in 10 months': 0, 'used in 11 months': 0, 'used in 12 months': 0}


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


{'Nov': 112, 'Dec': 11}


month21_gp = moped_21.groupby(["month"], as_index=False).size().sort_values(by="size")
month21_gp
month21_gp_1 = month21_gp.assign(month_name = ['october', 'December', 'November', 'September'])

month21_gp_1
month21_gp_new = month21_gp_1.assign(Percentage_utilize = lambda x: (x['size'] /len(moped_21) * 100))

# # month_name = ['January', 'February', 'March', 'April', 'May', 'June', 'July',\
# #               'August', 'September', 'october', 'november', 'December']

month21_gp_plot = month21_gp_new.plot(kind='bar', xlabel='month', ylabel='Number of moped utilize in 2021', x='month_name', y='size', color=[0.7,0.25,0.4])
month21_gp_new


b_id_21 = set()
b_m_21 = set()
for i, j in moped_21.iterrows():
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
converted_dict21 = dict(report_b_21_s)
# print(len(converted_dict))

Report_2021 = {}  
for j in range(1, 13):
    count=0
    for i, l in converted_dict21.items():
        if len(l) == j:
            count = count + 1
 
    Report_2021['used in ' + str(j) + ' months'] = count 

print(Report_2021)


{'used in 1 months': 554, 'used in 2 months': 1, 'used in 3 months': 0, 'used in 4 months': 0, 'used in 5 months': 0, 'used in 6 months': 0, 'used in 7 months': 0, 'used in 8 months': 0, 'used in 9 months': 0, 'used in 10 months': 0, 'used in 11 months': 0, 'used in 12 months': 0}


month_name21 = {}

count9 = 0
count10 = 0
count11 = 0
count12 = 0
for i, l in converted_dict21.items():
    if len(l) == 1:
        if l[0] == 9:
            count9 = count9 + 1
        if l[0] == 10:
            count10 = count10 + 1
        if l[0] == 11:
            count11 = count11 + 1            
        if l[0] == 12:
            count12 = count12 + 1            

    month_name21['Sep'] = count9
    month_name21['Oct'] = count10
    month_name21['Nov'] = count11
    month_name21['Dec'] = count12
print(month_name21)
plt.bar(*zip(*month_name21.items()), color=[0.7,0.25,0.4])
plt.show()   


{'Sep': 520, 'Oct': 1, 'Nov': 27, 'Dec': 6}


month22_gp = moped_22.groupby(["month"], as_index=False).size().sort_values(by="size")

month22_gp
month22_gp_1 = month22_gp.assign(month_name = ['January', 'February'])
month22_gp_new = month22_gp_1.assign(Percentage_utilize = lambda x: (x['size'] /len(moped_22) * 100))
                                 
month22_gp_new
# # month_name = ['January', 'February', 'March', 'April', 'May', 'June', 'July',\
# #               'August', 'September', 'october', 'november', 'December']

month22_gp_plot = month22_gp_new.plot(kind='bar', xlabel='month', ylabel='Number of moped utilize in 2021', x='month_name', y='size', color=[0.7,0.25,0.4])
month22_gp_new


b_id_22 = set()
b_m_22 = set()
for i, j in moped_22.iterrows():
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

print(report_b_22)


{'122c6db9-31fa-44d5-9bdc-d0e7f094b54e': [2], '6c7f6eec-071f-4378-a603-c932545eba90': [2], '0ecee8b2-f285-4dd1-bdfc-fbdd06a5aacb': [1], '03856e35-1e3e-4ff3-a26c-5e9504e33c9c': [2], '65c27fad-f1cb-4ace-87b5-864bc371ffdc': [1], '1849e6a8-cdfb-4740-a07a-538d88bccc34': [1], '21636a04-1bd4-454c-b689-84cffd4430e8': [2], '74a1b286-7169-4bf9-92cb-4885fc32be90': [2], '0bd5a220-ca1b-4b98-98fb-29998b196aa8': [2], 'a9a2965a-b5d1-40ef-9de5-b70ac36ee82a': [2], 'd00099a5-2e33-4c4b-b9f4-bbf342b72e46': [2, 1]}


report_b_22_s = sorted(report_b_22.items(), key=lambda x: len(x[1]))
converted_dict22 = dict(report_b_22_s)
# print(len(converted_dict22))

Report_2022 = {}  
for j in range(1, 13):
    count=0
    for i, l in converted_dict22.items():
        if len(l) == j:
            count = count + 1
 
    Report_2022['used in ' + str(j) + ' months'] = count 

print(Report_2022)


{'used in 1 months': 10, 'used in 2 months': 1, 'used in 3 months': 0, 'used in 4 months': 0, 'used in 5 months': 0, 'used in 6 months': 0, 'used in 7 months': 0, 'used in 8 months': 0, 'used in 9 months': 0, 'used in 10 months': 0, 'used in 11 months': 0, 'used in 12 months': 0}


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
      
    month_name22['Jan'] = count1
    month_name22['Feb'] = count2

print(month_name22)
plt.bar(*zip(*month_name22.items()), color=[0.7,0.25,0.4])
plt.show() 


{'Jan': 3, 'Feb': 7}


