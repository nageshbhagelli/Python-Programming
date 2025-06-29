import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv("module_10/Student_Dataset.csv")

def categorize_performance(gpa):
    if gpa >= 8.5:
        return 'Excellent'
    elif gpa >= 7.0:
        return 'Good'
    elif gpa >= 5.0:
        return 'Average'
    else:
        return 'Poor'

df['Performance_Category'] = df['GPA'].apply(categorize_performance)
# Ensure Performance_Category exists (if not already created)

# i. GPA distribution across Departments
plt.figure(figsize=(8,5))
sns.boxplot(x='Department', y='GPA', data=df)
plt.title('GPA Distribution Across Departments')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# ii. Project Score distribution based on Internship Completed
plt.figure(figsize=(8,5))
sns.violinplot(x='Internship_Completed', y='Project_Score', data=df)
plt.title('Project Score by Internship Completion')
plt.tight_layout()
plt.show()

# iii. Number of students in each Performance Category
plt.figure(figsize=(6,4))
sns.countplot(x='Performance_Category', data=df, order=['Excellent', 'Good', 'Average', 'Poor'], palette='Set2')
plt.title('Student Count by Performance Category')
plt.tight_layout()
plt.show()

# iv. Correlation heatmap
plt.figure(figsize=(6,5))
corr = df[['GPA', 'Attendance (%)', 'Project_Score']].corr()
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.tight_layout()
plt.show()

# v. Pairplot colored by Year
sns.pairplot(df, vars=['GPA', 'Attendance (%)', 'Project_Score'], hue='Year', palette='husl')
plt.suptitle('Pairplot: GPA, Attendance, Project Score by Year', y=1.02)
plt.tight_layout()
plt.show()