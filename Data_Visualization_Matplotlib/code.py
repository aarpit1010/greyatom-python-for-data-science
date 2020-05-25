# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#Reading the file
data=pd.read_csv(path)

# Step 1
loan_status=data['Loan_Status'].value_counts()
plt.bar(loan_status.index,loan_status)
plt.show()


# Step 2
#Plotting an unstacked bar plot

property_and_loan=data.groupby(['Property_Area','Loan_Status']).size().unstack()
property_and_loan.plot(kind='bar',stacked=False)
plt.xlabel('Property Area')
plt.ylabel('Loan Status')
plt.xticks(rotation=45)
plt.show()


# Step 3
#Plotting a stacked bar plot

education_and_loan=data.groupby(['Education','Loan_Status']).size().unstack()
education_and_loan.plot(kind='bar',stacked=True)
plt.xlabel('Education Status')
plt.ylabel('Loan Status')
plt.xticks(rotation=45)
plt.show()


# Step 4 
#Subsetting the dataframe based on 'Education' column

graduate=data[data['Education']=='Graduate']
not_graduate=data[data['Education']=='Not Graduate']

pd.Series(graduate['LoanAmount']).plot(kind='density', label='Graduate')
pd.Series(not_graduate['LoanAmount']).plot(kind='density', label='Not Graduate')


# Step 5
#Setting up the subplots

fig ,(ax_1,ax_2,ax_3)=plt.subplots(nrows=3, ncols=1)

data.plot(x='ApplicantIncome', y='LoanAmount', kind='scatter', ax=ax_1)
ax_1.set_title('Applicant Income')

data.plot(x='CoapplicantIncome', y='LoanAmount', kind='scatter', ax=ax_2)
ax_2.set_title('Coapplicant Income')

data['TotalIncome']=data['ApplicantIncome']+ data['CoapplicantIncome']

data.plot(x='TotalIncome', y='LoanAmount', kind='scatter', ax=ax_3)
ax_3.set_title('Total Income')

plt.tight_layout()



