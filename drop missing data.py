import pandas as pd

def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
    # Remove rows where 'name' column has missing values
    students_cleaned = students.dropna(subset=['name'])
    
    # Return the cleaned DataFrame
    return students_cleaned

# Example input DataFrame
data = {'student_id': [32, 217, 779, 849],
        'name': ['Piper', None, 'Georgia', 'Willow'],
        'age': [5, 19, 20, 14]}

students = pd.DataFrame(data)

# Call the function
result_table = dropMissingData(students)

# Output the cleaned DataFrame
print(result_table)


    