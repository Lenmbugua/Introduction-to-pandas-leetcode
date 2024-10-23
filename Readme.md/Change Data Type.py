import pandas as pd
def changeDatatype(df):
    df['grade'] = df['grade'].astype(int)
    return df
if __name__ == "__main__":
    data = {
        'student_id': [1, 2],
        'name': ['Ava', 'Kate'],
        'age': [6, 15],
        'grade': [73.0, 87.0]
    }
    students = pd.DataFrame(data)
    result_table = changeDatatype(students)
    
    print(result_table)