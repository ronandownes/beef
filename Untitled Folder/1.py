import pandas as pd
import numpy as np

data = {
    'customer_id': [1, 2, 3, 4, 5, 6, 7, 8, 9],
    'age': [25, 32, np.nan, 45, 26, 31, np.nan, 42, 27],
    'gender': ['F', 'M', 'F', 'M', 'F', 'F', 'M', 'F', 'M'],
    'income': [60000, 75000, 45000, np.nan, 65000, 55000, 80000, np.nan, 70000],
    'purchase_amount': [50, 100, 75, 200, 75, 50, 150, 100, 125]
}

df = pd.DataFrame(data)
print(df.head())




import pandas as pd

# Load data into a dataframe from an online CSV file
url = 'https://people.sc.fsu.edu/~jburkardt/data/csv/hw_200.csv'
df = pd.read_csv(url)

# Print the first five rows of the dataframe
print(df.head())


df.shape

