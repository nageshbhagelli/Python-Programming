# 9.1 Rank employees based on their salary within their department.
employee = pd.read_csv('Employee.csv') 
employee['Rank'] = employee.groupby('Department')['Salary'].rank(ascending=False)
print(employee[['Name', 'Department', 'Salary', 'Rank']])

# 9.2 Which JoiningYear has the most employees still in the company?
print("JoiningYear with most employees still in company:", employee[employee['Status'] =='Working']['JoiningYear'].mode()[0])

# 9.3 Find employees who are above 50 years old and still working.
above50 = employee[(employee['Age'] > 50) & (employee['Status'] == 'Working')]
print("Employees above 50 and working:\n", above50)

# 9.4 Compute average salary increase trend (assuming salary grows by 5% annually sincejoining).
employee['Years'] = 2025 - employee['JoiningYear']
employee['SalaryTrend'] = employee['Salary'] * (1.05 ** employee['Years'])
print("Average salary increase trend:", employee['SalaryTrend'].mean())

# 9.5 Create bins of Age and find average salary for each bin.
bins = pd.cut(employee['Age'], bins=[20, 30, 40, 50, 60, 70])
print(employee.groupby(bins)['Salary'].mean())

# 9.6 Create a pivot table showing total number of employees by JoiningYear and Department.
pivot = employee.pivot_table(index='JoiningYear', columns='Department', values='Name',aggfunc='count')
print("Pivot table:\n", pivot)

# 9.7 Identify if remote work is more common in a specific department.
print(employee.groupby('Department')['RemoteWork'].mean())

# 9.8 Find standard deviation of salaries for each department.
print(employee.groupby('Department')['Salary'].std())

# 9.9 Plot a histogram of Performance Score for male employees.
import matplotlib.pyplot as plt
male_perf = employee[employee['Gender'] == 'Male']['PerformanceScore']
plt.hist(male_perf, bins=10)
plt.title('Performance Score for Male Employees')
plt.xlabel('Score')
plt.ylabel('Frequency')
plt.show()

# 9.10 How does Work Hours PerWeek affect the chance of leaving the company? Find top 5highest earning employees in each department.
print(employee.groupby('WorkHoursPerWeek')['LeftCompany'].mean())
top5 = employee.groupby('Department').apply(lambda x: x.nlargest(5, 'Salary'))
print("Top 5 highest earning employees in each department:\n", top5)