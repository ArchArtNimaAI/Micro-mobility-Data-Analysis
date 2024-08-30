import pandas as pd
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
new_data.columns

Index(['trip_id', 'device_id', 'vehicle_type', 'trip_duration',
       'trip_distance', 'start_time', 'end_time', 'modified_date', 'month',
       'hour', 'day_of_week', 'council_district_start', 'council_district_end',
       'year', 'census_geoid_start', 'census_geoid_end',
       'start_time_us_central', 'end_time_us_central'],
      dtype='object')

new_df = new_data.drop(columns=['trip_id', 'device_id', 'vehicle_type',
       'trip_distance', 'start_time', 'end_time', 'modified_date', 'month',
       'hour', 'council_district_start', 'council_district_end',
       'census_geoid_start', 'census_geoid_end',
       'start_time_us_central', 'end_time_us_central'], axis=1)

new_df['trip_duration'] = new_df['trip_duration'].astype('int')     


week_men_median = {}
week_men_median['Days'] = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

### Mean ###
week_men_median['Mean'] = []
# Monday
Monday = new_df.query("day_of_week == '0'")
week_men_median['Mean'].append(Monday['trip_duration'].describe()[1])
# Tuesday
Tuesday = new_df.query("day_of_week == '1'")
week_men_median['Mean'].append(Tuesday['trip_duration'].describe()[1])
# Wednesday
Wednesday = new_df.query("day_of_week == '2'")
week_men_median['Mean'].append(Wednesday['trip_duration'].describe()[1])
# Thursday
Thursday = new_df.query("day_of_week == '3'")
week_men_median['Mean'].append(Thursday['trip_duration'].describe()[1])
# Friday
Friday = new_df.query("day_of_week == '4'")
week_men_median['Mean'].append(Friday['trip_duration'].describe()[1])
# Saturday
Saturday = new_df.query("day_of_week == '5'")
week_men_median['Mean'].append(Saturday['trip_duration'].describe()[1])
# Sunday
Sunday = new_df.query("day_of_week == '6'")
week_men_median['Mean'].append(Sunday['trip_duration'].describe()[1])



### Median ###
week_men_median['Median'] = []
# Monday
Monday = new_df.query("day_of_week == '0'")
week_men_median['Median'].append(Monday['trip_duration'].describe()[5])
# Tuesday
Tuesday = new_df.query("day_of_week == '1'")
week_men_median['Median'].append(Tuesday['trip_duration'].describe()[5])
# Wednesday
Wednesday = new_df.query("day_of_week == '2'")
week_men_median['Median'].append(Wednesday['trip_duration'].describe()[5])
# Thursday
Thursday = new_df.query("day_of_week == '3'")
week_men_median['Median'].append(Thursday['trip_duration'].describe()[5])
# Friday
Friday = new_df.query("day_of_week == '4'")
week_men_median['Median'].append(Friday['trip_duration'].describe()[5])
# Saturday
Saturday = new_df.query("day_of_week == '5'")
week_men_median['Median'].append(Saturday['trip_duration'].describe()[5])
# Sunday
Sunday = new_df.query("day_of_week == '6'")
week_men_median['Median'].append(Sunday['trip_duration'].describe()[5])

# week_men_median


men_median_df = pd.DataFrame(data=week_men_median)
men_median_df.plot(kind='bar', x='Days', y= 'Mean', color=[0.7,0.25,0.4])
men_median_df.plot(kind='bar', x='Days', y= 'Median', color=[0.7,0.25,0.4])
men_median_df


week_men_median = {}
week_men_median['Days'] = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

### Mean ###
week_men_median['Mean'] = []
# Monday
Monday = new_df.query("day_of_week == '0' and year == '2020'")
week_men_median['Mean'].append(Monday['trip_duration'].describe()[1])
# Tuesday
Tuesday = new_df.query("day_of_week == '1' and year == '2020'")
week_men_median['Mean'].append(Tuesday['trip_duration'].describe()[1])
# Wednesday
Wednesday = new_df.query("day_of_week == '2' and year == '2020'")
week_men_median['Mean'].append(Wednesday['trip_duration'].describe()[1])
# Thursday
Thursday = new_df.query("day_of_week == '3' and year == '2020'")
week_men_median['Mean'].append(Thursday['trip_duration'].describe()[1])
# Friday
Friday = new_df.query("day_of_week == '4' and year == '2020'")
week_men_median['Mean'].append(Friday['trip_duration'].describe()[1])
# Saturday
Saturday = new_df.query("day_of_week == '5' and year == '2020'")
week_men_median['Mean'].append(Saturday['trip_duration'].describe()[1])
# Sunday
Sunday = new_df.query("day_of_week == '6' and year == '2020'")
week_men_median['Mean'].append(Sunday['trip_duration'].describe()[1])



### Median ###
week_men_median['Median'] = []
# Monday
Monday = new_df.query("day_of_week == '0' and year == '2020'")
week_men_median['Median'].append(Monday['trip_duration'].describe()[5])
# Tuesday
Tuesday = new_df.query("day_of_week == '1' and year == '2020'")
week_men_median['Median'].append(Tuesday['trip_duration'].describe()[5])
# Wednesday
Wednesday = new_df.query("day_of_week == '2' and year == '2020'")
week_men_median['Median'].append(Wednesday['trip_duration'].describe()[5])
# Thursday
Thursday = new_df.query("day_of_week == '3' and year == '2020'")
week_men_median['Median'].append(Thursday['trip_duration'].describe()[5])
# Friday
Friday = new_df.query("day_of_week == '4' and year == '2020'")
week_men_median['Median'].append(Friday['trip_duration'].describe()[5])
# Saturday
Saturday = new_df.query("day_of_week == '5' and year == '2020'")
week_men_median['Median'].append(Saturday['trip_duration'].describe()[5])
# Sunday
Sunday = new_df.query("day_of_week == '6' and year == '2020'")
week_men_median['Median'].append(Sunday['trip_duration'].describe()[5])

# week_men_median


men_median_df_2020 = pd.DataFrame(data=week_men_median)
men_median_df_2020.plot(kind='bar', x='Days', y= 'Mean', color=[0.7,0.25,0.4])
men_median_df_2020.plot(kind='bar', x='Days', y= 'Median', color=[0.7,0.25,0.4])
men_median_df_2020


week_men_median = {}
week_men_median['Days'] = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

### Mean ###
week_men_median['Mean'] = []
# Monday
Monday = new_df.query("day_of_week == '0' and year == '2021'")
week_men_median['Mean'].append(Monday['trip_duration'].describe()[1])
# Tuesday
Tuesday = new_df.query("day_of_week == '1' and year == '2021'")
week_men_median['Mean'].append(Tuesday['trip_duration'].describe()[1])
# Wednesday
Wednesday = new_df.query("day_of_week == '2' and year == '2021'")
week_men_median['Mean'].append(Wednesday['trip_duration'].describe()[1])
# Thursday
Thursday = new_df.query("day_of_week == '3' and year == '2021'")
week_men_median['Mean'].append(Thursday['trip_duration'].describe()[1])
# Friday
Friday = new_df.query("day_of_week == '4' and year == '2021'")
week_men_median['Mean'].append(Friday['trip_duration'].describe()[1])
# Saturday
Saturday = new_df.query("day_of_week == '5' and year == '2021'")
week_men_median['Mean'].append(Saturday['trip_duration'].describe()[1])
# Sunday
Sunday = new_df.query("day_of_week == '6' and year == '2021'")
week_men_median['Mean'].append(Sunday['trip_duration'].describe()[1])



### Median ###
week_men_median['Median'] = []
# Monday
Monday = new_df.query("day_of_week == '0' and year == '2021'")
week_men_median['Median'].append(Monday['trip_duration'].describe()[5])
# Tuesday
Tuesday = new_df.query("day_of_week == '1' and year == '2021'")
week_men_median['Median'].append(Tuesday['trip_duration'].describe()[5])
# Wednesday
Wednesday = new_df.query("day_of_week == '2' and year == '2021'")
week_men_median['Median'].append(Wednesday['trip_duration'].describe()[5])
# Thursday
Thursday = new_df.query("day_of_week == '3' and year == '2021'")
week_men_median['Median'].append(Thursday['trip_duration'].describe()[5])
# Friday
Friday = new_df.query("day_of_week == '4' and year == '2021'")
week_men_median['Median'].append(Friday['trip_duration'].describe()[5])
# Saturday
Saturday = new_df.query("day_of_week == '5' and year == '2021'")
week_men_median['Median'].append(Saturday['trip_duration'].describe()[5])
# Sunday
Sunday = new_df.query("day_of_week == '6' and year == '2021'")
week_men_median['Median'].append(Sunday['trip_duration'].describe()[5])

# week_men_median


men_median_df_2021 = pd.DataFrame(data=week_men_median)
men_median_df_2021.plot(kind='bar', x='Days', y= 'Mean', color=[0.7,0.25,0.4])
men_median_df_2021.plot(kind='bar', x='Days', y= 'Median', color=[0.7,0.25,0.4])
men_median_df_2021


week_men_median = {}
week_men_median['Days'] = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

### Mean ###
week_men_median['Mean'] = []
# Monday
Monday = new_df.query("day_of_week == '0' and year == '2022'")
week_men_median['Mean'].append(Monday['trip_duration'].describe()[1])
# Tuesday
Tuesday = new_df.query("day_of_week == '1' and year == '2022'")
week_men_median['Mean'].append(Tuesday['trip_duration'].describe()[1])
# Wednesday
Wednesday = new_df.query("day_of_week == '2' and year == '2022'")
week_men_median['Mean'].append(Wednesday['trip_duration'].describe()[1])
# Thursday
Thursday = new_df.query("day_of_week == '3' and year == '2022'")
week_men_median['Mean'].append(Thursday['trip_duration'].describe()[1])
# Friday
Friday = new_df.query("day_of_week == '4' and year == '2022'")
week_men_median['Mean'].append(Friday['trip_duration'].describe()[1])
# Saturday
Saturday = new_df.query("day_of_week == '5' and year == '2022'")
week_men_median['Mean'].append(Saturday['trip_duration'].describe()[1])
# Sunday
Sunday = new_df.query("day_of_week == '6' and year == '2022'")
week_men_median['Mean'].append(Sunday['trip_duration'].describe()[1])



### Median ###
week_men_median['Median'] = []
# Monday
Monday = new_df.query("day_of_week == '0' and year == '2022'")
week_men_median['Median'].append(Monday['trip_duration'].describe()[5])
# Tuesday
Tuesday = new_df.query("day_of_week == '1' and year == '2022'")
week_men_median['Median'].append(Tuesday['trip_duration'].describe()[5])
# Wednesday
Wednesday = new_df.query("day_of_week == '2' and year == '2022'")
week_men_median['Median'].append(Wednesday['trip_duration'].describe()[5])
# Thursday
Thursday = new_df.query("day_of_week == '3' and year == '2022'")
week_men_median['Median'].append(Thursday['trip_duration'].describe()[5])
# Friday
Friday = new_df.query("day_of_week == '4' and year == '2022'")
week_men_median['Median'].append(Friday['trip_duration'].describe()[5])
# Saturday
Saturday = new_df.query("day_of_week == '5' and year == '2022'")
week_men_median['Median'].append(Saturday['trip_duration'].describe()[5])
# Sunday
Sunday = new_df.query("day_of_week == '6' and year == '2022'")
week_men_median['Median'].append(Sunday['trip_duration'].describe()[5])

# week_men_median


men_median_df_2022 = pd.DataFrame(data=week_men_median)
men_median_df_2022.plot(kind='bar', x='Days', y= 'Mean', color=[0.7,0.25,0.4])
men_median_df_2022.plot(kind='bar', x='Days', y= 'Median', color=[0.7,0.25,0.4])
men_median_df_2022


