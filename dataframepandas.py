#using dictionary
import pandas as pd

data = {
    'Name': ['Shreya', 'Shravani', 'Sandhya', 'Tanisha'],
    'Age': [24, 27, 22, 32],
    'City': ['Pune', 'Mumbai', 'Delhi', 'Chennai']
}


#using list
df = pd.DataFrame(data)
print(df)

data = [['Shreya', 24, 'Pune'],
        ['Shravani', 27, 'Mumbai'],
        ['Sandhya', 22, 'Delhi']]

df = pd.DataFrame(data, columns=['Name', 'Age', 'City'])
print(df)

