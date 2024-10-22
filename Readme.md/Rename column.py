import pandas as pd

def renameColumns(employees: pd.DataFrame) -> pd.DataFrame:
    employees.rename(columns={
        'id': 'student_id',
        'first': 'first_name',
        'last': 'last_name',
        'age': 'age_in_years'
    }, inplace=True)
    return employees

# Example usage:
data = {
    'id': [1, 2, 3, 4, 5],
    'first': ['Mason', 'Ava', 'Taylor', 'Georgia', 'Thomas'],
    'last': ['King', 'Wright', 'Hall', 'Thompson', 'Moore'],
    'age': [6, 7, 16, 18, 10]
}

students = pd.DataFrame(data)
result_table = renameColumns(students)
print(result_table)
