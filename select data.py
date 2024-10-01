import pandas as pd

def selectData(df: pd.DataFrame) -> pd.DataFrame:
    # Select the 'name' and 'age' where student_id is 101
    student_info = df.loc[df['student_id'] == 101, ['name', 'age']]
    
    return student_info

# Sample data
data = {
    'student_id': [3, 151, 181, 84, 171, 63, 104, 193, 42, 101, 36, 11],
    'name': ['Alice', 'Charlie', 'Hannah', 'Lily', 'Finn', 'Julia', 'Isaac', 'Piper', 'Thomas', 'Taylor', 'Michael', 'Eve'],
    'age': [13, 14, 10, 16, 6, 13, 15, 6, 16, 7, 16, 5]
}

# Create DataFrame
df = pd.DataFrame(data)

# Call the function and print the result
result = selectData(df)
print(result)
