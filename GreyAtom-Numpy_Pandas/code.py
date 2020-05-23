# --------------
# Importing header files
import numpy as np
import warnings

warnings.filterwarnings('ignore')

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]

#Reading file
data = np.genfromtxt(path, delimiter=",", skip_header=1)
print(data.shape)
census=np.concatenate((data, new_record),axis = 0)

print(census.shape)
#Code starts here

age=census[:,0]
max_age=np.max(age)
min_age=np.min(age)
age_mean=np.mean(age)
age_std=np.std(age)

race_0=census[census[:,2]==0]
race_1=census[census[:,2]==1]
race_2=census[census[:,2]==2]
race_3=census[census[:,2]==3]

minarr=[0,1,2,3]

len_0=len(race_0)
len_1=len(race_1)
len_2=len(race_2)
len_3=len(race_3)

minlen=min(len_0,len_1,len_2,len_3)

if minlen==len_0: minority_race=minarr[0]
elif minlen==len_1: minority_race=minarr[1]
elif minlen==len_2: minority_race=minarr[2]
else : minority_race=minarr[3]
print(minority_race)

senior_citizens=census[census[:,0] >60]
working_hours_sum=senior_citizens.sum(axis=0)[6]
senior_citizens_len=len(senior_citizens)
avg_working_hours=working_hours_sum/senior_citizens_len
print(avg_working_hours)

high=census[census[:,1]>10]
low=census[census[:,1]<=10]

avg_pay_high=high[:,7].mean()
avg_pay_low=low[:,7].mean()
print(avg_pay_low)



