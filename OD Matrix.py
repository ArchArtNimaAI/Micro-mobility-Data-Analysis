import pandas as pd
import matplotlib.pyplot as plt
from sodapy import Socrata

# df = pd.DataFrame.from_records(results)
df = pd.read_pickle('AustinTexas_dataset.pkl')
df

new_df = df.dropna( axis = 0, how = 'any')

new_df["council_district_start"] = new_df["council_district_start"].replace("None", 0)
new_df["council_district_start"] = new_df["council_district_start"].astype('int')
new_df["council_district_end"] = new_df["council_district_end"].replace("None", 0)
new_df["council_district_end"] = new_df["council_district_end"].astype('int')

matrix = (
    new_df.assign(count=1)
    .pivot_table(index="council_district_start", columns="council_district_end",
                 values="count", aggfunc="count")
    .fillna(0)
    .astype(int)
).sort_values("council_district_start")

new_df["council_district_end"] = new_df["council_district_end"].astype('int')


od_matrix1 = (new_df.assign(count=1)).pivot_table(index="vehicle_type", columns= 'year', values="count", aggfunc="count")\
.fillna(0)
od_matrix1

od_matrix_bicycle = (new_df.assign(count=1)).pivot_table(index="vehicle_type", columns= 'year', values="count", aggfunc="count")\
.fillna(0).query("vehicle_type == 'bicycle'")
od_matrix_bicycle

od_matrix1.plot(kind="bar", color=[0.7,0.25,0.4])

od_matrix2 = (df.assign(count=1)).pivot_table(index="vehicle_type", columns= 'year', values="count", aggfunc="count").fillna(0).query("vehicle_type == 'car'")
od_matrix2


od_matrix2.plot(kind="bar", color=[0.7,0.25,0.4])

od_matrix3 = (new_df.assign(count=1)).pivot_table(index="vehicle_type", columns= 'year', values="count", aggfunc="count")\
.fillna(0).query("vehicle_type == 'moped'")
od_matrix3

od_matrix3.plot(kind="bar", color=[0.7,0.25,0.4])

od_matrix4 = (new_df.assign(count=1)).pivot_table(index="vehicle_type", columns= 'year', values="count", aggfunc="count")\
.fillna(0).query("vehicle_type == 'scooter'")
od_matrix4

od_matrix4.plot(kind="bar", color=[0.7,0.25,0.4])

scooter_filter_2020  = new_df.query("vehicle_type == 'scooter' and year == '2020'").groupby(["vehicle_type", "year", "council_district_start"], as_index= False).size().sort_values(by="council_district_start")
scooter_filter_2020

# scooter_filter_2020.to_csv('Scooter_2020.csv', index=False)
scooter_filter_2021  = new_df.query("vehicle_type == 'scooter' and year == '2021'").groupby(["vehicle_type", "year", "council_district_start"], as_index= False).size().sort_values(by="council_district_start")
scooter_filter_2021
# scooter_filter_2021.to_csv('Scooter_21.csv', index=False)
scooter_filter_2022  = new_df.query("vehicle_type == 'scooter' and year == '2022'").groupby(["vehicle_type", "year", "council_district_start"], as_index= False).size().sort_values(by="council_district_start")
scooter_filter_2022
# scooter_filter_2022.to_csv('Scooter_22.csv', index=False)
bicycle_filter_2020  = new_df.query("vehicle_type == 'bicycle' and year == '2020'").groupby(["vehicle_type", "year", "council_district_start"], as_index= False).size().sort_values(by="council_district_start")
bicycle_filter_2020
# bicycle_filter_2020.to_csv('bicycle_20.csv', index=False)
bicycle_filter_2021  = new_df.query("vehicle_type == 'bicycle' and year == '2021'").groupby(["vehicle_type", "year", "council_district_start"], as_index= False).size().sort_values(by="council_district_start")
bicycle_filter_2021
# bicycle_filter_2021.to_csv('bicycle_21.csv', index=False)
bicycle_filter_2022  = new_df.query("vehicle_type == 'bicycle' and year == '2022'").groupby(["vehicle_type", "year", "council_district_start"], as_index= False).size().sort_values(by="council_district_start")
bicycle_filter_2022
# bicycle_filter_2022.to_csv('bicycle_22.csv', index=False)
moped_filter_2020  = new_df.query("vehicle_type == 'moped' and year == '2020'").groupby(["vehicle_type", "year", "council_district_start"], as_index= False).size().sort_values(by="council_district_start")
moped_filter_2020
# moped_filter_2020.to_csv('moped_20.csv', index=False)
moped_filter_2021  = new_df.query("vehicle_type == 'moped' and year == '2021'").groupby(["vehicle_type", "year", "council_district_start"], as_index= False).size().sort_values(by="council_district_start")
moped_filter_2021
# moped_filter_2021.to_csv('moped_21.csv', index=False)
moped_filter_2022  = new_df.query("vehicle_type == 'moped' and year == '2022'").groupby(["vehicle_type", "year", "council_district_start"], as_index= False).size().sort_values(by="council_district_start")
moped_filter_2022
# moped_filter_2022.to_csv('moped_22.csv', index=False)


