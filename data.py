import pandas as pd

data = {
    'name': ['A', 'B', 'C'],
    'age': [30, 21, 10],
    'address': ['pune', 'mumbai', 'pune']
}

print('Student Details')

df = pd.DataFrame(data)

print(df)