import pandas as pd

df_list = pd.DataFrame({'Item': ['Bread', 'Eggs', 'Lunch Meat', 'Milk'], 'Qty': [1,12,1,1]})
s_list = pd.Series([1,12,1,1], index=['Bread', 'Eggs', 'Lunch Meat', 'Milk'], name= 'Grocery List')

print(df_list)
print()
print(s_list)