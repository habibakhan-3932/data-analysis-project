import pandas as pd
import numpy as np

# Load  CSV file 
df = pd.read_csv("messy_student_data.csv")

# Preview the raw data
print("Raw Data Preview:")
print(df.head())

#  Basic info
print("\nBasic Info:")
print(df.info())

print("\n Missing Values:")
print(df.isnull().sum())

print("\n Duplicate Rows:", df.duplicated().sum())

# Remove duplicates
df.drop_duplicates(inplace=True)

# Clean 'Name'
df['Name'] = df['Name'].str.strip().str.title()

# Clean 'Gender'
df['Gender'] = df['Gender'].str.strip().str.lower()
df['Gender'] = df['Gender'].replace({
    'malee': 'male', 'm': 'male',
    'femal': 'female', 'f': 'female'
})
df = df[df['Gender'].isin(['male', 'female'])]

# Fix 'Age'
df.loc[(df['Age'] < 15) | (df['Age'] > 30), 'Age'] = np.nan
df['Age'] = df['Age'].fillna(df['Age'].median())

#Clean 'Attendance'
df.loc[(df['Attendance'] < 0) | (df['Attendance'] > 100), 'Attendance'] = np.nan
df['Attendance'] = df['Attendance'].fillna(df['Attendance'].mean().round(2))

#Clean marks
for subject in ['Math', 'Science', 'English']:
    df.loc[(df[subject] < 0) | (df[subject] > 100), subject] = np.nan
    df[subject] = df[subject].fillna(df[subject].mean().round(2))

#Clean 'Study_Hours'
df.loc[(df['Study_Hours'] < 0) | (df['Study_Hours'] > 15), 'Study_Hours'] = np.nan
df['Study_Hours'] = df['Study_Hours'].fillna(df['Study_Hours'].median())

#Clean 'Activities'
df['Activities'] = df['Activities'].astype(str).str.strip().str.lower()
df['Activities'] = df['Activities'].replace({
    'ye': 'yes', 'n0': 'no', 'yes ': 'yes', 'no ': 'no', '': np.nan
})
df['Activities'] = df['Activities'].fillna('no')

#Clean 'Final_Result'
df['Final_Result'] = df['Final_Result'].astype(str).str.strip().str.lower()
df['Final_Result'] = df['Final_Result'].replace({
    'pass ': 'pass', 'faill': 'fail', '': np.nan
})

# Fill missing result based on marks
avg_marks = df[['Math', 'Science', 'English']].mean(axis=1)
df.loc[df['Final_Result'].isna(), 'Final_Result'] = np.where(avg_marks >= 40, 'pass', 'fail')

#Round numeric columns
df[['Attendance', 'Math', 'Science', 'English', 'Study_Hours']] = df[['Attendance', 'Math', 'Science', 'English', 'Study_Hours']].round(2)

#Save cleaned CSV
df.to_csv("cleaned_student_data.csv", index=False)

print("Data cleaned successfully and saved as cleaned_student_data.csv")
print(df.head())