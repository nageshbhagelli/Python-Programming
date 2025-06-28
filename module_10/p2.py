import pandas as pd

# Load the dataset
df = pd.read_csv("module_10/Student_Dataset.csv")

# i. Convert columns to category dtype
df['Department'] = df['Department'].astype('category')
df['Internship_Completed'] = df['Internship_Completed'].astype('category')
df['Year'] = df['Year'].astype('category')

# ii. Create Performance_Category column
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

# iii. Average GPA and Project Score for each Department
avg_scores = df.groupby('Department')[['GPA', 'Project_Score']].mean()
print("Average GPA and Project Score per Department:")
print(avg_scores)

# iv. Count of students by Internship status and Year
internship_counts = df['Internship_Completed'].value_counts()
year_counts = df['Year'].value_counts()

print("\nNumber of Students by Internship Completion:")
print(internship_counts)

print("\nNumber of Students by Year:")
print(year_counts)
