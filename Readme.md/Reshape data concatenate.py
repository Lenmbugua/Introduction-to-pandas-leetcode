import pandas as pd

# Define the function to concatenate tables
def concatenateTables(df1, df2):
    return pd.concat([df1, df2], ignore_index=True)

# Example usage
if __name__ == "__main__":
    # Sample DataFrames
    df1 = pd.DataFrame({
        'student_id': [1, 2, 3, 4],
        'name': ['Mason', 'Ava', 'Taylor', 'Georgia'],
        'age': [8, 6, 15, 17]
    })
    df2 = pd.DataFrame({
        'student_id': [5, 6],
        'name': ['Leo', 'Alex'],
        'age': [7, 7]
    })

    # Call the function
    result_table = concatenateTables(df1, df2)
    print(result_table)
