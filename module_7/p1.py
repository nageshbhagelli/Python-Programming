# 7.a. Create a Pandas Data Frame from a Dictionary. The dictionary should containpassenger details such 
# as name, age, and fare. Then, display the created Data Frame.
import pandas as pd # 7.a
data = {
'Name': ['Alice', 'Bob', 'Charlie'],
'Age': [25, 30, 22],
'Fare': [100, 150, 120]
}
df = pd.DataFrame(data)
print(df)