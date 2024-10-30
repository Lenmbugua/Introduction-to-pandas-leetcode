import pandas as pd

def pivotTable(weather):
    # Pivot the DataFrame without resetting the index
    result_table = weather.pivot(index='month', columns='city', values='temperature')
    return result_table

# Sample DataFrame
weather = pd.DataFrame({
    'city': ['Jacksonville', 'Jacksonville', 'Jacksonville', 'Jacksonville', 'Jacksonville',
             'ElPaso', 'ElPaso', 'ElPaso', 'ElPaso', 'ElPaso'],
    'month': ['January', 'February', 'March', 'April', 'May',
              'January', 'February', 'March', 'April', 'May'],
    'temperature': [13, 23, 38, 5, 34, 20, 6, 26, 2, 43]
})

# Call the function with the weather DataFrame
result_table = pivotTable(weather)
print(result_table)
