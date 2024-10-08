import pandas as pd
import matplotlib.pyplot as plt
from sodapy import Socrata
import seaborn as sns

df = pd.read_pickle('AustinTexas_dataset.pkl')
df.head(15)
df.shape
(3000000, 18)
df.info()

sns.heatmap(df.isna())

new_data = df.dropna(axis= 0, how= 'any')
new_data.shape
print("Old data frame length:", len(df))
print("New data frame length:", len(new_data)) 
print("Number of rows with at least 1 'nan' or 'null' value: ",
      (len(df)-len(new_data)))

#Old data frame length: 3000000
#New data frame length: 2999340
#Number of rows with at least 1 'nan' or 'null' value:  660

new_data.info()
#start-date and time : 2021-09-11T06:00:00:000
start_time_gp = new_data.groupby(["start_time"], as_index=False)["start_time"].size()
start_date = start_time_gp.sort_values(by=["start_time"], ascending=True)
start_date
#Most recent time is: 2022-03-25T00:30:00:000


#Most recent time: 2021-10-11T06:00:00:000 ------> 537 records
# most_recent_time = start_time_gp.sort_values(by=["size"], ascending=False)
# most_recent_tim
Most_data = new_data.groupby(["start_time"], as_index=False)["start_time"].size()
Most_data = start_time_gp.sort_values(by=["size"], ascending=False)
Most_data

new_data_year = new_data.groupby(["year", "month", "start_time", "vehicle_type"], as_index= False).size()
new_data_year
gragh = new_data_year.groupby(["year", "month"]).size()
gragh.plot(kind="bar", x="year", ylabel="size", y="size", xlabel= "year, month", color=[0.7,0.25,0.4])
# gragh = new_data_year.plot(kind='bar', color="orange", x="year", y="size", xlabel= "year, month", ylabel= "size")

unique_vehicle = new_data.groupby(["vehicle_type", "year"], as_index= False)["year"].size()
unique_vehicle.sort_values(by="year")

unique_vehicle["vehicle_type"] = unique_vehicle["vehicle_type"].astype(str) + "-" + unique_vehicle["year"].astype(str)
v_gragh = unique_vehicle.plot(kind='bar', x="vehicle_type", color=[0.7,0.25,0.4], xlabel= "vehicle_type_year", ylabel= "size")

