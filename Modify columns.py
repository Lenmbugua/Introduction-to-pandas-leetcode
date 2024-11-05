import pandas as pd

def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees['salary'] = employees['salary'] * 2
    return employees

# Example usage:
data = {'name': ['Jack', 'Piper', 'Mia', 'Ulysses'],
        'salary': [19666, 74754, 62509, 54866]}
employees = pd.DataFrame(data)
modified_employees = modifySalaryColumn(employees)
print(modified_employees)