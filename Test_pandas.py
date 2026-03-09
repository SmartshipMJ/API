import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}

df = pd.DataFrame(data)
print(f"DataFrame:\n{df}\n")

# Accessing columns
names = df['Name']
print(f"Names:\n{names}\n")

# Filtering rows
age_above_30 = df[df['Age'] > 30]
print(f"People older than 30:\n{age_above_30}\n")

# Adding a new column
df['Salary'] = [50000, 60000, 70000]
print(f"DataFrame with Salary column:\n{df}\n")