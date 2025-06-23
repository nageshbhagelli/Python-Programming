# 7.b.1 Read the Titanic dataset from a CSV file (titanic.csv) into a Pandas Data Frame anddisplay the first few rows.
titanic = pd.read_csv('titanic.csv') # 7.b.1
print(titanic.head())

# 7.b.2 Filter the dataset to select only the rows where the passenger's age is greater than 30,and display the filtered results.
filtered = titanic[titanic['Age'] > 30] # 7.b.2
print(filtered)

# 7.b.3 Replace missing values in the age column with a default value (e.g., 30) and displaythe updated Data Frame.
titanic['Age'].fillna(30, inplace=True) # 7.b.3
print(titanic.head())

# 7.b.4 Remove any rows containing missing values from the dataset and display the cleanedData Frame.
cleaned = titanic.dropna() # 7.b.4
print(cleaned.head())

# 7.b.5 Determine and display the maximum and minimum values in the age column.
print("Max Age:", titanic['Age'].max()) # 7.b.5
print("Min Age:", titanic['Age'].min())