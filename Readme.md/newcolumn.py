import pandas as pd

def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
    # Modify the 'employees' DataFrame, not 'df'
    employees['bonus'] = employees['salary'] * 2
    return employees

# Example of how you would use the function:
# Assuming 'employees' is the DataFrame you pass to the function
employees = pd.DataFrame({
    'employee': ['Alice', 'Bob', 'Charlie'],
    'salary': [50000, 60000, 55000]
})

# Call the function
updated_employees = createBonusColumn(employees)

# Display the updated DataFrame
print(updated_employees)
