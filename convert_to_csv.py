import pandas as pd

# Read the Excel file
df1 = pd.read_excel('0.92-0.99.xlsx')
df2 = pd.read_excel('0.70-0.80.xlsx')
df3 = pd.read_excel('0.65-0.80.xlsx')
df4 = pd.read_excel('0.55-0.70.xlsx')

# Export the DataFrame to CSV
df1.to_csv('0.92-0.99.csv', index=False)
df2.to_csv('0.70-0.80.csv', index=False)
df3.to_csv('0.65-0.80.csv', index=False)
df4.to_csv('0.55-0.70.csv', index=False)
