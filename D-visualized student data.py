# Student Data Visualization Project
# Author: Habiba Khan
# Step: Import Cleaned Data → Visualize → Generate Insights

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Step 1: Load Cleaned Data
df = pd.read_csv("cleaned_student_data.csv")
print("✅ Data Loaded Successfully!")
print(df.head())
# Step 2: Visualization using Matplotlib
#Average Marks by Gender
gender_group = df.groupby('Gender')[['Math', 'Science', 'English']].mean()
gender_group.plot(kind='bar', figsize=(6,4))
plt.title('Average Marks by Gender')
plt.ylabel('Average Marks')
plt.xlabel('Gender')
plt.tight_layout()
plt.savefig("average_marks_by_gender.png")
plt.show()

#  Attendance vs Math Marks
plt.figure(figsize=(6,4))
plt.scatter(df['Attendance'], df['Math'], color='purple')
plt.title('Attendance vs Math Marks')
plt.xlabel('Attendance (%)')
plt.ylabel('Math Marks')
plt.tight_layout()
plt.savefig("average_marks_by_gender.png")
plt.show()

#  Study Hours vs Average Marks
df['Avg_Marks'] = df[['Math', 'Science', 'English']].mean(axis=1)
plt.figure(figsize=(6,4))
plt.scatter(df['Study_Hours'], df['Avg_Marks'], color='green')
plt.title('Study Hours vs Average Marks')
plt.xlabel('Study Hours per Day')
plt.ylabel('Average Marks')
plt.tight_layout()
plt.savefig("average_marks_by_gender.png")
plt.show()

# 4️Activities vs Pass/Fail Count
activity_result = df.groupby(['Activities', 'Final_Result']).size().unstack()
activity_result.plot(kind='bar', figsize=(6,4))
plt.title('Activities vs Final Result')
plt.xlabel('Participated in Activities')
plt.ylabel('Number of Students')
plt.tight_layout()
plt.savefig("average_marks_by_gender.png")
plt.show()
corr = df[['Math','Science','English','Attendance','Study_Hours']].corr()
print("\n📈 Correlation Matrix:")
print(corr)
# Step 3: Insights
print("\n Average Marks by Gender:\n", df.groupby('Gender')['Avg_Marks'].mean())
print("\n Average Marks by Activities:\n", df.groupby('Activities')['Avg_Marks'].mean())
print("\n Students Passed:", (df['Final_Result'] == 'pass').sum())
print(" Students Failed:", (df['Final_Result'] == 'fail').sum())