import pandas as pd
import requests

data = {
    'name': ['A', 'B', 'C'],
    'age': [30, 21, 10],
    'address': ['pune', 'mumbai', 'pune']
}

print('Student Details')

df = pd.DataFrame(data)

print(df)

print('API data')

response = requests.get('https://jsonplaceholder.typicode.com/users')
print(response.json())