import pandas as pd

def meltTable(report: pd.DataFrame) -> pd.DataFrame:
    reshaped_report = pd.melt(report, id_vars=['product'], 
                              value_vars=['quarter_1', 'quarter_2', 'quarter_3', 'quarter_4'],
                              var_name='quarter', value_name='sales')
    return reshaped_report

# Example usage:
data = {
    'product': ['Umbrella', 'SleepingBag'],
    'quarter_1': [417, 800],
    'quarter_2': [224, 936],
    'quarter_3': [379, 93],
    'quarter_4': [611, 875]
}

report = pd.DataFrame(data)
result_table = meltTable(report)
print(result_table)
