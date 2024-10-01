import pandas as pd

def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    # Get the first 3 rows from the employees DataFrame
    first_three_rows = employees.head(3)
    return first_three_rows

# Example usage:
# Input DataFrame
data = {
    'employee_id': [3, 90, 9, 60, 49, 43],
    'name': ['Bob', 'Alice', 'Tatiana', 'Annabelle', 'Jonathan', 'Khaled'],
    'department': ['Operations', 'Sales', 'Engineering', 'InformationTechnology', 'HumanResources', 'Administration'],
    'salary': [48675, 11096, 33805, 37678, 23793, 40454]
}

# Create DataFrame
employees = pd.DataFrame(data)

# Get the first 3 rows
result = selectFirstRows(employees)

# Display the result
print(result)
